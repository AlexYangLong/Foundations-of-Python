from person import Person

class Teacher(Person):
    def __init__(self, name, age, height, money, course):
        # super().父类的方法(参数列表)  调用父类中的方法
        super().__init__(name, age, height, money)
        self.__course = course

    def teach(self):
        print(self.__course)