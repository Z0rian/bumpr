import os
import tkinter as tk
from tkinter import ttk, Entry, messagebox
import pygame
import pandas as pd

# Initialize pygame mixer
pygame.mixer.init()

# Song data
mySongs = {
    'song': ['BackInBlack', 'BohemianRhapsody', 'Imagine', 'StairwayToHeaven', 'HeyJude',
             'SmellsLikeTeenSpirit', 'HotelCalifornia', 'LikeARollingStone', 'BillieJean', 'ShapeOfYou'],
    'file': ['backinblack.mp3', 'bohemianrhapsody.mp3', 'imagine.mp3', 'stairwaytoheaven.mp3', 'heyjude.mp3',
             'smellsliketeenspirit.mp3', 'hotelcalifornia.mp3', 'likearollingstone.mp3', 'billiejean.mp3', 'shapeofyou.mp3'],
    'album': ['BackInBlack', 'ANightAtTheOpera', 'Imagine', 'LedZeppelinIV', 'Revolver',
              'Nevermind', 'HotelCalifornia', 'Highway61Revisited', 'Thriller', 'Divide'],
    'artist': ['AC/DC', 'Queen', 'John Lennon', 'Led Zeppelin', 'The Beatles', 'Nirvana',
               'The Eagles', 'Bob Dylan', 'Michael Jackson', 'Ed Sheeran'],
    'length': [253, 355, 181, 482, 240, 301, 390, 373, 294, 233],
    'genre': ['Rock', 'Rock', 'Pop', 'Rock', 'Rock', 'Grunge', 'Rock', 'Rock', 'Pop', 'Pop']
}

songdf = pd.DataFrame(mySongs)
current_song_index = 0

# --- Functions ---

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

def toggle_play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songdf)
    play_song()

def prev_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songdf)
    play_song()

def search_song(*args):
    query = search_entry.get().lower()
    tree.delete(*tree.get_children())
    filtered_df = songdf[songdf['song'].str.lower().str.contains(query)] if query else songdf
    populate_table(filtered_df)

def on_song_select(event):
    selected = tree.focus()
    if selected:
        index = int(tree.item(selected)['text'])
        play_song(index)

def loadSong():
    songSelector = tk.Toplevel(root)
    songSelector.title("Load Song")
    songSelector.geometry("400x350")

    song_listbox = tk.Listbox(songSelector)
    song_listbox.pack(fill=tk.BOTH, expand=True)

    music_files = []
    for root_dir, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.mp3'):
                full_path = os.path.join(root_dir, file)
                music_files.append(full_path)

    for song in music_files:
        song_listbox.insert(tk.END, song)

def populate_table(data):
    for i, row in data.iterrows():
        tree.insert('', 'end', text=str(i), values=list(row))

# --- GUI Setup ---
root = tk.Tk()
root.title("Bumpr Music Player")
root.geometry("700x400")

# Left frame for table
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

search_entry = Entry(frame)
search_entry.pack(side=tk.TOP, fill=tk.X)
search_entry.bind("<KeyRelease>", search_song)



columns = list(songdf.columns)
tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="w")

tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Double-1>", on_song_select)

populate_table(songdf)

# Right frame for controls
controls_frame = tk.Frame(root)
controls_frame.pack(side=tk.BOTTOM, pady=10)

prev_button = tk.Button(controls_frame, text="⏮️", command=prev_song)
prev_button.pack(side=tk.LEFT, padx=5)

play_button = tk.Button(controls_frame, text="▶️/⏸️", command=toggle_play_pause)
play_button.pack(side=tk.LEFT, padx=5)

next_button = tk.Button(controls_frame, text="⏭️", command=next_song)
next_button.pack(side=tk.LEFT, padx=5)

load_song_button = tk.Button(controls_frame, text="Load Song", command=loadSong)
load_song_button.pack(side=tk.TOP, pady=20)

song_label = tk.Label(root, text="Select a song to play")
song_label.pack(side=tk.TOP, pady=10)

root.mainloop()
