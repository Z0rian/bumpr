# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 11:25:24 2025

@author: Alex, Josh, Zorian
"""

import tkinter as tk
from tkinter import Listbox, Scrollbar
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Song data
directory = "Bumpr_music/"
songs = [
    ("Back in Black", "backinblack.mp3"),
    ("Bohemian Rhapsody", "bohemianrhapsody.mp3"),
    ("Imagine", "imagine.mp3"),
    ("Stairway to Heaven", "stairwaytoheaven.mp3"),
    ("Hey Jude", "heyjude.mp3"),
    ("Smells Like Teen Spirit", "smellsliketeenspirit.mp3"),
    ("Hotel California", "hotelcalifornia.mp3"),
    ("Like A Rolling Stone", "likearollingstone.mp3"),
    ("Billie Jean", "billiejean.mp3"),
    ("Shape of You", "shapeofyou.mp3")
]

current_song_index = 0

# Function to load and play a song
def play_song(index=None):
    global current_song_index
    if index is not None:
        current_song_index = index
    song_file = directory + songs[current_song_index][1]
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play()
    song_label.config(text=f"Now Playing: {songs[current_song_index][0]}")

# Function to pause or unpause
def toggle_play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Function to play next song
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song()

# Function to play previous song
def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song()

# GUI Setup
root = tk.Tk()
root.title("Bumpr Music Player")
root.geometry("400x300")

# Song List
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

song_list = Listbox(frame, yscrollcommand=scrollbar.set, width=30)
for i, (song_name, _) in enumerate(songs):
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

# Add Song Dialogue




root.mainloop()