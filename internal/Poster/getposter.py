import requests
from bs4 import BeautifulSoup

def getposter(tconst, Name):
    try:    
        #tconst = "tt0371746"
        Poster_base = f"https://www.imdb.com/title/{tconst}/"
        """
        print(tconst)
        print(type(tconst))
        print(Name)
        print(type(Name))
        """
        r = requests.get(Poster_base)

        #print(r.content)
        soup = BeautifulSoup(r.text, "html.parser")

        #Moviename = "Iron Man"
        name = f"{Name} Poster"
        imgelement = soup.find(title = name)
        #print(type(imgelement))
        src = imgelement["src"]
        #print(src)
        return src
    
    except:
        src = "https://cdn.iconscout.com/icon/free/png-256/data-not-found-1965034-1662569.png"
        return src

"""
open(f"poster.html",'wb').write(r.content)
print(f"Written poster.html")"""


"""src = getposter("tt0816692", "Interstellar")
print(src)"""