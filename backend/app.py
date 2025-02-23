from flask import Flask, render_template

app = Flask(__name__)

'''
Home Redirect
'''
@app.route('/')
def hello_world():
    return render_template('idk.html')


song_url = "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/d1/b8/d4/d1b8d4c6-daf7-f6a0-e4fc-fb9abe0a4277/mzaf_834058705086793867.plus.aac.p.m4a"
artist = "Kendrick Lamar"
song_name = "GNX"
album_art = "https://is1-ssl.mzstatic.com/image/thumb/Music211/v4/50/c2/cc/50c2cc95-3658-9417-0d4b-831abde44ba1/24UM1IM28978.rgb.jpg/316x316bb.webp"

'''
TEST
'''
@app.route('/music')
def get_curr_song():
    return {
        'artist': artist,
        'song_name': song_name,
        'song_url': song_url,
        'album_art': album_art}