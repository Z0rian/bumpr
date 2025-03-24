"""
Bumpr Music Service Project
Authors: Alex, Josh, and Zorian

"""

import pygame
import pandas as pd
import numpy as np

pygame.mixer.init()

#make a dictionary
mySongs = {
    'song': ['BackInBlack', 'BohemianRhapsody', 'Imagine', 'StairwayToHeaven', 'HeyJude', 
                 'SmellsLikeTeenSpirit', 'HotelCalifornia', 'LikeARollingStone', 'BillieJean', 'ShapeOfYou'],
    'file': ['AC DC - Back In Black (Official 4K Video).mp3', 'bohemianrhapsody.mp3', 'imagine.mp3', 'stairwaytoheaven.mp3', 'heyjude.mp3',
             'smellsliketeenspirit.mp3', 'hotelcalifornia.mp3', 'likearollingstone.mp3', 'billiejean.mp3', 'shapeofyou.mp3'],
    'album': ['BackInBlack', 'ANightAtTheOpera', 'Imagine', 'LedZeppelinIV', 'Revolver', 
              'Nevermind', 'HotelCalifornia', 'Highway61Revisited', 'Thriller', 'Divide'],
   'length': [253, 355, 181, 482, 240, 
               301, 390, 373, 294, 233],
    'genre': ['Rock', 'Rock', 'Pop', 'Rock', 'Rock', 
              'Grunge', 'Rock', 'Rock', 'Pop', 'Pop']
}
    



songdf = pd.DataFrame(mySongs)



#print(songdf)
#print(type(songdf[songdf['song'] == 'BackInBlack']['file']))

#print((songdf[songdf['song'] == 'BackInBlack']['file']).split(" "), (1))


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
        songIndex = int(input("Enter song index: "))
        pygame.mixer.music.load(mySongs['file'][songIndex])
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



# Keep the program running while audio plays
while pygame.mixer.music.get_busy():
    pass
