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

cachefile = ".cache"
if os.path.exists(cachefile):
    os.remove(cachefile)

clientid = '276a17e1b96d4a4ca9810ab918a90f21'
clientsecret = 'd45b660ec9b04782956c15d43abaaebf'
app = Flask(__name__)


app.secret_key = "ehagoiehfeihfies"
app.config['SESSION_COOKIE_NAME'] = 'Spotipy Cookie'
TOKEN_INFO = "token_info"

@app.route('/')
def home():
    return render_template("index.html")        #REDIRECT button - HOME PAGE

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

@app.route('/getTracks')
def getTrack():
    try:
        token_info = get_token()
    except:
        print("User not logged in ")
        return redirect(url_for("login", _external=False))
    sp = spotipy.Spotify(auth=token_info['access_token'])

    necessary_data = []

    for i in range(5): 
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
        temp_list = [str(track["href"]), str(track["id"]), str(track["name"])] #Taking 'href', 'Id' & 'name'
        necessary_data.append(temp_list)

    return str(necessary_data)
    
 
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

if __name__ == "__main__":
    app.run()