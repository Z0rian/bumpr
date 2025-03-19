"""
Bumpr Music Service Project
Authors: Alex, Josh, and Zorian

"""

import pygame

pygame.mixer.init()

#make Artist class
class Artist:
    def __init__(self, artistName):
        self.artistName = artistName
    
    def getArtistName(self):
        print("Artist name: " + self.artistName)
        
#make Genre class
class Genre:
    def __init__(self, genreName):
        self.genreName = genreName
    
    def getGenreName(self):
        print("Genre name: " + self.genreName)
        
#=========================================================================================        
#initialize a few preset artists and genres
rock = Genre("Rock")
pop = Genre("Pop")
country = Genre("Country")

acdc = Artist("AC DC")



#make Song class
class Song:
    def __init__(self, title, Artist, Genre):
        self.title = title
        self.artist = artist
        self.genre = genre
    
    def songInfo(self):
        print("Title: " + self.title)
        print("Artist: " + self.artist)
        print("Genre: " + self.genre)
    
    def start(self):
        pygame.mixer.music.load(self.title)
        pygame.mixer.music.play()
        
    def play():
        pygame.mixer.music.play()
    
    def pause():
        pygame.mixer.music.pause()




while True:
    print("1: Play Back in Black")
    print("2: Play Thunderstruck")
    print("3: Play Highway to Hell")
    print("4: Play You Shook Me All Night Long")
    print("5: Play Hell's Bells")
    print("a: Pause song")
    print("b: Play song")
    choice = input("Enter your choice")
    if choice == '1':
        pygame.mixer.music.load("AC DC - Back In Black (Official 4K Video).mp3")
        pygame.mixer.music.play()
    elif choice == '2':
        pygame.mixer.music.load("AC DC - Thunderstruck (Official Video).mp3")
        pygame.mixer.music.play()
    elif choice == '3':
        pygame.mixer.music.load("AC DC - Highway to Hell (Official Video).mp3")
        pygame.mixer.music.play()
    elif choice == '4':
        pygame.mixer.music.load("AC DC - You Shook Me All Night Long (Official 4K Video).mp3")
        pygame.mixer.music.play()
    elif choice == '5':
        pygame.mixer.music.load("AC DC - Hells Bells (Official 4K Video).mp3")
        pygame.mixer.music.play()
    elif choice == 'a':
        pygame.mixer.music.pause()
    elif choice == 'b':
        pygame.mixer.music.unpause()

def newSong():
    newSong = input.print("Song Creation Wizard: Enter song name: ")
    newArtist = input.print("Enter artist name: ")
    newGenre = input.print("Enter genre name: ")


# Keep the program running while audio plays
while pygame.mixer.music.get_busy():
    pass