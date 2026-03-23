import { NextResponse } from 'next/server';
import { GoogleGenAI } from '@google/genai';

export async function POST(request: Request) {
  try {
    const { code, apiKey } = await request.json();

    if (!code) {
      return NextResponse.json({ error: 'Code or description is required' }, { status: 400 });
    }

    // Initialize with provided API key, or default to the server's environment variable
    const ai = new GoogleGenAI({ apiKey: apiKey || process.env.GEMINI_API_KEY });
    
    const prompt = `
You are an expert Python QA Engineer and Backend Developer. 
Your task is to write structured, comprehensive pytest test cases for the following python code or description:

${code}

Requirements:
1. Use the pytest framework.
2. Include a variety of test cases:
   - Happy path (valid inputs)
   - Edge cases (boundary values, extreme cases)
   - Invalid inputs (wrong types, missing values, etc.) ensuring proper exception handling using pytest.raises.
3. Provide ONLY the raw Python code for the tests as your output. 
4. DO NOT include markdown code blocks (e.g., no \`\`\`python). DO NOT include ANY explanations or text outside the code.
`;

    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: prompt,
    });

    let text = response.text || '';
    if (text.startsWith("```python")) text = text.slice(9);
    else if (text.startsWith("```")) text = text.slice(3);
    if (text.endsWith("```")) text = text.slice(0, -3);
    text = text.trim();

    return NextResponse.json({ result: text });
  } catch (error: any) {
    console.error(error);
    return NextResponse.json({ error: error.message || 'Failed to generate test cases. Please ensure your API key is correct.' }, { status: 500 });
  }
}
