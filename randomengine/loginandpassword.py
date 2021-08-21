import random
from time import time


class Transliter():

    _WORDS = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'E', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'CSH', 'Ъ': '', 'Ы': 'I', 'Ь': '',
        'Э': 'E', 'Ю': 'U', 'Я': 'Y',
    }

    def _eng(self, text: str) -> str:
        return self._translit_eng(text)

    @classmethod
    def _translit_eng(cls, text: str) -> str:
        new_string = ''
        for char in text:
            new_string += cls._WORDS[char.upper()]
        new_string.lower()
        return new_string.capitalize()


class DataAuth():

    _SYMBOLS = ('!', '@', '$', '%', '_', '*', '+', '-', '~', '.')

    @staticmethod
    def username(text: str) -> str:
        username = Transliter()._eng(text) + str(time())[5:10]
        return  username + str(random.randrange(123, 999))

    @classmethod
    def password(cls, text: str) -> str:
        password = Transliter()._eng(text) + str(random.randrange(123456, 999999))
        return password + random.choice(cls._SYMBOLS)
