from src.item import Item


class MixinLang:
    lang = 'EN'

    def __init__(self):
        self.__language = self.lang

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        elif self.language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLang):
    pass
