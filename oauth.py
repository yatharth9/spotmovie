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
    return render_template("index.html")

@app.route('/rd')
def login():
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
    return str(sp.current_user_saved_tracks(limit=20, offset=0)['items'])

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