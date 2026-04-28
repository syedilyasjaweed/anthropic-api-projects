cat > ~/Developer/anthopic-api-course/README.md << 'EOF'
# Anthropic API Projects

Hands-on Python projects built while working through the Anthropic API — covering everything from basic API calls to streaming, structured output, and multi-turn chatbots using Claude.

---

## What's in this repo

| File | What it does |
|------|-------------|
| `lesson1.py` | First API call — sends a prompt and prints Claude's response |
| `lesson2.py` | Accepts user input from the terminal at runtime |
| `lesson3.py` | Multi-turn chatbot with full conversation history |
| `lesson4.py` | Helper functions — clean reusable wrappers around the API |
| `lesson5.py` | System prompts — persona control using a grumpy chef character |
| `lesson6.py` | Specialist chatbot — "Mike the Mechanic", a domain-scoped assistant |
| `lesson7.py` | Temperature control — experimenting with response creativity |
| `lesson8.py` | Streaming — printing Claude's response token by token as it arrives |
| `lesson9.py` | Structured output — JSON extraction using prefilling and stop sequences |
| `001_prompting.ipynb` | Jupyter notebook exploring prompting techniques |
| `001_tools.ipynb` | Jupyter notebook on tool use with the API |
| `dataset.json` | Dataset used for the evaluation pipeline in Lesson 10 |

---

## Key concepts covered

- Authenticating securely with the Anthropic API using `.env` and `python-dotenv`
- Understanding that Claude has no memory between API calls — the `messages` list IS the memory
- Building and managing conversation history manually
- Writing reusable helper functions for cleaner API interactions
- Controlling model behavior with system prompts and temperature
- Streaming responses for real-time output
- Extracting structured JSON using prefilling and stop sequences
- Running a basic dataset evaluation pipeline

---

## Setup

**Requirements:** Python 3.8+, an Anthropic API key

```bash
git clone https://github.com/syedilyasjaweed/anthropic-api-projects.git
cd anthropic-api-projects
pip install anthropic python-dotenv
```

Create a `.env` file in the root directory: