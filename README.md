# Webpage Summarizer - Chrome Extension

## 📌 Overview
Webpage Summarizer is a Chrome extension that extracts and summarizes the content of any webpage using a local AI-based summarization API. With a single click, it fetches the webpage text, sends it to the API, and displays a concise summary.

## ✨ Features
- Extracts text from the active webpage
- Sends the extracted text to a local API for summarization
- Displays a formatted summary inside the extension popup
- Allows users to copy the summary with a single click
- Simple and lightweight UI

## Requirements:
   Install requirements with the following:
   ```sh
  pip install Ollama Flask
  ```

## 🛠 Installation
1. **Download or Clone** this repository:
   ```sh
   git clone https://github.com/your-username/webpage-summarizer.git
   ```
2. **Go to Chrome Extensions Page**
   - Open Chrome and type `chrome://extensions/` in the address bar.
3. **Enable Developer Mode**
   - Toggle the "Developer mode" switch (top-right corner).
4. **Load Unpacked Extension**
   - Click on "Load unpacked."
   - Select the folder where you cloned/downloaded this extension.
5. **Pin the Extension** (Optional)
   - Click on the puzzle icon 🧩 in the Chrome toolbar.
   - Pin "Webpage Summarizer" for easy access.

## How To Run
1. run Ollama:
   `run Ollama`
3. Pull the necessary model.
4. Run the API server:
   `python server.py`
5. Refer to the <b>Usage</b> tab for further instructions.

## 🚀 Usage
1. Open any webpage you want to summarize.
2. Click on the Webpage Summarizer extension icon.
3. Click the **"Summarize"** button.
4. Wait for the summary to be generated.
5. Click **"📋 Copy Summary"** to copy it to your clipboard.

## 🛑 Troubleshooting
- **Extension not working?** Make sure the API server is running on `http://localhost:5000/summarize`.
- **Summary not fetching?** Make sure Ollama is running at `http://localhost:11434`.
- **Summary not displaying?** Try refreshing the extension or checking the console for errors (`Ctrl+Shift+I` → Console).
- **Permission issues?** Ensure Chrome allows the extension to access webpages.

## 💡 Contributing
Feel free to fork this repo and submit pull requests with improvements!
