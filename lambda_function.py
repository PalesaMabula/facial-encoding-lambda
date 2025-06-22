# lambda_function.py
import json
import base64
from facial_encoder import read_image_from_base64, read_image_from_url, encode_faces

def handler(event, context):
    try:
        body = json.loads(event["body"])

        if "image_base64" in body:
            image = read_image_from_base64(body["image_base64"])
        elif "image_url" in body:
            image = read_image_from_url(body["image_url"])
        else:
            return {"statusCode": 400, "body": json.dumps({"error": "No valid image source provided."})}

        encodings, locations = encode_faces(image)
        encoding_list = [enc.tolist() for enc in encodings]

        return {
            "statusCode": 200,
            "body": json.dumps({
                "encodings": encoding_list,
                "face_count": len(encodings)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
