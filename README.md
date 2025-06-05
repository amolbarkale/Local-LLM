# 🎭 AI Rephraser - Local LLM Text Transformation

A powerful web application that transforms your text into different writing styles using **100% local AI inference** with Llama 3.2 3B model.

## 🚀 App Type Selected: **Rephraser**

Transform any text into 6 different writing styles:
- 👔 **Professional** - Business-appropriate, formal tone
- 😊 **Casual** - Friendly, conversational style  
- 🎓 **Academic** - Scholarly, formal writing
- 🎨 **Creative** - Engaging, expressive language
- ⚡ **Concise** - Direct, brief communication
- 😄 **Humorous** - Witty, entertaining tone

## ✨ Features

- **100% Local Processing** - No data sent to external APIs
- **Real-time Style Transformation** - Choose from 6 writing styles
- **Adjustable Creativity** - Temperature control (0.1 - 1.0)
- **Modern UI** - Responsive, professional interface
- **Activity Logging** - Track all operations with timestamps
- **Export Functionality** - Save logs and outputs
- **Connection Monitoring** - Real-time Ollama status
- **Keyboard Shortcuts** - Ctrl+Enter to rephrase

## 🔧 Model Used

- **Primary Model**: `llama3.2:3b`
- **Parameters**: 3 billion parameters
- **Size**: ~2.0 GB
- **Provider**: Meta AI (running locally via Ollama)

## 📋 Prerequisites

1. **Ollama** installed and running
2. **Llama 3.2 3B** model downloaded
3. Modern web browser (Chrome, Firefox, Safari, Edge)
4. Minimum 4GB RAM (8GB recommended)

## 🛠️ Setup Instructions

### Step 1: Install Ollama

**Windows/Mac:**
```bash
# Download from: https://ollama.ai/download
# Or use package managers:

# macOS (Homebrew)
brew install ollama

# Windows (via installer)
# Download .exe from official site
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

### Step 2: Install Llama 3.2 3B Model

```bash
# Pull the model (this will download ~2GB)
ollama pull llama3.2:3b

# Verify installation
ollama list
```

### Step 3: Start Ollama Server

```bash
# Start Ollama (usually starts automatically)
ollama serve

# Test the model
ollama run llama3.2:3b "Hello, how are you?"
```

### Step 4: Run the Application

#### Option A: Simple File Method
1. Save the HTML file as `ai-rephraser.html`
2. Open in your web browser
3. Start rephrasing!

#### Option B: Local Server Method (Recommended)
```bash
# If you have Python installed
python -m http.server 8000

# If you have Node.js installed
npx serve .

# Then open: http://localhost:8000
```

## 🎯 How to Use

1. **Check Connection**: Ensure the status shows "Connected to Ollama"
2. **Enter Text**: Type or paste text in the input area
3. **Choose Style**: Select from 6 available writing styles
4. **Adjust Creativity**: Use the temperature slider (0.1 = focused, 1.0 = creative)
5. **Rephrase**: Click "🚀 Rephrase Text" or press Ctrl+Enter
6. **Copy/Export**: Use the control buttons to save your results

## 📊 Technical Details

### API Endpoints Used
- `GET http://localhost:11434/api/tags` - Check Ollama status
- `POST http://localhost:11434/api/generate` - Generate rephrased text

### Model Parameters
```json
{
  "model": "llama3.2:3b",
  "temperature": 0.1-1.0,
  "top_p": 0.9,
  "top_k": 40,
  "repeat_penalty": 1.1,
  "num_predict": 500
}
```

### Performance Expectations
- **Response Time**: 2-10 seconds (depends on hardware)
- **Memory Usage**: 2-4 GB RAM
- **CPU Usage**: High during generation, idle when waiting

## 🔍 Troubleshooting

### Common Issues

**❌ "Ollama not connected"**
```bash
# Check if Ollama is running
ollama list

# Restart Ollama
ollama serve

# Check port 11434 is available
curl http://localhost:11434/api/tags
```

**❌ "Model not found"**
```bash
# Reinstall the model
ollama pull llama3.2:3b

# List available models
ollama list
```

**❌ "Slow response times"**
- Ensure sufficient RAM (8GB+ recommended)
- Close other heavy applications
- Consider using a smaller model if needed

**❌ "Browser compatibility issues"**
- Use modern browsers (Chrome 80+, Firefox 75+, Safari 13+)
- Enable JavaScript
- Check console for errors (F12)

## 📝 Output Logging

The application automatically logs all activities:
- **Frontend Logs**: Displayed in the Activity Logs section
- **Local Storage**: Saved in browser's localStorage
- **Export Options**: Download logs as `.txt` files

### Log Format
```
[HH:MM:SS] Event description
[14:30:25] Style changed to: professional
[14:30:30] Starting rephrasing: professional style, temperature: 0.7
[14:30:35] Successfully rephrased 45 characters -> 52 characters
```

## 🎨 Customization

### Adding New Styles
Edit the `getStylePrompt()` function in the HTML file:

```javascript
const prompts = {
    // Add your custom style
    technical: "Rewrite this text in technical jargon with industry-specific terms...",
    // ... existing styles
};
```

### Modifying UI
- **Colors**: Edit the CSS variables in the `<style>` section
- **Layout**: Modify the grid system classes
- **Animations**: Adjust transition durations and effects

## 🔒 Privacy & Security

- **100% Local Processing** - No data leaves your machine
- **No External APIs** - All processing via local Ollama
- **No Data Collection** - No analytics or tracking
- **Open Source** - Full code visibility

## 🚧 Known Limitations

- Requires local Ollama installation
- Model responses may vary based on hardware
- Large texts may take longer to process
- Limited to single-language processing (primarily English)

## 🔄 Updates & Maintenance

### Updating the Model
```bash
# Update to latest version
ollama pull llama3.2:3b

# Check for updates
ollama list
```

### Clearing Cache
```bash
# Clear browser cache and localStorage
# Or use the "Clear" button in the app
```

## 📞 Support

For issues and questions:
1. Check the troubleshooting section above
2. Verify Ollama installation: `ollama --version`
3. Test model directly: `ollama run llama3.2:3b "test"`
4. Check browser console for JavaScript errors

## 🏆 Performance Tips

1. **Hardware**: Use SSD storage for faster model loading
2. **Memory**: Allocate 8GB+ RAM for optimal performance
3. **Temperature**: Use lower values (0.1-0.3) for consistent results
4. **Text Length**: Keep input under 1000 characters for faster processing