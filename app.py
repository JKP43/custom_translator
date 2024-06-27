from flask import Flask, request, jsonify, render_template
from translator import translate_text

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    from_language = data.get('from_language')
    to_language = data.get('to_language')
    translated_text = translate_text(text, from_language, to_language)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
