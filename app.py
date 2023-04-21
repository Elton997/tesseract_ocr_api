import io,re,cv2,json
import pytesseract
from pytesseract import Output
from PIL import Image
import numpy as np
from flask import Flask, request ,jsonify

# Initialize Flask app
app = Flask(__name__)

# API endpoint to extract key-value pairs from invoice image
@app.route('/extract-invoice', methods=['POST'])
def extract_invoice():
    # Get image from request payload
    if 'image' not in request.files:
        return jsonify({'success': False, 'message': 'Image not found in request payload.'})

    # Read image from request payload
    image_file = request.files['image']
    image_bytes = image_file.read()
    image = np.array(Image.open(io.BytesIO(image_bytes)))

    # Extract text from image using Tesseract OCR
    text = pytesseract.image_to_string(image)
    key_value_pairs=extract_key_value_pairs(text)
    # Return key-value pairs as JSON response
    return jsonify({'success': True, 'key_value_pairs': key_value_pairs})

def extract_key_value_pairs(text):
    """
    Extracts key-value pairs from given text using regex matching.
    """
    key_value_pairs = {}

    # loop through each line of text
    for line in text.split('\n'):
        # split line based on colon
        line = line.split(':')
        if len(line)>1:
            # extract key and value
            key = line[0].strip()
            value = line[len(line)-1].strip()
            key=re.sub('[^a-zA-Z0-9 \n\.]', '', key)
            value=re.sub('[^a-zA-Z0-9 \n\.]', '', value)
            # add to dictionary
            key_value_pairs[key] = value

    return key_value_pairs

# Start Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
