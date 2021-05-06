# For the Flask App.
from flask import Flask, request, url_for, session, redirect, render_template

# Spotify Api Python Wrapper.
import spotipy

# To authenticate the user with App and to get user data.
from spotipy.oauth2 import SpotifyOAuth

# For the Environement Variables.
import os

# To check if the token is expired or not.
import time

# To send SMS to phone, in case of any Error.
import alert.sms as SMS

#importing JSON
import json

#importing pandas
import pandas as pd

#importing Mysql connector to connect to the Mysql Database
import mysql.connector

#importing to randomize the selection
import random

#importing this package to get functions in use
import internal.DBwork as db
import internal.Poster
import internal.GenreWork as gw

cachefile = ".cache"
if os.path.exists(cachefile):
    os.remove(cachefile)

clientid = os.getenv('SPOTIPY_CLIENT_ID')
clientsecret = os.getenv('SPOTIPY_CLIENT_SECRET')
app = Flask(__name__)


app.secret_key = "ehagoiehfeihfies"
app.config['SESSION_COOKIE_NAME'] = 'Spotipy Cookie'
TOKEN_INFO = "token_info"

@app.route('/')
def home():
    return render_template("Homepage.html")        #REDIRECT button - HOME PAGE

@app.route('/rd')
def login():                                    #Login Page
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for("getTrack", _external=False))

#___________________________________________________________________________________________________________________

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())

    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=clientid,
        client_secret=clientsecret,
        redirect_uri=url_for('redirectPage', _external=True),
        scope="user-library-read")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404


@app.route('/getTracks')
def getTrack():
    try:
        token_info = get_token()
    except:
        print("User not logged in ")
        return redirect(url_for("login", _external=False))

    sp = spotipy.Spotify(auth=token_info['access_token'])

    MainGenreList = []

    #necessary_data = []

    """for i in range(5): 
        user_music_data = sp.current_user_saved_tracks(limit=1, offset=i)['items']  #Here we're using current user saved tracks, can be later replaced with top tracks
        
        '''
        #Here, because we were getting a list in form of string, that's why we didn't preferred to use it!!!

        user_music_data = sp.current_user_saved_tracks(limit=5, offset=0)['items']  #Here we're using current user saved tracks, can be later replaced with top tracks
        user_music_data = str(user_music_data)
        return user_music_data
        '''
        
        #here, item is containing the Python-format Dictionary but in String format
        item = str(user_music_data)        

        #Converting String to Dictionary
        import ast
        movie = ast.literal_eval(item[1:-1:])   #'movie' contains the dictionary which can be used to extract the data
        
        track = movie["track"]
        Name = str(track["name"])
        MainGenreList.append(gw.genreFinder(Name, sp))

        MajorGenreList = gw.GenreListFinder(MainGenreList)
        Name = "SpotMovies - Filter.csv"
        MainOutputList = gw.OutputListFinder(MajorGenreList, Name, 45, pd)
        MainOutputList_Final = []
        
        for i in MainOutputList:
            MainOutputList_Final.append(str(i))
        
        Movies = db.getMovies(MainOutputList_Final)
        '''
        temp_list = [str(track["href"]), str(track["id"]), str(track["name"])] #Taking 'href', 'Id' & 'name'
        necessary_data.append(temp_list)
        '''
    """
    #return str(Movies)      #Returning JSON type data
    return redirect(url_for("results", _external=False))


@app.route('/results')
def results():
    return render_template("RedirectingHomepage.html")

if __name__ == "__main__":
    app.run()