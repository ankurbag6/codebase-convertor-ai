# codebase-convertor-ai

AI-powered code converter: uses LLMs to port Python code into high-performance C++, then compiles and runs both versions side by side so you can compare correctness and speed across models.

## Features

- Gradio UI to paste Python code and convert it with a model of your choice
- Supports OpenAI, Anthropic, Google Gemini, xAI Grok, Groq, OpenRouter and local Ollama models
- Runs the Python, compiles and runs the generated C++ (`clang++ -O3`), and tracks per-model speedups in a table
- Passes your machine's CPU/OS/compiler info to the model so it can tune the C++ for your hardware

## Requirements

- Python 3.12 (pinned in `.python-version`)
- [uv](https://docs.astral.sh/uv/) (recommended) or `pip`
- A C++ compiler: `clang++` (macOS: `xcode-select --install`)
- Optional: [Ollama](https://ollama.com) for local models

## Setup

```bash
# 1. Create the virtual environment and install dependencies
uv venv --python 3.12
uv pip install -r requirements.txt

#    or, without uv:
#    python3.12 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# 2. Configure API keys
cp .env.example .env
#    then edit .env and fill in the keys you have
```

### Environment variables

| Variable             | Required | Used for                  |
| -------------------- | -------- | ------------------------- |
| `OPENAI_API_KEY`     | Yes      | GPT models                |
| `ANTHROPIC_API_KEY`  | No       | Claude models             |
| `GOOGLE_API_KEY`     | No       | Gemini models             |
| `GROK_API_KEY`       | No       | xAI Grok models           |
| `GROQ_API_KEY`       | No       | Groq-hosted models        |
| `OPENROUTER_API_KEY` | No       | OpenRouter-hosted models  |

`.env` is git-ignored; never commit real keys.

## Usage

```bash
source .venv/bin/activate
python app.py
```

The UI opens in your browser. Pick a model, click **Convert code**, then **Run Python** and **Compile and run C++** to compare output and execution time.

## Project structure

```
app.py            # Gradio app: model clients, prompts, conversion, compile/run
system_info.py    # Collects host CPU/OS/compiler info for the prompt
requirements.txt  # Python dependencies
.env.example      # Template for API keys
```

Generated `main.cpp` and the `main` binary are written to the project folder and are git-ignored.
