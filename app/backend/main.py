from flask import Flask, send_from_directory
# from PIL import Image
# import io

app = Flask(__name__)


@app.route('/')
def index():
    return send_from_directory('../public', 'index.html')


@app.route('/ping')
def ping():
    print('ping')
    return 'Pong'


# @app.route('/image')
# def get_image():
#     # Create a PIL image object (you might have this already)
#     pil_image = Image.open(
#         'path_to_your_image.jpg')  # Replace 'path_to_your_image.jpg' with the actual path to your image
#
#     # Convert PIL image to bytes
#     img_byte_array = io.BytesIO()
#     pil_image.save(img_byte_array, format='JPEG')
#     img_byte_array = img_byte_array.getvalue()
#
#     # Set the appropriate content type
#     headers = {'Content-Type': 'image/jpeg'}
#
#     # Return the image bytes as a response
#     return Response(img_byte_array, headers=headers)


if __name__ == '__main__':
    app.run(debug=True)
