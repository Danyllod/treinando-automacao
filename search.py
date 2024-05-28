import pyautogui
import time

# Espera 5 segundos para que você possa mover o mouse para a posição desejada
print("Você tem 5 segundos para posicionar o mouse sobre o primeiro botão...")
time.sleep(5)

# Captura e imprime a posição atual do mouse
print("Posição do primeiro botão:", pyautogui.position())

# Espera 5 segundos para que você possa mover o mouse para a próxima posição desejada
print("Você tem 5 segundos para posicionar o mouse sobre o segundo botão...")
time.sleep(5)

# Captura e imprime a posição atual do mouse
print("Posição do segundo botão:", pyautogui.position())

# Repita conforme necessário para todos os botões que você deseja automatizar
