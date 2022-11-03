import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy
import math


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.res = '0'
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
        self.pushButton_p = None
        self.pushButton_rd = None
        self.pushButton_sq = None
        self.pushButton_rev = None
        self.pushButton_two = None
        self.pushButton_ten = None
        self.pushButton_mod = None
        self.pushButton_sin = None
        self.pushButton_cos = None
        self.pushButton_tg = None
        self.pushButton_ctg = None
        self.pushButton_trunc = None
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
        self.pushButton_p.clicked.connect(self.p)
        self.pushButton_rd.clicked.connect(self.rd)
        self.pushButton_sq.clicked.connect(self.sq)
        self.pushButton_rev.clicked.connect(self.rev)
        self.pushButton_two.clicked.connect(self.two)
        self.pushButton_ten.clicked.connect(self.ten)
        self.pushButton_mod.clicked.connect(self.mod)
        self.pushButton_sin.clicked.connect(self.sin)
        self.pushButton_cos.clicked.connect(self.cos)
        self.pushButton_tg.clicked.connect(self.tg)
        self.pushButton_ctg.clicked.connect(self.ctg)
        self.pushButton_trunc.clicked.connect(self.trunc)
        [i.clicked.connect(self.brackets) for i in self.buttonGroup_br.buttons()]
        [i.clicked.connect(self.run) for i in self.buttonGroup.buttons()]

    def eq(self):
        self.res = str(eval(self.expression))
        self.lineEdit_res.setText(self.res)
        self.res = '0'

    def clear(self):
        self.res = '0'
        self.expression = ''
        self.lineEdit_res.setText("0")
        self.lineEdit_ex.setText('0')

    def restore(self, el):
        self.plussing = el == '+'
        self.minning = el == '-'
        self.multing = el == '*'
        self.diving = el == '/'

    def run(self):
        self.expression += str(self.sender().text())
        self.lineEdit_ex.setText(self.expression)
        if self.plussing and self.brackets():
            self.lineEdit_res.setText(str(eval(self.expression)))
        if self.minning and self.brackets():
            self.lineEdit_res.setText(str(eval(self.expression)))
        if self.multing and self.brackets():
            self.lineEdit_res.setText(str(eval(self.expression)))
        if self.diving and self.brackets():
            self.lineEdit_res.setText(str(eval(self.expression)))

    def brackets(self):
        if self.sender().text() == '(' or self.sender().text() == ')':
            self.expression += str(self.sender().text())
        self.lineEdit_ex.setText(self.expression)
        c = 0
        s = "".join(filter(lambda i: i in ("(", ")"), self.expression))
        for i in s:
            if i == '(':
                c += 1
            else:
                c -= 1
            if c < 0:
                return False
        return not c

    def plus(self):
        self.expression += '+'
        self.plussing = True
        self.restore('+')

    def min(self):
        self.expression += '-'
        self.minning = True
        self.restore('-')

    def mult(self):
        self.expression += '*'
        self.multing = True
        self.restore('*')

    def div(self):
        self.expression += '/'
        self.diving = True
        self.restore('/')

    def point(self):
        if '.' not in self.expression and self.expression:
            self.expression += '.'

    def fact(self):
        self.expression = str(math.factorial(math.trunc(eval(self.expression))))

    def change(self):
        self.expression = str(-eval(self.expression))

    def module(self):
        self.expression = str(abs(eval(self.expression)))

    def p(self):
        if self.expression == '0.0':
            self.expression = str(numpy.pi)
        else:
            self.expression = str(eval(str(self.expression)) * numpy.pi)

    def rd(self):
        self.expression = str(eval(self.expression) ** (1 / 2))

    def rev(self):
        self.expression = str(1 / eval(self.expression))

    def sq(self):
        self.expression = str(eval(self.expression) ** 2)

    def two(self):
        self.expression = str(2 ** eval(self.expression))

    def ten(self):
        self.expression = str(10 ** eval(self.expression))

    def deg(self):
        self.expression += '^'
        x, y = self.expression.split('^')
        if y:
            self.expression = str(eval(x) ** eval(y))

    def mod(self):
        self.expression += '≡'
        x, y = self.expression.split('≡')
        self.expression = str(math.fmod(math.trunc(eval(x)), math.trunc(eval(y))))

    def sin(self):
        pass

    def cos(self):
        pass

    def tg(self):
        pass

    def ctg(self):
        pass

    def trunc(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
