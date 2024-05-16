class ArithmeticOperator:
    def _init_(self, a, b):
        self.a = a
        self.b = b

    def sum(self, a, b):
        print(a + b)

    def substraction(self, a, b):
        print(a - b)

    def multi(self, a, b):
        print(a * b)

    def division(self, a, b):
        try:
          print(print(a/b) )
        except :
        print(a / b)


obj = ArithmeticOperator()
obj.sum(2, 5)
obj.substraction(9, 6)
obj.division(9, 6)
obj.multi(3, 6)