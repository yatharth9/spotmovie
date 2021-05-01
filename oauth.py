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

#genre Finder method 
def genreFinder(name,sp):
    #name is whether an artist or the song name
    result = sp.search(name) #search query

    track = result['tracks']['items'][0]

    artist = sp.artist(track["artists"][0]["external_urls"]["spotify"])
    genreList = artist["genres"]
    
    return genreList

#___________________________________________________________________________________________________________________

def GenreListFinder(MainGenreList):    
    MusicGenreList = ['EDM', 'ROCK', 'JAZZ', 'DUBSTEP', 'R&B', 'TECHNO', 'COUNTRY', 'ELECTRO', 'INDIE', 'POP', 'CLASSICAL', 'HIP-HOP', 'K-POP', 'METAL', 'RAP', 'REGGAE', 'FOLK']

    TempList = []
    MajorGenreList = []

    for i in MainGenreList:
        for j in i:
            temp = j.split()
            for t in temp:
                TempList.append(t.upper())

    TempList = list(dict.fromkeys(TempList))

    if "HIP" in TempList:
        if "HOP" in TempList:
            TempList.append("HIP-HOP")
            TempList.remove("HIP")
            TempList.remove("HOP")

    for i in TempList:
        if i in MusicGenreList:
            MajorGenreList.append(i)

    return MajorGenreList

#___________________________________________________________________________________________________________________

def OutputListFinder(MajorGenreList, pd):  
    data = pd.read_csv("SpotMovies - Filter.csv", header = None)
    x = data.iloc[:, :-2].values
    y = data.iloc[:, -1].values
    Counter = [0]*len(y)

    for j in range(len(x)):
        count = 0
        for index in range(len(MajorGenreList)):
            i = MajorGenreList[index]

            if i == x[j][0]:
                count += 45
                

            elif i == x[j][1]:
                count += 30
                

            elif i == x[j][2]:
                count += 15
                

            elif i == x[j][3]:
                count += 10
                
            else:
                count += 0

        Counter[j] = count


    Output = {}
    for i in range(len(y)):
        if Counter[i] > 45:
            Output[y[i]] = Counter[i]

    OutputList = sorted(Output.items(), key=lambda x: x[1], reverse=True)

    MainOutputList = []
    for i in OutputList:
        MainOutputList.append(i[0])

    return MainOutputList

#___________________________________________________________________________________________________________________

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
        Name = str(track["name"])
        MainGenreList.append(genreFinder(Name, sp))

        MajorGenreList = GenreListFinder(MainGenreList)
        MainOutputList = OutputListFinder(MajorGenreList, pd)
        '''
        temp_list = [str(track["href"]), str(track["id"]), str(track["name"])] #Taking 'href', 'Id' & 'name'
        necessary_data.append(temp_list)
        '''

    return str(MainOutputList)

 
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