# AI Test Case Generator

This project is a Python-based utility that automatically generates structured, comprehensive software test cases using the Google Gemini AI API (`google-genai`). It takes in a Python source file or a function description as input, parses the logic, and uses advanced Generative AI to design edge cases, invalid path testing, and standard happy path logic natively outputting in the `pytest` framework.

## Features
- **Generative Testing:** Converts Python function code or string descriptions into ready-to-use testing blocks.
- **Comprehensive Coverage:** Instructs the AI to focus on expected behavior, boundary values, extreme cases, and invalid inputs containing appropriate exception asserts (`pytest.raises`).
- **Free API Tier Usage:** Originally scaled with OpenAI, this tool now defaults to Google's fast & free `gemini-2.5-flash` engine using the native Google GenAI SDK.
- **CLI Native:** Clean Command-Line Interface makes batch-processing possible.

## Quickstart

### 1. Installation
Install the project dependencies, primarily the newest Google GenAI module and `pytest`:
```bash
pip install -r requirements.txt
```

### 2. Configure Credentials
Grab a free API key from [Google AI Studio](https://aistudio.google.com/) and register it as an environment variable in your terminal:

**Windows PowerShell:**
```powershell
$env:GEMINI_API_KEY="your-api-key"
```
**Mac / Linux bash:**
```bash
export GEMINI_API_KEY="your-api-key"
```

### 3. Usage

Process an existing local file (`example_math.py`) and dump generated tests into `test_generated.py`:
```bash
python ai_test_generator.py --file example_math.py --output test_generated.py
```

Process a function logically based on raw text description:
```bash
python ai_test_generator.py --description "def fibonacci(n: int) -> int. Returns fib sequence element. Raise ValueError if n < 0" --output test_fibonacci.py
```

Run your new test suite:
```bash
python -m pytest test_generated.py -v
```
