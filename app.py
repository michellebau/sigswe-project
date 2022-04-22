import random
from flask import Flask, render_template
from data import get_data

app = Flask(__name__)

@app.route('/')
def hello():

    artist_list = ('6M2wZ9GZgrQXHCFfjv46we', '1Y8cdNmUJH7yBTd9yOvr5i', '0TImkz4nPqjegtVSMZnMRq')
    rand = random.randint(0, len(artist_list) - 1)
    data = get_data()

    return render_template(
        'index.html',
        song_name = data[0],
        artist_names = data[1],
        album_cover = data[2],
        preview_url = data[3],
        spotify_url = data[4]
    )

if __name__ == '__main__':
    app.run(
        debug=True,
    )