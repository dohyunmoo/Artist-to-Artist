import base64
import requests

def encode_image(url):
    image_response = requests.get(url)
    image_data = image_response.content

    encoded = base64.b64encode(image_data).decode("utf-8")

    return encoded
