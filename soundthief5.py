import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pour gérer l'image du logo
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import threading
import os
import subprocess  # Pour lancer le lecteur de MP3 de Windows

# Variables globales
is_recording = False
audio_data = []

def start_recording():
    global is_recording, audio_data
    if not is_recording:
        # Démarrer l'enregistrement
        is_recording = True
        record_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        play_button.config(state=tk.DISABLED)
        status_label.config(text="Enregistrement en cours...", fg="red")
        audio_data = []  # Réinitialiser les données audio
        threading.Thread(target=record_audio).start()

def stop_recording():
    global is_recording
    if is_recording:
        # Arrêter l'enregistrement
        is_recording = False
        record_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)
        play_button.config(state=tk.NORMAL)
        status_label.config(text="Enregistrement terminé", fg="green")
        save_audio_to_file()

def play_recording():
    try:
        # Lancer le lecteur de MP3 de Windows pour jouer le fichier
        if os.path.exists("output.mp3"):
            subprocess.run(["start", "output.mp3"], shell=True)
        else:
            status_label.config(text="Aucun fichier à jouer", fg="red")
    except Exception as e:
        status_label.config(text=f"Erreur de lecture : {str(e)}", fg="red")

def record_audio():
    global audio_data
    with sd.InputStream(samplerate=44100, channels=2, dtype='int16', device=input_device.get()) as stream:
        while is_recording:
            data, _ = stream.read(1024)
            audio_data.append(data)

def save_audio_to_file():
    global audio_data
    if audio_data:
        audio_array = np.concatenate(audio_data, axis=0)
        write("output.wav", 44100, audio_array)
        print("Fichier WAV enregistré : output.wav")
        convert_to_mp3("output.wav", "output.mp3")

def convert_to_mp3(input_file, output_file):
    try:
        audio = AudioSegment.from_wav(input_file)
        audio.export(output_file, format="mp3")
        print(f"Conversion réussie : {output_file}")
    except Exception as e:
        print(f"Erreur lors de la conversion en MP3 : {str(e)}")

# Interface graphique
root = tk.Tk()
root.title("Sound Thief (C)2025 - Dr CADIC")
root.geometry("600x240")  # Augmentation de la largeur pour accueillir le logo
root.configure(bg="black")

# Charger le logo
try:
    logo_image = Image.open("logo250x250.jpg")
    # Utiliser Resampling.LANCZOS au lieu de ANTIALIAS
    logo_image = logo_image.resize((200, 200), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo, bg="black")
    logo_label.image = logo_photo  # Garder une référence pour éviter la suppression par le garbage collector
    logo_label.pack(side=tk.LEFT, padx=20, pady=10)
except Exception as e:
    print(f"Erreur lors du chargement du logo : {str(e)}")
    # Si le logo ne charge pas, afficher un message à la place
    logo_label = tk.Label(root, text="Logo non chargé", bg="black", fg="white")
    logo_label.pack(side=tk.LEFT, padx=10, pady=10)

# Liste des périphériques audio disponibles
devices = sd.query_devices()
input_devices = [device['name'] for device in devices if device['max_input_channels'] > 0]

# Menu déroulant pour choisir la source audio
input_device = ttk.Combobox(root, values=input_devices, width=40)
input_device.current(0)  # Sélectionner le premier périphérique par défaut
input_device.pack(pady=10)

# Boutons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

# Bouton d'enregistrement
record_button = tk.Button(button_frame, text="●", font=("Arial", 24), command=start_recording, bg="gray", fg="red", bd=0, state=tk.NORMAL)
record_button.grid(row=0, column=0, padx=10)

# Bouton d'arrêt
stop_button = tk.Button(button_frame, text="■", font=("Arial", 24), command=stop_recording, bg="dark gray", fg="white", bd=0, state=tk.DISABLED)
stop_button.grid(row=0, column=1, padx=10)

# Bouton de lecture
play_button = tk.Button(button_frame, text="▶", font=("Arial", 24), command=play_recording, bg="gray", fg="green", bd=0, state=tk.DISABLED)
play_button.grid(row=0, column=2, padx=10)

# Label pour afficher l'état de l'enregistrement
status_label = tk.Label(root, text="Prêt", fg="white", bg="black", font=("Arial", 12))
status_label.pack(side=tk.BOTTOM, pady=10)

# Lancer l'interface
root.mainloop()