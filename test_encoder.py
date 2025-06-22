# test_encoder.py
import base64
from facial_encoder import read_image_from_base64, encode_faces

# Sample base64 image (use a real image in practice)
def test_encoding():
    with open("test_image.jpg", "rb") as image_file:
        b64 = base64.b64encode(image_file.read()).decode('utf-8')

    image = read_image_from_base64(b64)
    encodings, locations = encode_faces(image)

    assert len(encodings) > 0, "No faces encoded"
    print("✅ Test passed: Faces encoded successfully")
