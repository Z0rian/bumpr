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
    'file': ['Bumpr_music/backinblack.mp3', 'Bumpr_music/bohemianrhapsody.mp3', 'Bumpr_music/imagine.mp3', 'Bumpr_music/stairwaytoheaven.mp3', 'Bumpr_music/heyjude.mp3',
             'Bumpr_music/smellsliketeenspirit.mp3', 'Bumpr_music/hotelcalifornia.mp3', 'Bumpr_music/likearollingstone.mp3', 'Bumpr_music/billiejean.mp3', 'Bumpr_music/shapeofyou.mp3'],
    'album': ['BackInBlack', 'ANightAtTheOpera', 'Imagine', 'LedZeppelinIV', 'Revolver', 
              'Nevermind', 'HotelCalifornia', 'Highway61Revisited', 'Thriller', 'Divide'],
    'artist': ['AC/DC', 'Queen', 'John Lennon', 'Led Zeppelin', 'The Beatles', 'Nirvana',
               'The Eagles', 'Bob Dylan', 'Michael Jackson', 'Ed Sheeran'],
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
    print("1: Select song")
    print("a: Pause song")
    print("b: Play song")
    choice = input("Enter your choice")
    if choice == '1':
        print("1: Back in Black")
        print("2: Bohemian Rhapsody")
        print("3: Imagine")
        print("4: Stairway to Heaven")
        print("5: Hey Jude")
        print("6: Smells Like Teen Spirit")
        print("7: Hotel California")
        print("8: Like A Rolling Stone")
        print("9: Billie Jean")
        print("10: Shape of You")
        songIndex = int(input("Enter song index: ")) - 1
        pygame.mixer.music.load(mySongs['file'][songIndex])
        pygame.mixer.music.play()
    elif choice == 'a':
        pygame.mixer.music.pause()
    elif choice == 'b':
        pygame.mixer.music.unpause()



# Keep the program running while audio plays
while pygame.mixer.music.get_busy():
    pass
