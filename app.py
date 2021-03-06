from turtle import update
from flask import Flask, render_template, request
#from Get_songs import update_songs
import random
from Song_Info import db, Song_Info
from Find_lyrics import clean_lyrics
from multiprocessing import Value
import random
from sqlalchemy.sql import func
from Song_Info import app

from update import update_songs
from apscheduler.schedulers.background import BackgroundScheduler


#current_top_50_info = update_songs()

sched = BackgroundScheduler(daemon=True)
sched.add_job(update_songs,'interval',minutes=1440)
sched.start()

def get_random_song():
    random.seed = 4
    given = Song_Info.query.order_by(func.random()).first()
    artist = given.artist
    song_name=  given.title
    lyrics = clean_lyrics(given.lyrics)
    new_song = (artist, song_name, lyrics)
    return new_song

#get_random_song()

new_song = get_random_song()[2]

counter = Value('i', 0)

song = get_random_song()
@app.route('/', methods = ["GET", "POST"])
def index():
    song = get_random_song()
    song = get_random_song()
    song_artist = song[0]
    song_name = song[1]
    song_lyrics = song[2]
    data = {'song_artist': song_artist, 'song_name': song_name, 'song_lyrics': song_lyrics}
    return render_template('home.html', data=data)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)




