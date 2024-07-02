from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

from pprint import pprint

# loading client variables from .env file
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    return json_result["access_token"]

def search_artist_id(token, artist_name):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    headers = authorization(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)

    artist_id = json_result["artists"]["items"][0]["id"]
    search_related_artist(token, artist_id)


def search_related_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = authorization(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)

    for artist in json_result["artists"]:
        print(artist["name"], artist["genres"], artist["id"])

def authorization(token):
    return {"Authorization": f"Bearer {token}"}

def main():
    token = get_token()
    search_artist_id(token, "newjeans")

if __name__ == "__main__":
    main()