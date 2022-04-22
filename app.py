from flask import Flask, render_template
from data import get_data
import random
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello():
    artist_list = ('6M2wZ9GZgrQXHCFfjv46we', '1Y8cdNmUJH7yBTd9yOvr5i', '3Nrfpe0tUJi4K4DXYWgMUX', '5RmQ8k4l3HZ8JoPb4mNsML')
    
    rand = random.randint(0, len(artist_list) - 1)

    data = get_data(artist_list[rand])

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
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080))
    )