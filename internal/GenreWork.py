
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

def OutputListFinder(MajorGenreList, Name, Boundary, pd):  
    #Name       - CSV File Name
    #Boundary   - Threshold to choose the genres of total values above threshold

    data = pd.read_csv(Name, header = None)
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
        if Counter[i] > Boundary:
            Output[y[i]] = Counter[i]

    OutputList = sorted(Output.items(), key=lambda x: x[1], reverse=True)

    MainOutputList = []
    for i in OutputList:
        MainOutputList.append(i[0])

    return MainOutputList

#____________________________________________________________________________________________________________________
