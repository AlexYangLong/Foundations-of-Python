class Person(object):
    def __init__(self, name, age, height, money):
        self.name = name
        self._age = age
        self.__height = height
        self.__money = money

    def set_money(self, money):
        self.__money = money
        return self.__money

    def get_money(self):
        return self.__money

    def run(self):
        return '人都会跑.........'