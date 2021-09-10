#importing getposter to get posters
import internal.Poster.getposter as gp
#import Poster.getposter as gp
import mysql.connector
import pandas as pd
import time
from tabulate import tabulate

def TemplateCommand(type, value, end, String):
    #Here, 'type' = {where, AND, OR, JOIN, UNION, INTERSECTION}
    #&, 'value' = genres
    #&, 'end' = {;, space}

    String = String + type + " FIND_IN_SET('" + value + "', genres)>0" + end
    return String

#____________________________________________________________________________________________________________________

def GetFromOneGenre(MainOutputList, Movies, Cursor, year, Range):
    for index in range(len(MainOutputList)):
        Gen = MainOutputList[index]    
        
        command = "Select tconst, primaryTitle, startYear, runtimeMinutes, genres, directors, averageRating, changeFactor, poster from details_data_movie where startYear > {0} ".format(year)
        command = TemplateCommand('and ', Gen, ' ', command)
        command += "and changeFactor<averageRating/100 ORDER BY changeFactor, averageRating DESC;"
        #print(command)
        Cursor.execute(command)
        Result = Cursor.fetchall()
        
        for index in range(Range):
            Movies.append(Result[index])

    return Movies

#____________________________________________________________________________________________________________________

def GetFromTwoGenre(MainOutputList, Movies, Cursor, year, Range):

    TempList = MainOutputList

    for index1 in range(len(TempList)):
        Gen1 = TempList[index1]

        for index2 in range(index1+1, len(TempList)):
            Gen2 = TempList[index2]
            command = "Select tconst, primaryTitle, startYear, runtimeMinutes, genres, directors, averageRating, changeFactor, poster from details_data_movie where startYear > {0} ".format(year)
            command = TemplateCommand('and ', Gen1, ' ', command)
            command = TemplateCommand('and ', Gen2, ' ', command)
            command += "and changeFactor<averageRating/100 ORDER BY changeFactor, averageRating DESC;"
            #print(command)

            Cursor.execute(command)
            Result = Cursor.fetchall()

            for index in range(Range):
                Movies.append(Result[index])
                
    return Movies

#____________________________________________________________________________________________________________________

def getMovies(MainOutputList):
    
    try:
        mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "22072000", database = "spotmovie")
        Cursor = mydb.cursor(buffered=True)
        
        Movies = []
        #Movies = GetFromOneGenre(MainOutputList, Movies, Cursor, 2000, 2)  #n2
        Movies = GetFromTwoGenre(MainOutputList, Movies, Cursor, 1980, 5)  #n3
        #Movies = GetFromThreeGenre(MainOutputList, Movies, Cursor, 2010, random) #n
        
        m = pd.DataFrame(Movies, columns=["tconst", "primaryTitle", "startYear", "runtimeMinutes", "genres", "directors", "averageRating", "changeFactor", "poster"])
        m.drop_duplicates(subset ="tconst", keep = 'first', inplace = True)
        m.sort_values("averageRating", ascending = False, inplace = True)
        
        return m.iloc[:,:].values
    
    except mysql.connector.Error as error:
        print("Failed to get the data from the database - {}".format(error))

    finally:
        if mydb.is_connected():
            Cursor.close()
            mydb.close()
            print("MySQL connection is closed")

#____________________________________________________________________________________________________________________
