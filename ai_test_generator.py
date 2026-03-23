import os
import argparse
import sys

def generate_test_cases_gemini(function_code_or_description, api_key=None, model="gemini-2.5-flash"):
    try:
        from google import genai
    except ImportError:
        print("Error: The 'google-genai' library is missing.")
        print("Please install it by running: pip install google-genai")
        sys.exit(1)

    # Set up Gemini with the given or environmental API key
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        print("Error: Gemini API Key not found.")
        print("Set it using: $env:GEMINI_API_KEY='your-key' or pass it using --api-key")
        sys.exit(1)
        
    client = genai.Client(api_key=key)
    
    prompt = f"""
You are an expert Python QA Engineer and Backend Developer. 
Your task is to write structured, comprehensive pytest test cases for the following python code or description:

{function_code_or_description}

Requirements:
1. Use the `pytest` framework.
2. Include a variety of test cases:
   - Happy path (valid inputs)
   - Edge cases (boundary values, extreme cases)
   - Invalid inputs (wrong types, missing values, etc.) ensuring proper exception handling using `pytest.raises`.
3. Provide ONLY the raw Python code for the tests as your output. 
4. DO NOT include markdown code blocks (e.g., no ```python). DO NOT include ANY explanations or text outside the code.
"""
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    return response.text

def main():
    parser = argparse.ArgumentParser(description="AI Test Case Generator (Powered by Google Gemini SDK)")
    parser.add_argument("-d", "--description", type=str, help="A description or string containing the function to test")
    parser.add_argument("-f", "--file", type=str, help="A python file containing the function(s) to test")
    parser.add_argument("-o", "--output", type=str, default="test_generated.py", help="Output python file for generated tests")
    parser.add_argument("--api-key", type=str, help="Your Gemini API key")
    parser.add_argument("--model", type=str, default="gemini-2.5-flash", help="Model to use (default: gemini-2.5-flash)")
    
    args = parser.parse_args()
    
    source = ""
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as file:
                source = file.read()
        except FileNotFoundError:
            print(f"Error: Could not find file {args.file}")
            sys.exit(1)
    elif args.description:
        source = args.description
    else:
        print("Error: You must provide either --description or --file.")
        parser.print_help()
        sys.exit(1)

    print(f"Generating test cases using Google GenAI SDK ({args.model})... Please wait.")
    
    try:
        content = generate_test_cases_gemini(source, api_key=args.api_key, model=args.model)
            
        # Cleanup potential markdown wrap just in case Gemini occasionally disobeys the prompt
        if content.startswith("```python"): content = content[9:]
        elif content.startswith("```"): content = content[3:]
        if content.endswith("```"): content = content[:-3]
        content = content.strip()
        
        with open(args.output, "w", encoding="utf-8") as out_file:
            out_file.write(content)
            
        print(f"Success! Generated test cases have been saved to '{args.output}'")
        print("\nRun the tests with: pytest " + args.output + " -v")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
