from flask import Flask, render_template, send_from_directory, request
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

content = {
    'en': {
        'greeting': 'Hello!',
        'message': 'Welcome to our website.'
    },
    'th': {
        'greeting': 'สวัสดี!',
        'message': 'ยินดีต้อนรับสู่เว็บไซต์ของเรา'
    }
}

@app.route('/')
def index():
    lang = request.args.get('lang', 'en')  
    lang_content = content.get(lang, content['en']) 
    return render_template('index.html', lang_content=lang_content)

@app.route('/img/<filename>')
def send_img(filename):
    return send_from_directory('./static/img', filename)

if __name__ == '__main__':
    app.run(debug=True)
