from flask import Flask, Response, send_from_directory, request
import io
from sdmigeapi import client

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('../public', 'index.html')


@app.route('/api/image')
def image():
    prompt = request.args.get('prompt')
    print(prompt)

    return Response('Stable Diffusion model timed out',
                    status=503,
                    headers={'Content-Type': 'text/plain'})

    try:
        images = client.generate_images(prompt, n_imgs=1)
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
    return send_from_directory('../public', filename)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
