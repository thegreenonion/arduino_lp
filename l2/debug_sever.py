import gzip
import random

from flask import request
from flask import Flask, make_response

app = Flask(__name__,
            static_url_path='/',
            static_folder='data/',
            template_folder='')


def create_compress_files(file):
    with open(file, 'r') as f:
        file_content = f.read()
    content = gzip.compress(file_content.encode('utf8'))
    with open(file + ".gz", "wb") as f:
        f.write(content)


@app.route('/js/core/<param>')
def core_js(param):
    response = create_js_response(param, path="data/js/core/")
    return response

@app.route('/js/jquery/<param>')
def jquery_js(param):
    response = create_js_response(param, path="data/js/jquery/")
    return response

@app.route('/css/jquery/<param>')
def jquery_css(param):
    response = create_js_response(param, path="data/css/jquery/")
    return response


@app.route('/js/lang/<param>')
def lang_js(param):
    response = create_js_response(param, path="data/js/lang/")
    return response


def create_js_response(param, path):
    with open(f"{path}{param}.gz", 'rb') as f:
        content = f.read()
    response = make_response(content)
    response.headers['Content-length'] = len(content)
    response.headers['Content-Encoding'] = 'gzip'
    return response


# create_compress_files("data/css/jquery/jquery.mobile.min.css")
# create_compress_files("data/js/jquery/jquery.mobile-1.4.5.min.js")

@app.route('/pin_mode', methods=['GET'])
def pin_mode():
    pin = request.args.get('pin')
    mode = request.args.get('mode')
    return f'pin_mode({pin},{mode});', 200

@app.route('/digital_write', methods=['GET'])
def digital_write():
    pin = request.args.get('pin')
    value = request.args.get('value')
    return f'digital_wirte({pin},{value});', 200

@app.route('/analog_write', methods=['GET'])
def analog_write():
    pin = request.args.get('pin')
    value = request.args.get('value')
    return f'analog_write({pin},{value});', 200

@app.route('/digital_read', methods=['GET'])
def digital_read():
    pin = request.args.get('pin')
    return f'digital_read({pin});', 200


@app.route('/right')
def right():
    return 'right', 200


@app.route('/left')
def left():
    return 'left', 200


@app.route('/forward')
def forward():
    return 'forward', 200


@app.route('/backward')
def backward():
    return 'backward', 200


@app.route('/stop')
def stop():
    return 'backward', 200


@app.route('/obstacle')
def obstacle():
    return f"{random.random()}", 200


if __name__ == '__main__':
    print("http://127.0.0.1:5000/index.html")
    app.run("0.0.0.0")
