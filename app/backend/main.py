from PIL import Image
from flask import Flask, Response, send_from_directory, request
import io
from sdmigeapi import client
import json

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('../public', 'index.html')


@app.route('/api/image')
def image():
    # pil_image = Image.open('../public/puppy.jpg')

    prompt = request.args.get('prompt').lower()
    prompt = prompt[:-1]
    negative = request.args.get('negative').lower()
    print(prompt)
    print(negative)
    try:
        images = client.generate_images(prompt, negative=negative, n_imgs=1)
    except TimeoutError:
        return Response('Stable Diffusion model timed out',
                        status=503,
                        headers={'Content-Type': 'text/plain'})
    pil_image = images[0]
    img_byte_array = io.BytesIO()
    pil_image.save(img_byte_array, format='JPEG')
    img_byte_array = img_byte_array.getvalue()
    headers = {'Content-Type': 'image/jpeg'}
    return Response(img_byte_array, headers=headers)


@app.route('/api/<string:filename>')
def files(filename):
    return send_from_directory('../public/json', filename)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
