from flask import Flask, request, jsonify
from deepfake_detection import classify_image

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_deepfake():
    if 'image_url' not in request.json:
        return jsonify({"error": "No image URL provided"}), 400

    image_url = request.json['image_url']
    results = classify_image(image_url)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
