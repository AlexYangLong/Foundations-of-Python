
class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def balance(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary=12000):
        """
        初始化方法
        :param salary: 基本薪资
        """
        super().__init__(name, salary)

    def balance(self):
        """求本月薪水"""
        return self.salary


class Saler(Employee):
    def __init__(self, name, sales_amount, base_pay=1200):
        """
        初始化方法
        :param base_pay: 底薪
        :param sales_amount: 销售额
        """
        super().__init__(name, base_pay)
        self.sales_amount = sales_amount

    def balance(self):
        """求本月月薪"""
        return self.salary + self.sales_amount * 0.05


class Programmer(Employee):
    def __init__(self, name, hour, hourly_wage=150):
        """
        初始化方法
        :param hour: 工作时长
        :param hourly_wage: 每小时薪资
        """
        super().__init__(name, hourly_wage)
        self.hour = hour

    def balance(self):
        """求本月月薪"""
        return self.salary * self.hour


def show_salary(emp_list):
    for emp in emp_list:
        print(emp.balance())


def main():
    emp_list = []
    manager = Manager('经理', 12000)
    emp_list.append(manager)

    saler = Saler('销售员', 1000000, 1200)
    emp_list.append(saler)

    programmer = Programmer('程序员', 108, 150)
    emp_list.append(programmer)

    show_salary(emp_list)


if __name__ == '__main__':
    main()