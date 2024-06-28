from flask import Flask, request, jsonify, render_template, send_file
from translator import translate_text
from io import BytesIO

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
        with open('/tmp/translated_text.txt', 'w', encoding='utf-8') as f:
            f.write(translated_text)
        return send_file('translated_text.txt', as_attachment=True)
    else:
        return "No file to download"

# Download using memory
# @app.route('/download', methods=['POST'])
# def download():
#     try:
#         translated_text = request.form['translatedText']
#         buffer = BytesIO()
#         buffer.write(translated_text.encode('utf-8'))
#         buffer.seek(0)
#         return send_file(
#             buffer,
#             as_attachment=True,
#             download_name='translated_text.txt',
#             mimetype='text/plain'
#         )
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
