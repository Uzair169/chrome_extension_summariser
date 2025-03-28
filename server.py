from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_API = "http://localhost:11434/api/generate"  # Adjust if needed

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        response = requests.post(OLLAMA_API, json={"model": "llama3.2:1b", "prompt": f"Summarize this: {text}", "stream": False})
        
        if response.status_code == 200:
            response_json = response.json()
            summary = response_json.get("response", "")
            print(summary)
            return jsonify({"summary": summary})
        else:
            return jsonify({"error": "Ollama request failed", "status_code": response.status_code}), 500
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Request to Ollama API failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
