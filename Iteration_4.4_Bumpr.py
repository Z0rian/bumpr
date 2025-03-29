"""
Bumpr Music Service Project
Authors: Alex, Josh, and Zorian

"""

import os
import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, messagebox
import pygame
import pandas as pd

# Initialize pygame mixer
pygame.mixer.init()

# Song data
mySongs = {
    'song': ['BackInBlack', 'BohemianRhapsody', 'Imagine', 'StairwayToHeaven', 'HeyJude', 
             'SmellsLikeTeenSpirit', 'HotelCalifornia', 'LikeARollingStone', 'BillieJean', 'ShapeOfYou'],
    'file': ['Bumpr_music/backinblack.mp3', 'Bumpr_music/bohemianrhapsody.mp3', 'Bumpr_music/imagine.mp3', 'Bumpr_music/stairwaytoheaven.mp3', 'Bumpr_music/heyjude.mp3',
             'Bumpr_music/smellsliketeenspirit.mp3', 'Bumpr_music/hotelcalifornia.mp3', 'Bumpr_music/likearollingstone.mp3', 'Bumpr_music/billiejean.mp3', 'Bumpr_music/shapeofyou.mp3'],
    'album': ['BackInBlack', 'ANightAtTheOpera', 'Imagine', 'LedZeppelinIV', 'Revolver', 
              'Nevermind', 'HotelCalifornia', 'Highway61Revisited', 'Thriller', 'Divide'],
    'artist': ['AC/DC', 'Queen', 'John Lennon', 'Led Zeppelin', 'The Beatles', 'Nirvana',
               'The Eagles', 'Bob Dylan', 'Michael Jackson', 'Ed Sheeran'],
    'length': [253, 355, 181, 482, 240, 301, 390, 373, 294, 233],
    'genre': ['Rock', 'Rock', 'Pop', 'Rock', 'Rock', 'Grunge', 'Rock', 'Rock', 'Pop', 'Pop']
}

songdf = pd.DataFrame(mySongs)
current_song_index = 0

# Function to load and play a song
def play_song(index=None):
    global current_song_index
    if index is not None:
        current_song_index = index
    song_file = songdf['file'][current_song_index]
    if not os.path.exists(song_file):
        messagebox.showerror("File Not Found", f"Error: The file {song_file} does not exist.")
        return
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play()
    song_label.config(text=f"Now Playing: {songdf['song'][current_song_index]}")

# Function to pause or unpause
def toggle_play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Function to play next song
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songdf)
    play_song()

# Function to play previous song
def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songdf)
    play_song()

# Function to filter songs based on search query
def search_song():
    query = search_entry.get().lower()
    song_list.delete(0, tk.END)
    for i, song_name in enumerate(songdf['song']):
        if query in song_name.lower():
            song_list.insert(tk.END, song_name)

def loadSong():
    songSelector = tk.Toplevel(root)  
    songSelector.title("Load Song")
    songSelector.geometry("400x350")

    # Create a listbox to display found songs
    song_listbox = Listbox(songSelector)
    song_listbox.pack(fill=tk.BOTH, expand=True)

    # Search recursively for .mp3 files in all subdirectories
    music_files = []
    for root_dir, _, files in os.walk('.'):  # Walk through all directories
        for file in files:
            if file.endswith('.mp3'):
                full_path = os.path.join(root_dir, file)  # Get full file path
                music_files.append(full_path)  # Store file path

    # Add songs to the listbox
    for song in music_files:
        song_listbox.insert(tk.END, song)


# GUI Setup
root = tk.Tk()
root.title("Bumpr Music Player")
root.geometry("400x350")

# Song List Frame
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Search Bar
search_entry = Entry(frame)
search_entry.pack(side=tk.TOP, fill=tk.X)
search_entry.bind("<KeyRelease>", lambda event: search_song())

scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

song_list = Listbox(frame, yscrollcommand=scrollbar.set, width=30)
for i, song_name in enumerate(songdf['song']):
    song_list.insert(i, song_name)

song_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
song_list.bind("<Double-Button-1>", lambda event: play_song(song_list.curselection()[0]))
scrollbar.config(command=song_list.yview)

# Controls
controls_frame = tk.Frame(root)
controls_frame.pack(side=tk.BOTTOM, pady=10)

prev_button = tk.Button(controls_frame, text="⏮️", command=prev_song)
prev_button.pack(side=tk.LEFT, padx=5)

play_button = tk.Button(controls_frame, text="▶️/⏸️", command=toggle_play_pause)
play_button.pack(side=tk.LEFT, padx=5)

next_button = tk.Button(controls_frame, text="⏭️", command=next_song)
next_button.pack(side=tk.LEFT, padx=5)

# Song Label
song_label = tk.Label(root, text="Select a song to play")
song_label.pack(side=tk.TOP, pady=10)

# Add Songs
load_song_button = tk.Button(root, text="Load Song", command=loadSong)
load_song_button.pack(side=tk.TOP, pady=10)


root.mainloop()