# Facial Encoding Lambda

This project uses Python's `face_recognition` library to detect and encode faces from images. It is designed for deployment on AWS Lambda and supports both base64 and URL-based image inputs.

## 🧠 Features

- Face detection and encoding
- AWS Lambda handler for API integration
- Support for image input via base64 or URL
- Simple test cases included

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run locally:

```bash
python test_lambda.py
```

To test encoder manually:

```bash
python test_encoder.py
```

## 🖼 Example Request

Send a POST request to Lambda with:

```json
{
  "image_url": "https://raw.githubusercontent.com/ageitgey/face_recognition/master/examples/obama.jpg"
}
```

## 📁 Project Structure

```
facial-encoding-lambda/
├── facial_encoder.py
├── lambda_function.py
├── test_encoder.py
├── test_lambda.py
├── requirements.txt
└── README.md
```

## ✨ Author

Palesa Mabula
