# test_lambda.py
import json
from lambda_function import handler

# Replace this with a real base64 image string for actual test
fake_event = {
    "body": json.dumps({
        "image_url": "https://raw.githubusercontent.com/ageitgey/face_recognition/master/examples/obama.jpg"
    })
}

result = handler(fake_event, None)
print("Lambda Output:", result)
