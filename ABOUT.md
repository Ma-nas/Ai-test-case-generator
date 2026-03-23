# About the AI Test Case Generator

## The Problem
Developing robust, comprehensive test suites is critically important for software stability, yet doing so manually is notoriously time-consuming for development teams. Ensuring edge cases, strange boundary numbers, negative parameters, and exception handling are accurately verified can be easily overlooked during fast development cycles.

## The Solution
The **AI Test Case Generator** bridges the gap in the development pipeline by leveraging Large Language Models to read source code or function descriptions natively and systematically generate tests that map against rigorous QA testing philosophies.

By pointing this utility at a standard source file containing loose functions or classes, the developer instantly skips the initial boilerplate of `pytest` structures, mock configurations, and simple boundary checking.

## How it Works
1. **Input Layer:** It reads standard raw Python code (`.py` files) or accepts direct string commands. It avoids building massive Abstract Syntax Trees (ASTs) by forwarding logical units contextually directly into the neural network prompt.
2. **LLM Engine:** Through a securely integrated payload, the source code along with a tightly constraint System Prompt is sent to the Google GenAI Engine (`gemini-2.5-flash`), explicitly commanding the model to isolate only Python code blocks representing unit tests. The prompt forces strict PEP-8 guidelines and demands exhaustive `pytest.raises` verifications to handle bad data types without throwing stack traces.
3. **Execution Layer:** It sanitizes any extra markdown the LLM might hallucinate back into the response stream before pushing raw python test frameworks directly into output module files like `test_generated.py`.

## Built With
- **Python**: Used for parsing inputs and communicating heavily with External APIs.
- **Google GenAI SDK**: Powering the advanced deep machine learning capabilities representing the core code generation functionality.
- **Pytest**: The globally recognized, lightweight standard for verifying assertions and functional testing in Python infrastructures.
