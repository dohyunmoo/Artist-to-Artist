from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

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


def search_related_artist(token, artist_name):
    url_search = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    headers = authorization(token)

    result_search = get(url_search, headers=headers)
    json_result_search = json.loads(result_search.content)

    artist_id = json_result_search["artists"]["items"][0]["id"]

    url_related = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = authorization(token)

    result = get(url_related, headers=headers)
    json_result = json.loads(result.content)
    
    # reutrn related artists
    return json_result["artists"]


def authorization(token):
    return {"Authorization": f"Bearer {token}"}


def test(artist_name):
    token = get_token()
    artists = search_related_artist(token, artist_name)

    for artist in artists:
        print(artist["name"], artist["genres"], artist["id"])

if __name__ == "__main__":
    test("taylor swift")