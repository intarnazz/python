import pygame
import sys

class StartScreen():
    """ ЭКРАН ГЛАВНОГО МЕНЮ """
    def __init__(self, screen, form, screen_width, screen_height) -> None:
        """ ИНИЦИАЛИЗАЦИЯ """
        pygame.init()
        self.form = form 
        # 'form' припас для маштобирования, пока не использовал (и не буду использовать)
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.settings_menu = False

        #============================
        #print(pygame.font.get_fonts()) 
        # СПИСОК ШРИФТОВ
        #============================

        #===================================================================
        #===================================================================
        self.font = pygame.font.SysFont('cambria', int(self.screen_height/43.2)) # ШРИФТ ГЛАВНОГО МЕНЮ
        #===================================================================

        #////////////////////// ТЕКСТ КНОПОК ////////////////////////////////
        #======= New game ====================================
        NewGame = "New game"
        self.NewGame_image = self.font.render(NewGame, True,
            (255, 255, 255), None
            )
        self.NewGame_rect = self.NewGame_image.get_rect()
        self.NewGame_rect.center = self.screen_rect.center
        #print(self.screen_height/1,6875)
        self.NewGame_rect.y = int(self.screen_height/1.6875) #640
        #======= //New game// ====================================
        #======= Quit game ====================================
        NewGame = "Quit game"
        self.QuitGame_image = self.font.render(NewGame, True,
            (255, 255, 255), None
            )
        self.QuitGame_rect = self.QuitGame_image.get_rect()
        self.QuitGame_rect.center = self.screen_rect.center
        self.QuitGame_rect.y = int(self.screen_height/1.421) #760
        #======= //Quit game// ====================================
        #======= Settings ====================================
        NewGame = "Settings"
        self.Settings_image = self.font.render(NewGame, True,
            (255, 255, 255), None
            )
        self.Settings_rect = self.Settings_image.get_rect()
        self.Settings_rect.center = self.screen_rect.center
        self.Settings_rect.y = int(self.screen_height/1.5428571) #700
        #======= //Settings// ====================================
        #======= Settings menu ====================================
        NewGame = "Settings"
        self.Settings_image_menu = self.font.render(NewGame, True,
            (255, 255, 255), None
            )
        self.Settings_rect_menu = self.Settings_image_menu.get_rect()

        self.Settings_rect_menu.center = self.screen_rect.center
        self.Settings_rect_menu.y = 446 #!!!
        #======= //Settings menu// ====================================
        #////////////////////// ТЕКСТ КНОПОК ////////////////////////////////
        #========== BGменю настроек ===========================================================
        self.image_settings_menu = pygame.image.load('img\\1920_1080\\menu.png')
        self.image_settings_menu = pygame.transform.scale(self.image_settings_menu,
            (987*(self.screen_width/1920), 607*(self.screen_height/1080))
        )

        self.rect_settings_menu = self.image_settings_menu.get_rect()
        self.rect_settings_menu.center = self.screen_rect.center
        self.rect_settings_menu.y = 417 #!!!
        #========== //BGменю настроек// ===========================================================
        #========== линия ===========================================================
        self.image_line = pygame.image.load('img\\1920_1080\\line.png')
        self.image_line = pygame.transform.scale(self.image_line,
            (552*(self.screen_width/1920), 2*(self.screen_height/1080))
        )

        self.rect_line = self.image_line.get_rect()
        self.rect_line.center = self.screen_rect.center
        self.rect_line.y = 502 #!!!
        #========== //линия// ===========================================================
        #========== BG - это фоновая картинка ===========================================================
        self.image_main_menu = pygame.image.load('img\\1920_1080\\main_memu0.png')
        self.image_main_menu = pygame.transform.scale(self.image_main_menu,
            (self.screen_width, self.screen_height)
            )

        self.rect_main_menu = self.image_main_menu.get_rect()
        #========== //BG// ===========================================================

        # ============================================================
        # В СЛОВАРЕ ДОЛЖНЫ РАСПОЛОГАТЬСЯ ВСЕ КНОПКИ ГЛАВНОГО МЕНЮ
        triger_plus = int(self.screen_height/30) #36
        self.menu_nutton = [
            self.NewGame_rect.y - triger_plus,
            self.Settings_rect.y - triger_plus,
            self.QuitGame_rect.y - triger_plus
        ]# В СЛОВАРЕ ДОЛЖНЫ РАСПОЛОГАТЬСЯ ВСЕ КНОПКИ ГЛАВНОГО МЕНЮ
        # ============================================================


        self.n = 0 # id скнопки в списке
        #========== TRIGER ===========================================================
        self.image_menu_triger = pygame.image.load('img\\1920_1080\\menu_triger.png')
        self.image_menu_triger = pygame.transform.scale(self.image_menu_triger,
            (463*(self.screen_width/1920), 115*(self.screen_height/1080))
            )

        self.rect_menu_triger = self.image_menu_triger.get_rect()
        self.rect_menu_triger.center = self.screen_rect.center
        self.rect_menu_triger.y = self.menu_nutton[self.n]   #604
        #========== //TRIGER// ===========================================================
    
    def menu_event(self):
        """ СОБЫТИЯ КНОПОК ГЛАВНОГО МЕНЮ """
        if self.n == len(self.menu_nutton) - 1:
            sys.exit() # ВЫХОД
        if self.n == len(self.menu_nutton) - 2:
            self.settings_menu = True

    def update(self, num):
        """ обновление положения тригера """
        if num == 1:
            if self.n == 0:
                self.n = len(self.menu_nutton) - 1 
                self.rect_menu_triger.y = self.menu_nutton[self.n]
            else:
                self.n = self.n - 1
                self.rect_menu_triger.y = self.menu_nutton[self.n]
        elif num == -1:
            if self.n >= len(self.menu_nutton) - 1:
                self.n = 0
                self.rect_menu_triger.y = self.menu_nutton[self.n]
            else:
                self.n = self.n + 1
                self.rect_menu_triger.y = self.menu_nutton[self.n]

    def main_screen(self):
        """ ОТРЕСОВКА ТЕКСТА КНОПОК И ОТОБРАЖЕНИЕ ТРИГЕРА НА ЭКРАНЕ """
        self.screen.blit(self.image_main_menu, self.rect_main_menu)
        self.screen.blit(self.image_menu_triger, self.rect_menu_triger)
        self.screen.blit(self.NewGame_image, self.NewGame_rect)
        self.screen.blit(self.Settings_image, self.Settings_rect)
        self.screen.blit(self.QuitGame_image, self.QuitGame_rect)
        if self.settings_menu == True:
            self.screen.blit(self.image_settings_menu, self.rect_settings_menu)
            self.screen.blit(self.image_line, self.rect_line)
            self.screen.blit(self.Settings_image_menu, self.Settings_rect_menu)

