# TinyLlama Local LLM Script

A simple Python script that demonstrates calling a local TinyLlama model using Ollama.

## 🚀 Quick Setup

### Step 1: Install Ollama
- Download from: https://ollama.ai
- Install for your operating system

### Step 2: Download TinyLlama Model
```bash
ollama pull tinyllama
```

### Step 3: Set Up Python Environment

#### Option A: Simple Installation (No Virtual Environment)
```bash
pip install ollama
python run_tinyllama.py
```

#### Option B: With Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install required package
pip install ollama

# Run the script
python run_tinyllama.py
```

## 📁 Files

- `run_tinyllama.py` - Main script that sends a prompt to TinyLlama and prints the response

## 🔧 Troubleshooting

### "Error: listen tcp 127.0.0.1:11434: bind: Only one usage..."
This means Ollama is already running. **This is good!** Just run your Python script directly:
```bash
python run_tinyllama.py
```

### "Connection refused" or "Ollama not found"
Make sure Ollama service is running:
```bash
# Check if models are available (tests connection)
ollama list

# If nothing shows up, start Ollama manually
ollama serve
```

### "Model not found"
Download the TinyLlama model:
```bash
ollama pull tinyllama
```

## 📋 What the Script Does

1. Sets a prompt: "Hello, tinyllama! Tell me a fun fact about space."
2. Calls the local TinyLlama model via Ollama
3. Prints both the prompt and AI response

## 🎯 Expected Output

```
=== Prompt ===
Hello, tinyllama! Tell me a fun fact about space.

=== Response ===
[TinyLlama's response about space facts]
```

## 📚 Next Steps

- Try changing the prompt in the script
- Experiment with different models: `ollama pull mistral`
- Add interactive input to make it a chat bot

## 🆘 Common Issues

| Problem | Solution |
|---------|----------|
| `pip install ollama` fails | Make sure you're in the activated virtual environment |
| Script can't connect to Ollama | Run `ollama list` to test connection |
| TinyLlama responses are slow | Normal for first run, faster afterwards |
| Virtual environment commands don't work | Make sure you activated it first |

## 💡 Pro Tips

- Keep your virtual environment activated while working
- TinyLlama is small but surprisingly capable
- First run might be slower as the model loads into memory
- You can run multiple Python scripts while Ollama runs in the background