from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will allow all origins. You can restrict it to specific origins if needed.

@app.route('/detect', methods=['POST'])
def detect():
    # Your deepfake detection logic here
    data = request.get_json()
    image_data = data.get('image_data')
    # Process the image_data and perform detection
    result = {"label": "Deepfake"}  # Example response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
