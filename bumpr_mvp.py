"""
 Bumpr Music Service Project
 Authors: Alex, Josh, and Zorian
 
 """

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
    global songdf
    #on_song_select("<Button-2>")
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
 # Add songs to the listbox
    new_songs = []
    for song in music_files:
         song_listbox.insert(tk.END, song)
         if song not in songdf['file'].values:
             print(song)
             new_songs.append({'song': os.path.splitext(os.path.basename(song))[0], 
                               'file': song, 
                               'album': '', 
                               'artist': '', 
                               'length': '', 
                               'genre': ''})
 
    if new_songs:
         new_songs_df = pd.DataFrame(new_songs)
         songdf = pd.concat([songdf, new_songs_df], ignore_index=True)

def populate_table(data):
    for i, row in data.iterrows():
        tree.insert('', 'end', text=str(i), values=list(row))
        
def helpbutton():
    messagebox.showinfo(title="Help",message="Adding songs:\n\
                        -Add mp3 files to folder\n\
                        -Click 'Add Files' and close pop-up window\n\
                        -Search in menu to refresh library\n\
                        -Click on song to play\n\n\
                        Edit song information:\n\
                        -Right Click on song to edit info\n\n\
                        Sorting:\n\
                        -Click on column title to sort")

# --- GUI Setup ---
root = tk.Tk()
root.title("Bumpr Music Player")
root.geometry("1000x400")

# Left frame for table
frame = tk.Frame(root)
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

rightside = tk.Frame(root)
rightside.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

search_entry = Entry(frame)
search_entry.pack(side=tk.TOP, fill=tk.X)
search_entry.bind("<KeyRelease>", search_song)



columns = list(songdf.columns)
tree = ttk.Treeview(frame, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="w")
    
def sort_column(col, reverse):
    sorted_df = songdf.sort_values(by=col, ascending=reverse)
    populate_table(sorted_df)
    tree.heading(col, command=lambda: sort_column(col, not reverse))

for col in columns:
    tree.heading(col, text=col, command=lambda c=col: sort_column(c, False))

    

tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Double-1>", on_song_select)


populate_table(songdf)

def populate_table(data):
    tree.delete(*tree.get_children())
    for i, row in data.iterrows():
        tree.insert('', 'end', text=str(i), values=list(row))


# Right frame for controls
controls_frame = tk.Frame(root)
controls_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)

# Right-click context menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Edit Song Info", command=lambda: edit_song_info(tree.focus()))

def show_context_menu(event):
    selected = tree.identify_row(event.y)
    if selected:
        tree.selection_set(selected)
        menu.post(event.x_root, event.y_root)

tree.bind("<Button-2>", show_context_menu)  # Right-click for 

tree.bind("<Button-3>", show_context_menu)  # Right-click for 

def edit_song_info(item_id):
    if not item_id:
        return
    
    index = int(tree.item(item_id)['text'])
    song_data = songdf.loc[index]

    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Song Info")

    entries = {}
    for i, col in enumerate(songdf.columns):
        tk.Label(edit_window, text=col).grid(row=i, column=0)
        entry = tk.Entry(edit_window)
        entry.insert(0, song_data[col])
        entry.grid(row=i, column=1)
        entries[col] = entry

    def save_changes():
        for col in songdf.columns:
            songdf.at[index, col] = entries[col].get()
        tree.delete(*tree.get_children())
        populate_table(songdf)
        edit_window.destroy()

    save_button = tk.Button(edit_window, text="Save", command=save_changes)
    save_button.grid(row=len(songdf.columns), column=0, columnspan=2)


#sort_columns

prev_button = tk.Button(controls_frame, text="⏮️", command=prev_song)
prev_button.pack(side=tk.LEFT, padx=5,pady=15)

play_button = tk.Button(controls_frame, text="▶️/⏸️", command=toggle_play_pause)
play_button.pack(side=tk.LEFT, padx=6,pady=15)

next_button = tk.Button(controls_frame, text="⏭️", command=next_song)
next_button.pack(side=tk.LEFT, padx=7,pady=15)

load_song_button = tk.Button(controls_frame, text="Add Files", command=loadSong)
load_song_button.pack(side=tk.LEFT, padx=8,pady=15)

song_label = tk.Label(root, text="Select a song to play")
song_label.pack(side=tk.TOP, anchor="n")

help_button = tk.Button(rightside, text="?", command=helpbutton)
help_button.pack(side=tk.TOP, anchor='ne')


root.mainloop()
