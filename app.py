from flask import Flask, request, jsonify, render_template, send_file
from translator import translate_text
import requests
import os

app = Flask(__name__)

translated_text = None

@app.route('/')
def index():
    return render_template('index.html')

# Translate using POST
@app.route('/translate', methods=['POST'])
def translate():
    global translated_text
    data = request.get_json()
    text = data.get('text')
    from_language = data.get('from_language')
    to_language = data.get('to_language')
    translated_text = translate_text(text, from_language, to_language)

    return jsonify({'translated_text': translated_text})

# Download the translated text
@app.route('/download')
def download():
    global translated_text
    if translated_text:
        # Write the translated text to a file with utf-8 encoding
        with open('translated_text.txt', 'w', encoding='utf-8') as f:
            f.write(translated_text)
        return send_file('translated_text.txt', as_attachment=True)
    else:
        return "No file to download"


if __name__ == '__main__':
    app.run(debug=True)
