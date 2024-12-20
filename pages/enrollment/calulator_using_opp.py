class Calculator:
    a = 0
    b = 0

    def __init__(self, value1, value2):
        self.a = value1
        self.b = value2

    def addition(self, x, y):
        sum = x + y
        print(sum)

    def substraction(self, m, n):
        sub = m - n
        print(sub)


if __name__ == '__main__':
    calc_sum = Calculator(value1=10, value2=5)
    calc_sub = Calculator(value1=20, value2=10)
    calc_sum.addition(x=calc_sum.a, y=calc_sum.b)
    calc_sub.substraction(m=calc_sub.a, n=calc_sub.b)
