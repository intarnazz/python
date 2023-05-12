import pygame

class Media():
    """ ПОДКЛЮЧЕНИЕ ЗВУКОВЫХ КАНАЛОВ """
    def __init__(self) -> None:
        pygame.mixer.init()

        pygame.mixer.Channel(0).play(pygame.mixer.Sound('mp\main-menu.mp3'), loops=-1)
        # ОСНОВНАЯ ТЕМА
        #pygame.mixer.Channel(1).play(pygame.mixer.Sound('other\DAGOTHWAVE.mp3'))
    
    def cursor_move(self):
        """ ЗВУК ПЕРЕКЛЮЧЕНИЯ ЧЕГО-ЛИБО """
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('mp\CURSOL_MOVE.wav.mp3'))
