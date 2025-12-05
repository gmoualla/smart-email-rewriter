# 📧 Smart Email Rewriter (Gemini 2.0)

A simple AI-powered tool that rewrites emails into different tones and styles using Google's Gemini 2.0 API.

## 🚀 Features
- Rewrite emails into **Professional**, **Friendly**, or **Concise** tones
- Iterative refinement with custom feedback
- Lightweight CLI interface
- Powered by Gemini 2.0 Flash (experimental)

## 🧰 Tech Stack
- Python 3.9+
- Google Gemini 2.0 API
- `google-genai` Python SDK

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/email-rewriter-gemini.git
cd email-rewriter-gemini
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Your Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey), then set it:

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**macOS/Linux:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

## ▶️ Usage

Run the email rewriter:
```bash
python email_rewriter.py
```

The tool will:
1. Ask you to paste your email text
2. Ask you to choose a style (Professional/Friendly/Concise)
3. Rewrite your email using Gemini 2.0
4. Allow you to refine the output with custom feedback

### Example Session
```
Smart Email Rewriter (Gemini 2.0 Version)
Paste the email you want to rewrite:

Hi, can u send me the report asap?

Choose style: 1) Professional 2) Friendly 3) Concise
Enter 1,2,3: 1

----- Rewritten Email -----
Subject: Request for Report

Dear [Recipient Name],

I am writing to request the report at your earliest convenience...
---------------------------
Refine? (y/n): n
```

## 📝 Sample Emails

Check the `examples/sample_email.txt` file for 10 sample emails you can use to test the tool.

## 🔧 Troubleshooting

### "ImportError: cannot import name 'genai'"
Make sure you installed the correct package:
```bash
pip install google-genai
```

### "API key not configured"
Verify your API key is set:
```bash
# Windows PowerShell
echo $env:GEMINI_API_KEY

# macOS/Linux
echo $GEMINI_API_KEY
```


## 📄 License

MIT License - feel free to use and modify!

