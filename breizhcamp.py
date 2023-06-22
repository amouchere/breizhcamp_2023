import vlc
import random
import os
import threading
from gpiozero import MotionSensor
from gpiozero import Button
from gpiozero import LED
from time import sleep

# queue_len : https://gpiozero.readthedocs.io/en/stable/api_input.html?highlight=wait_for_motion#motionsensor-d-sun-pir
pir = MotionSensor(4, queue_len=10)

ready_button = Button(17)
manual_grooar_button = Button(12)

# Chemin vers le répertoire contenant les fichiers son
tracks_directory = "/home/pi/breizhcamp_2023/tracks"

# Obtention des chemins absolus de tous les fichiers .wav dans le répertoire
tracks = [os.path.join(tracks_directory, f) for f in os.listdir(tracks_directory) if f.endswith('.wav')]

# Log pour lister les fichiers audio trouvés
print("Tracks disponibles :", tracks)
print("")

# Création de l'objet lecteur VLC
vlc_instance = vlc.Instance()
media_player = vlc_instance.media_player_new()

# Création d'une variable de contrôle pour sortir de la boucle LED
led_running = False

def led_thread():
    red = LED(21)
    yellow = LED(20)
    while True:
        try:
            if (led_running):
                red.on()
                yellow.off()
                sleep(1)
                red.off()
                yellow.on()
                sleep(1)
            else:
                red.off()
                yellow.off()
        except KeyboardInterrupt:
            break

def manual_grooar_thread():
    print('manual_grooar_thread démarré ...')
    while True:
        try:
            manual_grooar_button.wait_for_press()
            print('Lancement manuel')
            trex_groaaar_sound()
        except KeyboardInterrupt:
            break

led_thread = threading.Thread(target=led_thread)
manual_grooar_thread = threading.Thread(target=manual_grooar_thread)
# Lancement du thread
led_thread.start()
manual_grooar_thread.start()

# fonction de test
def trex_groaaar():
    print('GrOoOoAAArRR')

def trex_groaaar_sound():
    # Choix d'un fichier son au hasard
        track_to_play = random.choice(tracks)
        print("chargement du track: " + track_to_play)
        
        # Chargement du fichier son et récupération de la durée
        media = vlc_instance.media_new(track_to_play)
        media.parse()
        duration = int(media.get_duration() / 1000)  # durée en secondes
        
        # Lecture du fichier son
        media_player.set_media(media)
        media_player.play()
        sleep(duration)
        
        # Arrêt de la lecture
        media_player.stop()
        print("Arret du média")

try:
    while True:
        print('Reaaaady ?')
        ready_button.wait_for_press()
        print('Go')
        led_running = True
        print("Sleep 5 sec")
        sleep(5)
        print("En attente de mouvement ...")
        pir.wait_for_motion()
        # trex_groaaar()
        led_running = False
        trex_groaaar_sound()
        sleep(2)
except KeyboardInterrupt:
    print("Interruption")
