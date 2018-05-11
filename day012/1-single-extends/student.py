from person import Person

class Student(Person):
    def __init__(self, name, age, height, money, stuId):
        super().__init__(name, age, height, money)
        self.stuId = stuId

    def love(self):
        print('我在大学一场恋爱都没谈过,好后悔呀~~~~~')