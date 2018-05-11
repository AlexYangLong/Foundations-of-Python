from abc import abstractmethod, ABCMeta

# 面向对象三大特性：封装、继承、多态
# 封装：隐藏复杂的实现细节，暴露简单的调用接口
# 继承：从已有的类创建新类的过程，提供继承信息的称为父类（超类、基类），得到继承信息的叫子类（派生类）
# 多态：同样的引用调同样的方法，给出不同的信息（同一种的行为的不同表现形式）


class Employee(object, metaclass=ABCMeta):
    """抽象类：通过声明 metaclass=ABCMeta 将一个类变成抽象类，抽象类不能实例化对象，只能让子类取继承"""
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name[:-1] + '*'

    @abstractmethod
    def get_salary(self):
        """抽象方法：被 @abstractmethod 包装器修饰的方法就是抽象方法，不用实现，留给子类去重写"""
        pass


class Manager(Employee):

    def __init__(self, name):
        super().__init__(name)

    # @name.setter
    # def name(self, name):
    #     self._name = name

    def get_salary(self):
        return 12000


class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)
        self._work_hour = 0

    @property
    def work_hour(self):
        return self._work_hour

    @work_hour.setter
    def work_hour(self, hour):
        self._work_hour = hour if hour > 0 else 0

    def get_salary(self):
        return 150 * self._work_hour


class Salesmen(Employee):
    def __init__(self, name):
        super().__init__(name)
        self._sales = 0

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1500 + self._sales * 0.05


def main():
    emp_list = [Manager('Alex'), Programmer('Simon'), Programmer('Ada'), Salesmen('Adam'), Salesmen('Catherine')]
    for emp in emp_list:
        if isinstance(emp, Programmer):
            hour = int(input('请输入 %s 本月的工作时长：' % emp.name))
            emp.work_hour = hour
        elif isinstance(emp, Salesmen):
            sales = int(input('请输入 %s 本月的销售总额：' % emp.name))
            emp.sales = sales
        print('%s 本月的月薪为：￥ %.2f' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
