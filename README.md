# Invoice OCR API
This is a Python Flask API that extracts key-value pairs from invoice images using the Tesseract OCR library.

## Installation
```
git clone https://github.com/Elton997/tesseract_ocr_api.git
```

## Usage
1. Create Virtual Environment in Python to run the Flask API:

(For Windows Users)
```
python -m venv .venv
.venv\Scripts\activate.bat 
```

(For MAC or Linux Users)
```
python -m venv .venv
source venv/bin/activate
```

2. Install the required Python libraries:
```
pip install -r requirements.txt
```

3. To start the API, run the following command:
```
python app.py
```
This will start the API server at **http://localhost:8080**.

4. Send a POST request to the /extract-invoice endpoint with an image of an invoice in the request payload. The image should be in JPEG or PNG format.

## Postman Colletion:
I've already added the Postman collection(**tesseract-ocr-extract-invoce.postman_collection.json**) for testing purpose, you can use the same. Just change the images.

## License
This project is licensed under the terms of the MIT license.
