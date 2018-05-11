class Student(object):
    def __init__(self, value):
        self.__score = value

    @property
    def get_score(self):
        return self.__score

s1 = Student(20)
print(s1.get_score)