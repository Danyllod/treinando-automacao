import pyautogui
import time
import keyboard

# Lista de caminhos das imagens dos botões
button_images = ["botao.png","vender.png","vender2.png","sim.png","repeat.png"]

# Tempo de espera antes de começar a clicar (para permitir que você mude para a janela correta)
time.sleep(3)

# Iterar pelas imagens e clicar em cada botão
def find_and_click_button(image):
    try:
        # Localiza o centro da imagem na tela com uma confiança de 0.8
        button_location = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        if button_location is not None:
            pyautogui.moveTo(button_location)
            pyautogui.click()
            return True  # Retorna True se o botão foi encontrado e clicado
        else:
            return False  # Retorna False se o botão não foi encontrado
    except Exception as e:
        print(f"Erro ao tentar localizar a imagem {image}: {e}")
        return False

# Tempo de espera antes de começar a clicar (para permitir que você mude para a janela correta)
time.sleep(3)
button_stop = False
while not button_stop:
    for image in button_images:
        time.sleep(3)
        button_found = False
        while not button_found:
            button_found = find_and_click_button(image)
            if not button_found:
                print(f"Botão com a imagem {image} não encontrado. Tentando novamente...")
                time.sleep(15)  # Espera um segundo antes de tentar novamente
            
        if image == "botao.png":
            time.sleep(80)   
    if keyboard.is_pressed('s'):
        break        
        
print("Sequência de cliques concluída.")