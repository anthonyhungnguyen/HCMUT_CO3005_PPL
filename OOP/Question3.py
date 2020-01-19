from dataclasses import dataclass
from abc import ABC


class Expr(ABC):
    pass


@dataclass
class Number(Expr):
    number: float

    def print(self):
        print(self.number)


@dataclass
class Var(Expr):
    name: str


@dataclass
class UpOp(Expr):
    operator: str
    arg: Expr


@dataclass
class BinOp(Expr):
    operator: str
    left: Expr
    right: Expr

    def eval(self):
        if (isinstance(self.left, Var)):
            self.left = Number(1)
        if (isinstance(self.right, Var)):
            self.right = Number(1)

        if (isinstance(self.left, BinOp)):
            self.left = Number(self.left.eval().number)
        if (isinstance(self.right, BinOp)):
            self.right = Number(self.right.eval().number)

        if self.operator == "+":
            sum_op = self.left.number + self.right.number
            return Number(round(sum_op, 2))
        if self.operator == "-":
            sub_op = self.left.number - self.right.number
            return Number(round(sub_op, 2))
        if self.operator == "*":
            mul_op = self.left.number * self.right.number
            return Number(round(mul_op, 2))
        if self.operator == "/":
            div_op = self.left.number / self.right.number
            return Number(round(div_op, 2))


# b
x_var = Var("X")
inner = BinOp("+", x_var, Number(0.2))
t = BinOp("*", inner, Number(3))

# c
t.eval().print()
