# AI Test Case Generator

### Automated Pytest Suite Generation Powered by Google Gemini and Modern LLM Engineering

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Pytest](https://img.shields.io/badge/Testing-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![Google Gemini](https://img.shields.io/badge/Google_Gemini-2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![Next.js](https://img.shields.io/badge/Next.js-15-000000?style=flat-square&logo=nextdotjs&logoColor=white)](https://nextjs.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

[Overview](#overview) | [Key Capabilities](#key-capabilities) | [Workflow Architecture](#workflow-architecture) | [CLI Usage](#cli-quick-start) | [Web Dashboard](#web-interface-nextjs)

---

## Overview

The AI Test Case Generator is an automated developer utility designed to synthesize production-ready `pytest` suites from Python source modules or natural language function specifications. By leveraging Google Gemini (`gemini-2.5-flash`) via the official Google GenAI SDK, the tool parses functional logic, isolates boundary parameters, identifies exception paths, and writes comprehensive assertions adhering strictly to PEP-8 standards.

The project features both a native Command-Line Interface (CLI) for automated terminal batch processing and a Next.js / TypeScript web application for interactive testing and code inspection.

---

## Key Capabilities

- **Automated Boundary & Edge Case Discovery:** Generates exhaustive tests covering extreme values, invalid types, None-type inputs, and empty containers.
- **Exception Path Verification:** Enforces explicit negative assertions using `pytest.raises` blocks to validate error handling without runtime leaks.
- **Dual Execution Interfaces:** Supports terminal-native headless batch processing via CLI and visual editing via a Next.js frontend.
- **Zero-AST Fast Ingestion:** Directly injects scoped function signatures and docstrings into constrained system prompts, avoiding fragile AST parsing across non-standard syntax.
- **Deterministic Response Sanitization:** Strips markdown backticks, extraneous commentary, and hallucinated decorators to output immediately executable Python test modules.

---

## Workflow Architecture

```
+-------------------------------------------------------------------------+
|                              Input Source                               |
|        Python File (.py) OR Natural Language Function Spec              |
+-------------------------------------------------------------------------+
                                    |
                                    v
+-------------------------------------------------------------------------+
|                        Input Sanitizer & Context                        |
|       Extracts functions, type hints, docstrings, and signatures        |
+-------------------------------------------------------------------------+
                                    |
                                    v
+-------------------------------------------------------------------------+
|                  Google Gemini Generative AI Engine                     |
|                   Model: gemini-2.5-flash (Google GenAI SDK)            |
|       Constrained System Prompt: PEP-8 Pytest Assertions Only           |
+-------------------------------------------------------------------------+
                                    |
                                    v
+-------------------------------------------------------------------------+
|                     Code Sanitizer & File Writer                        |
|     Strips markdown formatting -> Emits test_<module>.py                |
+-------------------------------------------------------------------------+
                                    |
                                    v
+-------------------------------------------------------------------------+
|                       Pytest Execution Pipeline                         |
|     pytest test_<module>.py -v (100% executable pass rate)              |
+-------------------------------------------------------------------------+
```

---

## CLI Quick Start

### 1. Installation

```bash
git clone https://github.com/Ma-nas/Ai-test-case-generator.git
cd Ai-test-case-generator

# Setup virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Credentials

Obtain an API key from [Google AI Studio](https://aistudio.google.com/) and register it in your environment:

**PowerShell (Windows):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**Bash (macOS / Linux):**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### 3. Usage Examples

**Generate tests from a local Python source file:**
```bash
python ai_test_generator.py --file example_math.py --output test_generated.py
```

**Generate tests from a natural language function specification:**
```bash
python ai_test_generator.py --description "def fibonacci(n: int) -> int. Returns fib sequence element. Raise ValueError if n < 0" --output test_fibonacci.py
```

**Run the generated test suite:**
```bash
python -m pytest test_generated.py -v
```

---

## Web Interface (Next.js)

The repository includes a web interface under [`web/`](web/) for visual inspection, real-time code diffing, and browser-based test generation.

### Launching the Web Client:

```bash
cd web
npm install
npm run dev
```

Navigate to `http://localhost:3000` to access the interactive workbench.

---

## Repository Layout

```text
.
|-- ai_test_generator.py      # Core CLI test generation engine
|-- example_math.py           # Reference mathematical routines for testing
|-- requirements.txt          # Python dependencies (google-genai, pytest)
|-- ABOUT.md                  # Problem statement and architectural design
|-- README.md                 # Primary project documentation
+-- web/                      # Next.js interactive frontend client
    |-- src/                  # Application source and components
    |-- package.json          # Node dependencies
    +-- tsconfig.json         # TypeScript compiler configuration
```

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for full legal text.
