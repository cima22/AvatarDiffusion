from flask import Flask, Response, send_from_directory, request
from PIL import Image
import io
from sdmigeapi import client

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('../public', 'index.html')


@app.route('/ping')
def ping():
    print('ping')
    return 'Pong'


@app.route('/image')
def image():
    prompt = request.args.get('prompt')
    print(prompt)
    images = client.generate_images(prompt, n_imgs=1)
    pil_image = images[0]
    img_byte_array = io.BytesIO()
    pil_image.save(img_byte_array, format='JPEG')
    img_byte_array = img_byte_array.getvalue()
    headers = {'Content-Type': 'image/jpeg'}
    return Response(img_byte_array, headers=headers)


if __name__ == '__main__':
    app.run(debug=True)
