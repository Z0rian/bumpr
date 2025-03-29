"""
Bumpr Music Service Project
Authors: Alex, Josh, and Zorian

"""
import os
import tkinter as tk
from tkinter import ttk, Listbox
import pygame
import pandas as pd

# Initialize pygame mixer
pygame.mixer.init()

# Song data
mySongs = {
    'song': ['BackInBlack', 'BohemianRhapsody', 'Imagine', 'StairwayToHeaven', 'HeyJude', 
             'SmellsLikeTeenSpirit', 'HotelCalifornia', 'LikeARollingStone', 'BillieJean', 'ShapeOfYou'],
    'artist': ['AC/DC', 'Queen', 'John Lennon', 'Led Zeppelin', 'The Beatles', 'Nirvana',
               'The Eagles', 'Bob Dylan', 'Michael Jackson', 'Ed Sheeran'],
    'album': ['BackInBlack', 'ANightAtTheOpera', 'Imagine', 'LedZeppelinIV', 'Revolver', 
              'Nevermind', 'HotelCalifornia', 'Highway61Revisited', 'Thriller', 'Divide'],
    'file': ['Bumpr_music/backinblack.mp3', 'Bumpr_music/bohemianrhapsody.mp3', 'Bumpr_music/imagine.mp3', 'Bumpr_music/stairwaytoheaven.mp3', 'Bumpr_music/heyjude.mp3',
             'Bumpr_music/smellsliketeenspirit.mp3', 'Bumpr_music/hotelcalifornia.mp3', 'Bumpr_music/likearollingstone.mp3', 'Bumpr_music/billiejean.mp3', 'Bumpr_music/shapeofyou.mp3'],
    'length': [253, 355, 181, 482, 240, 301, 390, 373, 294, 233],
    'genre': ['Rock', 'Rock', 'Pop', 'Rock', 'Rock', 'Grunge', 'Rock', 'Rock', 'Pop', 'Pop']
}

songdf = pd.DataFrame(mySongs)

# GUI Setup
root = tk.Tk()
root.title("Bumpr Music Player")
root.geometry("1000x400")  # Set balanced startup size
root.configure(bg="#222")

# Configure row/column weights for flexible resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=6)  # Left side (song list) initially wider
root.grid_columnconfigure(1, weight=3)  # Right side (controls) starts smaller

# --- Left Side (Song List) ---
frame_left = tk.Frame(root, bg="#222")
frame_left.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

# Search Bar
search_entry = tk.Entry(frame_left)
search_entry.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
search_entry.bind("<KeyRelease>", lambda event: update_table())

# Table (Treeview)
columns = list(songdf.columns)
tree = ttk.Treeview(frame_left, columns=columns, show="headings", height=10)

# Set column widths (song full width, others shortened)
column_widths = {
    "song": 180, "artist": 100, "album": 120, "file": 80, "length": 50, "genre": 70
}

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=column_widths[col], anchor="w")

tree.pack(fill="both", expand=True)

# Function to Populate Table
def update_table():
    query = search_entry.get().strip().lower()
    tree.delete(*tree.get_children())  # Clear table

    filtered_df = songdf[songdf['song'].str.lower().str.contains(query)] if query else songdf

    for _, row in filtered_df.iterrows():
        tree.insert("", tk.END, values=list(row))

# Initial Table Population
update_table()

# --- Right Side (Player Controls) ---
frame_right = tk.Frame(root, bg="#222")
frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

# "Select a song to play" Label
label = tk.Label(frame_right, text="Select a song to play", bg="#222", fg="white", font=("Arial", 12))
label.pack(pady=5)

is_playing = False

# Function to Play/Pause
def toggle_play_pause():
    global is_playing
    selected_item = tree.focus()
    if not selected_item:
        return

    song_data = tree.item(selected_item, "values")
    song_file = song_data[3]

    if not is_playing:
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()
        play_pause_button.config(text="⏸")
        is_playing = True
    else:
        pygame.mixer.music.pause()
        play_pause_button.config(text="▶")
        is_playing = False

def play_next():
    selected = tree.focus()
    if not selected:
        return
    next_item = tree.next(selected)
    if next_item:
        tree.selection_set(next_item)
        tree.focus(next_item)
        toggle_play_pause()

def play_prev():
    selected = tree.focus()
    if not selected:
        return
    prev_item = tree.prev(selected)
    if prev_item:
        tree.selection_set(prev_item)
        tree.focus(prev_item)
        toggle_play_pause()

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

# Control Buttons
button_frame = tk.Frame(frame_right, bg="#222")
button_frame.pack()

prev_button = tk.Button(button_frame, text="⏮", width=5, command=play_prev)
play_pause_button = tk.Button(button_frame, text="▶", width=5, command=toggle_play_pause)
next_button = tk.Button(button_frame, text="⏭", width=5, command=play_next)

prev_button.pack(side=tk.LEFT, padx=5)
play_pause_button.pack(side=tk.LEFT, padx=5)
next_button.pack(side=tk.LEFT, padx=5)

# Add Songs
load_song_button = tk.Button(frame_right, text="Load Song", command=loadSong)
load_song_button.pack(side=tk.TOP, pady=10)

root.mainloop()
