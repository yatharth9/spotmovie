def getposter(tconst, Name):
    import requests

    from bs4 import BeautifulSoup

    #tconst = "tt0371746"
    Poster_base = f"https://www.imdb.com/title/{tconst}/"

    r = requests.get(Poster_base)

    #print(r.content)
    soup = BeautifulSoup(r.text, "html.parser")

    #Moviename = "Iron Man"

    imgelement = soup.find(title='{Name} Poster')
    #print(type(imgelement))
    src = imgelement["src"]
    return src
    #print(src)

"""
open(f"poster.html",'wb').write(r.content)
print(f"Written poster.html")"""