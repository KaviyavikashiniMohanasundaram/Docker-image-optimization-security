from flask import Flask, request, send_file, render_template, send_from_directory
from PIL import Image
import io, os

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/optimize', methods=['POST'])
def optimize_image():
    file = request.files['image']
    img = Image.open(file.stream)

    # Resize & compress
    img = img.resize((800, int(800 * img.height / img.width)))
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
