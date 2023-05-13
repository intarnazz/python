import json

class Dictionary():
    def __init__(self) -> None:
        english = {
            'New game':'New game',
            "Quit game":"Quit game",
            "Settings":"Settings",
            "Language":"Language",
            "Screen resolution":"Screen resolution",
            "Sound":"Sound",
        }
        with open('dictionary-english.json', 'w') as f:
            json.dump(english, f)

        rus = {
            'New game':'Новая игра',
            "Quit game":"Выход из игры",
            "Settings":"Настройки",
            "Language":"Язык",
            "Screen resolution":"Расширение экрана",
            "Sound":"Звук",
        }
        with open('dictionary-rus.json', 'w') as f:
            json.dump(rus, f)

