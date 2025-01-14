# soundthief
Utilitaire python pour capturer le son de la carte de votre ordinateur

Ce script Python est un enregistreur audio simple avec une interface graphique. Il permet de capturer le flux audio système (ce qui est envoyé vers les haut-parleurs ou les écouteurs), de l'enregistrer dans un fichier WAV, de le convertir en MP3, et de jouer le fichier enregistré en utilisant le lecteur de MP3 par défaut de Windows.

Fonctionnalités du Script
Enregistrement audio :

Capture le flux audio système en temps réel.

Enregistre l'audio dans un fichier WAV (output.wav).

Conversion en MP3 :

Convertit le fichier WAV en MP3 (output.mp3) après l'enregistrement.

Lecture du fichier audio :

Ouvre le fichier MP3 enregistré avec le lecteur de MP3 par défaut de Windows.

Interface graphique :

Une interface utilisateur simple avec un bouton pour démarrer/arrêter l'enregistrement, un bouton pour jouer le fichier, et un menu pour sélectionner la source audio.

Un logo est affiché à gauche de l'interface.

Fonctions du Script
start_recording() :

Démarre l'enregistrement audio en utilisant sounddevice.

Change l'état des boutons et affiche un message dans l'interface.

stop_recording() :

Arrête l'enregistrement audio.

Sauvegarde les données audio dans un fichier WAV et le convertit en MP3.

Change l'état des boutons et affiche un message dans l'interface.

play_recording() :

Ouvre le fichier MP3 enregistré avec le lecteur de MP3 par défaut de Windows en utilisant subprocess.

record_audio() :

Capture le flux audio système en temps réel et stocke les données dans une liste.

save_audio_to_file() :

Sauvegarde les données audio capturées dans un fichier WAV (output.wav).

Appelle la fonction convert_to_mp3 pour convertir le fichier WAV en MP3.

convert_to_mp3(input_file, output_file) :

Convertit un fichier WAV en MP3 en utilisant pydub.

Librairies Python Utilisées
tkinter :

Pour créer l'interface graphique (fenêtre, boutons, labels, etc.).

PIL (Pillow) :

Pour charger et afficher le logo dans l'interface.

sounddevice :

Pour capturer le flux audio système en temps réel.

numpy :

Pour manipuler les données audio capturées.

scipy.io.wavfile :

Pour sauvegarder les données audio dans un fichier WAV.

pydub :

Pour convertir le fichier WAV en MP3.

subprocess :

Pour ouvrir le fichier MP3 avec le lecteur de MP3 par défaut de Windows.

threading :

Pour exécuter l'enregistrement audio dans un thread séparé et éviter de bloquer l'interface graphique.

os :

Pour vérifier l'existence du fichier MP3 avant de le lire.

time :

Pour ajouter un délai avant de jouer le fichier audio (optionnel).

Installation des Librairies
Pour exécuter ce script, vous devez installer les librairies suivantes :

bash
Copy
pip install numpy sounddevice scipy pydub pillow
Structure du Script
Initialisation de l'interface graphique :

Crée une fenêtre Tkinter avec un fond noir.

Affiche un logo à gauche de l'interface.

Ajoute un menu déroulant pour sélectionner la source audio.

Boutons :

Bouton d'enregistrement (●) : Démarre l'enregistrement audio.

Bouton d'arrêt (■) : Arrête l'enregistrement audio.

Bouton de lecture (▶) : Ouvre le fichier MP3 avec le lecteur de Windows.

Enregistrement audio :

Capture le flux audio système en temps réel.

Sauvegarde les données dans un fichier WAV et le convertit en MP3.

Lecture du fichier audio :

Utilise subprocess pour ouvrir le fichier MP3 avec le lecteur par défaut de Windows.

Résultat Attendu
Une interface graphique simple avec un logo, un menu de sélection de source audio, et trois boutons (enregistrement, arrêt, lecture).

L'audio système est enregistré dans un fichier WAV, converti en MP3, et peut être lu avec le lecteur de MP3 de Windows.
