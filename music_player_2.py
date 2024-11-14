# Import necessary libraries
import pygame
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

# Initialize Pygame Mixer
pygame.mixer.init()

# Initialize list to store songs
playlist = []

# Create a function to load and add music to the playlist
def load_music():
    global playlist
    # Allow multiple file selection
    music_files = filedialog.askopenfilenames(title="Select Songs", filetypes=(("mp3 files", "*.mp3"),))
    if music_files:  # Check if files exist
        for music_file in music_files:
            playlist.append(music_file)
            song_listbox.insert(END, os.path.basename(music_file))

# Create a function to play selected music from the playlist
def play_selected_song(event):
    selected_song = song_listbox.curselection()
    if selected_song:
        song_index = selected_song[0]
        music_file = playlist[song_index]
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        song_label.config(text=os.path.basename(music_file))

# Create a function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Create a function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Create a function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Create the main GUI application window
root = Tk()
root.title("Python Music Player")
root.geometry("600x700")
root.config(bg="#1E1E1E")  # Dark background

# Function to show the settings interface
def show_settings():
    clear_frame()
    settings_frame.pack(pady=20)

# Function to show the main interface
def show_main():
    clear_frame()
    main_frame.pack(pady=20)

# Function to clear the current frame
def clear_frame():
    for widget in root.winfo_children():
        widget.pack_forget()

# Main Frame
main_frame = Frame(root, bg="#1E1E1E")

# Title label
title_label = Label(main_frame, text="🎶 Music Player", font=("Helvetica", 22, "bold"), fg="#00CCFF", bg="#1E1E1E")
title_label.pack(pady=20)

# Song label
song_label = Label(main_frame, text="No song loaded", font=("Helvetica", 16), fg="#FFFFFF", bg="#1E1E1E")
song_label.pack(pady=10)

# Create a frame for listbox and scrollbar
frame_listbox = Frame(main_frame, bg="#1E1E1E")
frame_listbox.pack(pady=10)

# Create a styled listbox to display the playlist
song_listbox = Listbox(
    frame_listbox, width=50, height=10, selectmode=SINGLE,
    bg="#282828", fg="white", font=("Helvetica", 12),
    selectbackground="#007ACC", selectforeground="white"
)
song_listbox.pack(side=LEFT, padx=10)
song_listbox.bind('<Double-1>', play_selected_song)  # Play song on double-click

# Add a scrollbar for the listbox
scrollbar = Scrollbar(frame_listbox, orient=VERTICAL)
scrollbar.config(command=song_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
song_listbox.config(yscrollcommand=scrollbar.set)

# Create button frame with custom spacing
button_frame = Frame(main_frame, bg="#1E1E1E")
button_frame.pack(pady=20)

# Define custom-styled buttons with padding and colors
load_button = ttk.Button(button_frame, text="Load Music", command=load_music)
load_button.grid(row=0, column=0, padx=10, pady=10, ipadx=10)

pause_button = ttk.Button(button_frame, text="Pause", command=pause_music)
pause_button.grid(row=0, column=1, padx=10, pady=10, ipadx=10)

resume_button = ttk.Button(button_frame, text="Resume", command=resume_music)
resume_button.grid(row=0, column=2, padx=10, pady=10, ipadx=10)

stop_button = ttk.Button(button_frame, text="Stop", command=stop_music)
stop_button.grid(row=0, column=3, padx=10, pady=10, ipadx=10)

# Settings Frame
settings_frame = Frame(root, bg="#1E1E1E")

# Volume Control
volume_label = Label(settings_frame, text="Volume Control", font=("Helvetica", 22, "bold"), fg="#00CCFF", bg="#1E1E1E")
volume_label.pack(pady=20)

volume_scale = Scale(settings_frame, from_=0, to=1, resolution=0.1, orient=HORIZONTAL, label="Volume", bg="#1E1E1E", fg="white", troughcolor="#282828")
volume_scale.set(0.5)  # Set initial volume to 50%
volume_scale.pack(pady=10)

# Function to set volume based on scale value
def set_volume(value):
    volume = float(value)
    pygame.mixer.music.set_volume(volume)

volume_scale.bind("<Motion>", lambda event: set_volume(volume_scale.get()))

# Button to return to main interface
back_button = ttk.Button(settings_frame, text="Back to Music Player", command=show_main)
back_button.pack(pady=20)

# Show the main interface by default
main_frame.pack(pady=20)

# Button to navigate to settings
settings_button = ttk.Button(main_frame, text="Settings", command=show_settings)
settings_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
