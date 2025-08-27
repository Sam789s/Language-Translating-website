from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template(
        "index.html", 
        translated_text=None, 
        detected_lang=None, 
        detection_code=None, 
        languages=LANGUAGES
    )

@app.route('/trans', methods=['POST'])
def translate():
    text = request.form['text']
    lang = request.form['lang']
    
    # Detect language
    detection = translator.detect(text)
    detected_lang = LANGUAGES.get(detection.lang, "Unknown")
    detection_code = detection.lang
    
    # Translate
    translated = translator.translate(text, dest=lang)
    
    return render_template(
        "index.html", 
        translated_text=translated.text, 
        detected_lang=detected_lang, 
        detection_code=detection_code,
        languages=LANGUAGES
    )

if __name__ == "__main__":
    app.run(debug=True)
