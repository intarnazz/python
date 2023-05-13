import json

class Settings():
    """ НАСТОЙКИ """
    def __init__(self):
        """ НАСТОЙКИ """
        with open('main-dictionary.txt') as md:
            file = md.read()

        with open(file) as f:
            self.main_dictionary = json.load(f)

        self.screen_width = 1920
        self.screen_height = 1080

        self.bgcolor = (0,0,0)

        self.form = 1