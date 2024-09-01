from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes and origins

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()

    if 'image_data' not in data:
        return jsonify({'error': 'No image data provided'}), 400

    image_data = data['image_data']
    # Process the image data and make predictions here

    # Simulate response
    response = {
        'label': 'Deepfake' if random.random() < 0.5 else 'Not a Deepfake'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
