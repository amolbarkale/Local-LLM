#!/usr/bin/env python3
"""
run_tinyllama.py

A minimal example that:
 1. sets a prompt string
 2. calls the local Ollama‐served tinyllama model
 3. prints prompt and response

Requirements:
  - Ollama must be installed and running
  - The tinyllama model must already be pulled (ollama pull tinyllama)
  - Python 'ollama' package installed (pip install ollama)
"""

import sys
import ollama  # ✅ Correct import - just 'ollama'

def main():
    # 1. Define your prompt:
    prompt_text = "Hello, tinyllama! Tell me a fun fact about space."

    try:
        # 2. Check if Ollama is running (optional but good practice)
        ollama.list()  # This will fail if Ollama isn't running
        
        # 3. Generate a response
        # The 'generate' call will block until the model replies.
        response = ollama.generate(
            model="tinyllama",
            prompt=prompt_text,
            # Optional parameters (if you want to customize):
            # options={
            #     "temperature": 0.7,
            #     "top_p": 0.9,
            #     "max_tokens": 64
            # }
        )
        
    except ollama.ResponseError as e:
        print(f"Ollama API error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error when calling Ollama: {e}", file=sys.stderr)
        print("Make sure Ollama is running: 'ollama serve'", file=sys.stderr)
        sys.exit(1)

    # 4. Print prompt and response
    print("=== Prompt ===")
    print(prompt_text, "\n")
    print("=== Response ===")
    # ✅ Correct way to access the response
    print(response['response'])

if __name__ == "__main__":
    main()