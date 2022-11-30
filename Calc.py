import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import math


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.res = ''
        self.expression = ''
        self.lineEdit_res = None
        self.lineEdit_ex = None
        self.pushButton_eq = None
        self.pushButton_cl = None
        self.pushButton_plus = None
        self.pushButton_min = None
        self.pushButton_mult = None
        self.pushButton_div = None
        self.pushButton_point = None
        self.pushButton_fact = None
        self.pushButton_ch = None
        self.pushButton_deg = None
        self.pushButton_module = None
        self.pushButton_back = None
        self.pushButton_rd = None
        self.pushButton_sq = None
        self.pushButton_rev = None
        self.pushButton_two = None
        self.pushButton_ten = None
        self.pushButton_round = None
        self.buttonGroup = None
        self.pushButton_br1 = None
        self.pushButton_br2 = None
        self.plussing = False
        self.minning = False
        self.multing = False
        self.diving = False
        uic.loadUi('Calculator.ui', self)
        self.pushButton_eq.clicked.connect(self.eq)
        self.pushButton_cl.clicked.connect(self.clear)
        self.pushButton_plus.clicked.connect(self.plus)
        self.pushButton_min.clicked.connect(self.min)
        self.pushButton_mult.clicked.connect(self.mult)
        self.pushButton_div.clicked.connect(self.div)
        self.pushButton_point.clicked.connect(self.point)
        self.pushButton_fact.clicked.connect(self.fact)
        self.pushButton_ch.clicked.connect(self.change)
        self.pushButton_deg.clicked.connect(self.deg)
        self.pushButton_module.clicked.connect(self.module)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_rd.clicked.connect(self.rd)
        self.pushButton_sq.clicked.connect(self.sq)
        self.pushButton_rev.clicked.connect(self.rev)
        self.pushButton_two.clicked.connect(self.two)
        self.pushButton_ten.clicked.connect(self.ten)
        self.pushButton_round.clicked.connect(self.round)
        [i.clicked.connect(self.brackets) for i in self.buttonGroup_br.buttons()]
        [i.clicked.connect(self.run) for i in self.buttonGroup.buttons()]

    def eq(self):
        """Выводит на экран значение"""
        if self.expression != '':
            self.res = str(eval(self.expression))
            self.lineEdit_res.setText(self.res)
            self.lineEdit_ex.setText(self.res)
            self.expression = self.res
            self.res = '0'

    def clear(self):
        """Очищает экран"""
        self.res = ''
        self.expression = ''
        self.lineEdit_res.setText('')
        self.lineEdit_ex.setText('')

    def restore(self, el):
        """Определение одной из простых операций"""
        self.plussing = el == '+'
        self.minning = el == '-'
        self.multing = el == '*'
        self.diving = el == '/'

    def run(self):
        """добавление цифр"""
        self.expression += str(self.sender().text())
        self.lineEdit_ex.setText(self.expression)
        if self.brackets():
            if self.plussing:
                self.lineEdit_res.setText(str(eval(self.expression)))
            if self.minning:
                self.lineEdit_res.setText(str(eval(self.expression)))
            if self.multing:
                self.lineEdit_res.setText(str(eval(self.expression)))
            if self.diving:
                self.lineEdit_res.setText(str(eval(self.expression)))

    def brackets(self):
        """проверка скобок"""
        if self.sender().text() == '(' or self.sender().text() == ')':
            self.expression += str(self.sender().text())
        self.lineEdit_ex.setText(self.expression)
        c = 0
        s = "".join(filter(lambda x: x in ("(", ")"), self.expression))
        for i in s:
            if i == '(':
                c += 1
            else:
                c -= 1
            if c < 0:
                return False
        return not c

    def plus(self):
        """функция сложения"""
        if self.expression[-1] != '*' and self.expression[-1] != '/':
            self.expression += '+'
            self.plussing = True
            self.restore('+')

    def min(self):
        """функция вычитания"""
        if self.expression[-1] != '*' and self.expression[-1] != '/':
            self.expression += '-'
            self.minning = True
            self.restore('-')

    def mult(self):
        """функция умножения"""
        if self.expression[-2:] != '//' and (self.expression[-1] != '/' and self.expression[-1] != '+' and
                                             self.expression[-1] != '-'):
            self.expression += '*'
            self.multing = True
            self.restore('*')

    def div(self):
        """функция деления"""
        if self.expression[-2:] != '//' and (self.expression[-1] != '*' and self.expression[-1] != '+' and
                                             self.expression[-1] != '-'):
            self.expression += '/'
            self.diving = True
            self.restore('/')

    def ispoint(self):
        """Проверка на то, можно ли ставить точку"""
        expression = self.expression
        res = ''
        if '.' in self.expression:
            while expression[-1] != '.':
               res += expression[-1]
               expression = expression[:-1]
            if res.isdigit():
                return False
            else:
                return True
        else:
            return True

    def point(self):
        """функция поставления точки"""
        if self.expression != '' and self.ispoint() and self.expression[-1] != ')' and self.expression[-1] != '(':
            self.expression += '.'

    def fact(self):
        """функция факториал"""
        self.expression = str(math.factorial(math.trunc(eval(self.expression))))

    def change(self):
        """функция изменения знака числа"""
        if eval(self.expression) != 0 and self.expression != '':
            self.expression = str(eval(self.expression) * (-1))

    def module(self):
        """функция модуль"""
        self.expression = str(abs(eval(self.expression)))

    def back(self):
        """функция очищения последнего знака"""
        if len(self.expression) > 0:
            self.expression = self.expression[:-1]
            self.lineEdit_ex.setText(self.expression)

    def rd(self):
        """функция квадратного корня"""
        if eval(self.expression) >= 0:
            self.expression = str(eval(self.expression) ** (1 / 2))

    def rev(self):
        """нахождение обратного числа"""
        if self.expression != '':
            self.expression = '1/' + self.expression

    def sq(self):
        """возведение в квадрат"""
        if eval(self.expression) != '':
            self.expression = str(eval(self.expression) ** 2)

    def two(self):
        """нахождение степени числа 2"""
        if self.expression != '':
            self.expression = '2**' + self.expression

    def ten(self):
        """нахождение степени числа 10"""
        if self.expression != '':
            self.expression = str(10 ** eval(self.expression))

    def deg(self):
        """функция степени"""
        self.expression += '**'
        x, y = self.expression.split('**', maxsplit=True)
        if y:
            self.expression = str(eval(x) ** eval(y))

    def round(self):
        """функция округления числа до целого"""
        self.expression = str(math.trunc(eval(self.expression)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
