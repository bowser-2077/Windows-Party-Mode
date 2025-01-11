import os
import sys
import subprocess
import urllib.request
import shutil
import pyautogui
import pygame
import random
import time
from threading import Thread

# URL du fichier son
Sound_URL = "https://www.dropbox.com/scl/fi/7njdtwjr6zeoqwsv3a527/son.mp3?rlkey=kdj9vpdimvvdep8p6xtwez0ga&st=oakwmmb5&dl=1"

# Créer un dossier temporaire dans %temp%
TEMP_DIR = os.path.join(os.getenv("TEMP"), "psychedelic_virus")
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

# Télécharger le son
SON_PATH = os.path.join(TEMP_DIR, "son.mp3")
if not os.path.exists(SON_PATH):
    print("Téléchargement du fichier audio...")
    urllib.request.urlretrieve(SON_URL, SON_PATH)

# Installer les dépendances dans le dossier temporaire
def install_dependencies():
    print("Installation des dépendances...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--target", TEMP_DIR, "pygame", "pyautogui"
    ])
    sys.path.append(TEMP_DIR)  # Ajouter les modules installés localement au chemin Python

try:
    import pyautogui
    import pygame
except ImportError:
    install_dependencies()
    import pyautogui
    import pygame

# Initialisation de Pygame pour l'audio
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(SON_PATH)
pygame.mixer.music.play(-1)  # Boucle infinie

# Fonction pour animer le curseur
def animate_cursor():
    screen_width, screen_height = pyautogui.size()
    while True:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=0.2)

# Fonction pour simuler un zoom/dézoom de fenêtres
def zoom_effect():
    for _ in range(10):
        pyautogui.hotkey('ctrl', '+')  # Zoom avant
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', '-')  # Zoom arrière
        time.sleep(0.5)

# Fonction pour créer une animation psychédélique
def psychedelic_effect():
    screen_width, screen_height = pyautogui.size()
    pygame.display.set_caption("Psychédélique Mode")
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Couleur aléatoire
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        screen.fill(color)
        pygame.display.flip()
        clock.tick(10)  # Limiter les FPS pour éviter un usage excessif du CPU

    pygame.quit()

# Lancer les animations dans des threads séparés
cursor_thread = Thread(target=animate_cursor, daemon=True)
cursor_thread.start()

zoom_thread = Thread(target=zoom_effect, daemon=True)
zoom_thread.start()

psychedelic_effect()
