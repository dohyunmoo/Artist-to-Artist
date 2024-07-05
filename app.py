from flask import Flask, render_template, request, redirect, url_for, jsonify

import api

app = Flask(__name__, template_folder="static")
app.config["JSON_AS_DICT"] = True

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game", methods=["POST", "GET"])
def game():
    data = request.form.to_dict()

    start_artist = data.get("start-artist")
    target_artist = data.get("target-artist")

    print(start_artist, target_artist)

    token = api.get_token()
    artists = api.search_related_artist(token, start_artist)
    related_artists_names = []

    for artist in artists:
        # print(artist["name"], artist["genres"], artist["id"])
        related_artists_names.append(artist["name"])

    return render_template(
        "game.html",
        start_artist=start_artist,
        target_artist=target_artist,
        related_artists=related_artists_names,
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)
