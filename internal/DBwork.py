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
        
        """
        max = 0
        for j in Result:
            if j[6]>max:
                max = j[6]
                value = j
        """
        """
        max1 = 0
        max2 = 9999999
        value = []
        for j in range(len(Result)):
            if Result[j][6]>max1 and Result[j][7]<max2:
                max1 = Result[j][6]
                max2 = Result[j][7]
                value.append(j)
        """        
        """
        print("length - %d" %len(Result))
        print("value - ")
        print(value, end="\n\n")
        """

        for index in range(Range):
            Movies.append(Result[index])
        """
        for j in range(len(Result)):
            if int(Result[j][3])>year and Result[j][3] != '\\N':
                TempMovies.append(Result[j])        
        
        j = random.randint(0, len(TempMovies)-1)
        MovieIndex = len(Movies)
        print(MovieIndex)
        href_movie = f"https://www.imdb.com/title/{TempMovies[j][0]}/"
        #Poster = gp.getposter(tconst=str(TempMovies[j][0]), Name=str(TempMovies[j][1]))
        #Movies.append({"tconst": TempMovies[j][0],"href_movie": href_movie, "Name": TempMovies[j][1], "Genres": TempMovies[j][2], "Year": TempMovies[j][3], "Poster": Poster})
        
        Movies.append({"tconst": TempMovies[j][0],"href_movie": href_movie, "Name": TempMovies[j][1], "Genres": TempMovies[j][2], "Year": TempMovies[j][3]})
        """

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

            """
            max = 0
            for j in Result:
                if j[6]>max:
                    max = j[6]
                    value = j
            """
            """
            max1 = 0
            max2 = 9999999
            value = []
            for j in range(len(Result)):
                if Result[j][6]>max1 and Result[j][7]<max2:
                    max1 = Result[j][6]
                    max2 = Result[j][7]
                    value.append(j)
            """
            """
            print("length - %d" %len(Result))
            print("value - ")
            print(value, end="\n\n")
            """

            for index in range(Range):
                Movies.append(Result[index])
            """
            TempMovies = []
    
            for j in range(len(Result)):
                if int(Result[j][3])>year and Result[j][3] != '\\N':
                    TempMovies.append(Result[j])

            j = random.randint(0, len(TempMovies)-1)
            MovieIndex = len(Movies)
            href_movie = f"https://www.imdb.com/title/{TempMovies[j][0]}/"
            #Poster = gp.getposter(tconst=str(TempMovies[j][0]), Name=str(TempMovies[j][1]))
            #Movies.append({"tconst": TempMovies[j][0],"href_movie": href_movie, "Name": TempMovies[j][1], "Genres": TempMovies[j][2], "Year": TempMovies[j][3], "Poster": Poster})
            
            Movies.append({"tconst": TempMovies[j][0],"href_movie": href_movie, "Name": TempMovies[j][1], "Genres": TempMovies[j][2], "Year": TempMovies[j][3]})
            """
    
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
        #file = open("RedirectedOutput.json", "w")
        #JSONdata = json.dumps(Movies, ensure_ascii= False)

        #file.write(JSONdata)
        #file.close()

        return m.iloc[:,:].values
    
    except mysql.connector.Error as error:
        print("Failed to get the data from the database - {}".format(error))

    finally:
        if mydb.is_connected():
            Cursor.close()
            mydb.close()
            print("MySQL connection is closed")

#____________________________________________________________________________________________________________________
"""
MainOutputList = ['ACTION', 'SPORT', 'CRIME', 'ADVENTURE']
#MainOutputList = ['ROMANCE', 'CRIME', 'HORROR']

St = time.time()
Movies = getMovies(MainOutputList)
Et = time.time()
print("Time elapsed - {0}".format(Et-St))

userRequest = True      #Assuming the user had Logged in
try:  
    start = 0
    end = 10 
    while(userRequest):
        print(tabulate(Movies[start:end], tablefmt="pipe"))
        print(len(Movies))

        if end == len(Movies):
            print("----------------------------------------THANKS FOR CHOOSING OUR RECOMMENDATIONS----------------------------------------")
            break

        i = int(input("LOAD MORE: (1 for yes/ 0 for exit) : "))
        if i == 0:
            userRequest = False
            print("----------------------------------------THANKS FOR CHOOSING OUR RECOMMENDATIONS----------------------------------------")
        else:   
            start = end
            end += 10
            if(end>=len(Movies)):
                end = len(Movies)
                print("This is the last possible iteration for NOW. ")         
     
except ValueError:
    print("Wrong Value")    
"""