#importing getposter to get posters
import internal.Poster.getposter as gp

import mysql.connector
import random
import json

#____________________________________________________________________________________________________________________

def TemplateCommand(type, value, end, String):
    #Here, 'type' = {where, AND, OR, JOIN, UNION, INTERSECTION}
    #&, 'value' = genres
    #&, 'end' = {;, space}

    String = String + type + " FIND_IN_SET('" + value + "', genres)>0" + end
    return String

#____________________________________________________________________________________________________________________

def GetFromOneGenre(MainOutputList, Movies, Cursor, year, random):
    for index in range(len(MainOutputList)):
        Gen = MainOutputList[index]    
        
        command = "Select tconst, primaryTitle, genres, startYear from data2 where genres = '" + Gen + "';"

        #print(command)
        Cursor.execute(command)
        Result = Cursor.fetchall()
        TempMovies = []
        
        for j in range(len(Result)):
            if int(Result[j][3])>year and Result[j][3] != '\\N':
                TempMovies.append(Result[j])        
        
        j = random.randint(0, len(TempMovies)-1)
        MovieIndex = len(Movies)
        href_movie = f"https://www.imdb.com/title/{TempMovies[j][0]}/"
        Poster = gp.getposter(tconst=str(TempMovies[j][0]), Name=str(TempMovies[j][1]))
        Movies["{0}".format(MovieIndex+1)] = {"tconst": TempMovies[j][0],"href_movie": href_movie, "Name": TempMovies[j][1], "Genres": TempMovies[j][2], "Year": TempMovies[j][3], "Poster": Poster}

    return Movies

#____________________________________________________________________________________________________________________

def GetFromTwoGenre(MainOutputList, Movies, Cursor, year, random):

    TempList = MainOutputList[:3]

    for index1 in range(len(TempList)):
        Gen1 = TempList[index1]

        for index2 in range(index1+1, len(TempList)):
            Gen2 = TempList[index2]
        
            command = "Select tconst, primaryTitle, genres, startYear from data2 "
            command = TemplateCommand('where', Gen1, ' ', command)
            command = TemplateCommand('AND', Gen2, ';', command)
            #print(command)

            Cursor.execute(command)
            Result = Cursor.fetchall()
            TempMovies = []
    
            for j in range(len(Result)):
                if int(Result[j][3])>year and Result[j][3] != '\\N':
                    TempMovies.append(Result[j])

            j = random.randint(0, len(TempMovies)-1)
            MovieIndex = len(Movies)
            href_movie = f"https://www.imdb.com/title/{TempMovies[j][0]}/"
            Poster = gp.getposter(tconst=str(TempMovies[j][0]), Name=str(TempMovies[j][1]))
            Movies["{0}".format(MovieIndex+1)] = {"tconst": TempMovies[j][0],"href_movie": href_movie, "Name": TempMovies[j][1], "Genres": TempMovies[j][2], "Year": TempMovies[j][3], "Poster": Poster}

    
    return Movies

#____________________________________________________________________________________________________________________

def GetFromThreeGenre(MainOutputList, Movies, Cursor, year, random):

    Gen1 = MainOutputList[0]
    Gen2 = MainOutputList[1]
    Gen3 = MainOutputList[2]

    command = "Select tconst, primaryTitle, genres, startYear from data2 "
    command = TemplateCommand('where', Gen1, ' ', command)
    command = TemplateCommand('AND', Gen2, ' ', command)
    command = TemplateCommand('AND', Gen3, ';', command)
    #print(command)

    Cursor.execute(command)
    Result = Cursor.fetchall()
    TempMovies = []
    
    for j in range(len(Result)):
        if int(Result[j][3])>year and Result[j][3] != '\\N':
            TempMovies.append(Result[j])

    j = random.randint(0, len(TempMovies)-1)
    MovieIndex = len(Movies)
    href_movie = f"https://www.imdb.com/title/{TempMovies[j][0]}/"
    Poster = gp.getposter(tconst=str(TempMovies[j][0]), Name=str(TempMovies[j][1]))
    Movies["{0}".format(MovieIndex+1)] = {"tconst": TempMovies[j][0],"href_movie": href_movie, "Name": TempMovies[j][1], "Genres": TempMovies[j][2], "Year": TempMovies[j][3], "Poster": Poster}

    return Movies
    
#____________________________________________________________________________________________________________________

def getMovies(MainOutputList):
    
    mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "22072000", database = "test")
    Cursor = mydb.cursor()
    
    Movies = {}

    Movies = GetFromOneGenre(MainOutputList, Movies, Cursor, 2010, random)
    Movies = GetFromTwoGenre(MainOutputList, Movies, Cursor, 2010, random)
    #Movies = GetFromThreeGenre(MainOutputList, Movies, Cursor, 2010, random)
    

    #file = open("JSONdata.json", "a")
    JSONdata = json.dumps(Movies, ensure_ascii= False)

    #file.write(JSONdata)
    #file.close()

    return JSONdata

#____________________________________________________________________________________________________________________

"""MainOutputList = ['ACTION', 'ROMANCE', 'SPORT', 'CRIME', 'ADVENTURE']

Movies = getMovies(MainOutputList)
print(Movies)"""