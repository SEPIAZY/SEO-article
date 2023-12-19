from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return render_template('./index.html')
# image host
@app.route('/img/<filename>')
def send_img(filename):
    return send_from_directory('./static/img', filename)

if __name__ == '__main__':
    app.run(debug=True)
