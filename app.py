from flask import Flask, render_template, request, redirect, url_for, jsonify
import concurrent.futures

import util
import api

app = Flask(__name__, template_folder="static")
app.config["JSON_AS_DICT"] = True

token = None
target_artist = None
count = 0

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game", methods=["POST", "GET"])
def game():
    global target_artist
    global target_artist_image
    global count
    if request.method == "POST":
        data = request.form.to_dict()

        start_artist = data.get("start-artist")
        target_artist = data.get("target-artist")

        global token
        if token == None:
            token = api.get_token()

        start_artist_image = util.encode_image(api.artist_image(token, start_artist))
        target_artist_image = util.encode_image(api.artist_image(token, target_artist))

        related_artists, encode_list = get_artists(start_artist)

        return render_template(
            "game.html",
            start_artist=start_artist,
            start_artist_image=start_artist_image,
            target_artist=target_artist,
            target_artist_image=target_artist_image,
            related_artists=related_artists,
            encode_list = encode_list,
            count=count
        )
    else:
        chosen_artist = request.args.get("chosen")
        chosen_artist_image = util.encode_image(request.args.get("chosenImage"))

        related_artists, encode_list = get_artists(chosen_artist)
        count += 1

        return render_template(
            "game.html",
            start_artist=chosen_artist,
            start_artist_image=chosen_artist_image,
            target_artist=target_artist,
            target_artist_image=target_artist_image,
            related_artists=related_artists,
            encode_list = encode_list,
            count=count
        )


def get_artists(start_artist):
    global token
    if token == None:
        token = api.get_token()

    print(token)

    artists = api.search_related_artist(token, start_artist)
    related_artists = [(artist["name"], artist["images"][0]["url"]) for artist in artists]
    image_url = [artist["images"][0]["url"] for artist in artists]

    encode_list = []

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(util.encode_image, url) for url in image_url]
        for f in futures:
            encode_list.append(f.result())

    return related_artists, encode_list

if __name__ == '__main__':
    app.run(debug=True, port=5001)
