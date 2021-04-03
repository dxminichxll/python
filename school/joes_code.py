import csv # Import CSV library

import random

import time





def login(): #login function

    with open("logins.csv") as csvfile: # open CSV file



        reader = csv.DictReader(csvfile) #dictReader will read the details into a dictionary

        database = [] # create an array to store the details



        for row in reader: # iterate through the rows in the file assigning the values to the dictionary

            database.append(dict(username=row['username'],

                                 password=row['password']))



    loggedin = False # boolvalue for logged in



    while not loggedin:

        username = input("Enter your username: ")

        password = input("Enter in your password: ")

        for row in database: # checks rows in database with columns username and password

            Username_File = row['username']

            Password_File = row['password']

            if (Username_File == username and

                Password_File == password):

                loggedin = True

                print("Succesfully logged in")

                main()

        if loggedin is not True:

            print ("Log in failed, enter correct details.")





def main():



    print ("Welcome to the dice game")





    choice= input ("""

                       1. Play game

                       2. Display top 5 scores

                       3. Rules

                       4. Exit



                       """)



    if choice =="1":

           play()

    elif choice=="2":

           topScores()

    elif choice =="3":

           rules()

    else:

           exit()



def play():

    # attempts = 0

    score = 0

    read = open("songs.txt","r")

    songs = read.readlines()

    # print (songs)

    songlist =[]




    for i in range (len(songs)):

        songlist.append(songs[i].strip('\n'))

    # print(songlist)

    while True:

        attempts = 0

        # print(songlist)

        choice = random.choice(songlist)

        artist, song = choice.split('-')

        # print(artist, song)

        while attempts == 0:

            songs = song.split()

            letters = [word[0] for word in songs]



            for x in range(0,2):

                print (artist, "".join(letters))
                # print(song)

                guess = str(input("Guess the song"))



                if guess == song:

                    print ("correct")

                    if attempts == 0:

                        score = score + 3
                        attempts += 1
                        # print("Attempts + 1")

                        break

                    if attempts == 1:

                        score = score + 1

                        break

                else:

                    print("try again")
                    # attempts += 1




            print ("next song")

            time.sleep(1)

main()

#login()
