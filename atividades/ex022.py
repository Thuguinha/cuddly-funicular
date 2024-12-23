import pygame

# Iniciar programa
pygame.mixer.init()

# Carregar o arquivo (mp3)
pygame.mixer.music.load('corinthians-radio-globo.mp3')

# Reproduzir a musica 
pygame.mixer.music.play()

# deixar a musica em loop
while pygame.mixer.music.get_busy():
     pygame.time.Clock().tick(10)