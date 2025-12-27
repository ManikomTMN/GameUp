from flask import Flask, render_template, send_file, abort
import os

app = Flask(__name__)

def get_location():
    with open("LOCATION.txt", "r") as f:
        return f.read().strip()

@app.route("/thumbnail/<game>")
def thumbnail(game):
    base_path = get_location()
    thumb_path = os.path.join(base_path, game, "THUMBNAIL.png")

    if not os.path.isfile(thumb_path):
        abort(404)

    return send_file(thumb_path)


@app.route("/")
def index():
    base_path = get_location()
    games = []

    for folder in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder)
        if not os.path.isdir(folder_path):
            continue

        game = {
            "folder": folder,
            "name": folder,
            "desc": "",
            "has_thumbnail": False
        }

        info_path = os.path.join(folder_path, "INFO.txt")
        if os.path.isfile(info_path):
            with open(info_path, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
                if len(lines) > 0:
                    game["name"] = lines[0]
                if len(lines) > 1:
                    game["desc"] = lines[1]

        thumb_path = os.path.join(folder_path, "THUMBNAIL.png")
        if os.path.isfile(thumb_path):
            game["has_thumbnail"] = True

        games.append(game)

    return render_template("index.html", games=games)


@app.route("/download/<game>")
def download(game):
    base_path = get_location()
    game_path = os.path.join(base_path, game)

    if not os.path.isdir(game_path):
        abort(404)

    # find the (hopefully only) zip file in the folder
    for item in os.listdir(game_path):
        if item.lower().endswith(".zip"):
            zip_path = os.path.join(game_path, item)
            return send_file(zip_path, as_attachment=True)

    abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
