"""
 * @author nhphung
"""
# 1752259
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType)),
        Symbol("putIntLn", MType([IntType], VoidType)),
        Symbol("putInt", MType([IntType], VoidType)),
        Symbol("getFloat", MType([], FloatType)),
        Symbol("putFloat", MType([FloatType], VoidType)),
        Symbol("putFloatLn", MType([FloatType], VoidType)),
        Symbol("putBool", MType([BoolType], VoidType)),
        Symbol("putBoolLn", MType([BoolType], VoidType)),
        Symbol("putString", MType([StringType], VoidType)),
        Symbol("putStringLn", MType([StringType], VoidType)),
        Symbol("putLn", MType([], VoidType))
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def flattenC(self, c):
        final = []
        for x in c:
            if type(x) is list:
                for i in x:
                    final.append(i)
            else:
                final.append(x)
        return final

    def getFunctionInC(self, c, name):
        for x in c:
            if type(x) is dict and x['func'].name == name:
                return x

    def getVariableInC(self, c, name):
        for x in c:
            if (type(x) is Symbol and x.name == name) or (type(x) is dict and x['func'].name == name):
                return x

    def getCurrentFunc(self, c):
        return self.getFunctionInC(c[-1], list(
            filter(lambda x: type(x) is str, self.flattenC(c)))[0])

    def visitProgram(self, ast, c):
        l = [{'func': x, 'isReturn': True, 'isCalled': True} for x in c]
        for x in ast.decl:
            l.insert(0, self.visit(x, l))
        # check no entry
        if not self.getFunctionInC(l, 'main'):
            raise NoEntryPoint()
        l = [l]
        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, l)

        # check func not return
        check_func_not_return = list(filter(lambda x: type(
            x) is dict and x['isReturn'] == False, self.flattenC(l)))
        if check_func_not_return:
            raise FunctionNotReturn(check_func_not_return[0]['func'].name)

        # Check unreachable
        check_func_unreachable = list(filter(lambda x: type(
            x) is dict and x['func'].name != 'main' and x['isCalled'] == False, self.flattenC(l)))

        if check_func_unreachable:
            raise UnreachableFunction(check_func_unreachable[0]['func'].name)

        return l

    def visitVarDecl(self, ast, c):
        if self.getVariableInC(c, ast.variable):
            raise Redeclared(Variable(), ast.variable)
        return Symbol(ast.variable, self.visit(ast.varType, c))

    def visitFuncDecl(self, ast, c):
        pr = []
        pr = [self.visit(x, pr) for x in ast.param]
        pr_type = [x.mtype for x in pr]
        return_type = self.visit(ast.returnType, c)
        if type(c[0]) is not list:
            if self.getVariableInC(c, ast.name.name):
                raise Redeclared(Function(), ast.name.name)
            return {'func': Symbol(ast.name.name, MType(pr_type, return_type)), 'isReturn': False, 'isCalled': False} if return_type is not VoidType else {'func': Symbol(ast.name.name, MType(pr_type, return_type)), 'isReturn': True, 'isCalled': False}
        else:
            c.insert(0, [])
            for x in ast.param:
                try:
                    c[0].insert(0, self.visit(x, c[0]))
                except Redeclared as e:
                    raise Redeclared(Parameter(), e.n)
        # Insert rettype to check inside if return type is correct
        # Insert function name
        c[0].insert(0, self.getFunctionInC(
            c[-1], ast.name.name)['func'].mtype.rettype)
        c[0].insert(0, ast.name.name)

        for x in ast.body.member:
            if type(x) is VarDecl:
                c[0].insert(0, self.visit(x, c[0]))
            else:
                self.visit(x, c)
        c.pop(0)

    def visitId(self, ast, c):
        filter_l = list(filter(lambda x: type(x) is Symbol or type(x)
                               is dict, self.flattenC(c)))
        exist = self.getVariableInC(filter_l, ast.name)
        if not exist:
            raise Undeclared(Identifier(), ast.name)
        else:
            if type(exist) is dict:
                return exist['func'].mtype
            else:
                return exist.mtype

    def visitIf(self, ast, c):
        l = False
        exp_type = self.visit(ast.expr, c)
        if exp_type is not BoolType:
            raise TypeMismatchInStatement(ast)
        func_symbol = self.getCurrentFunc(c)
        if not func_symbol['isReturn']:
            if ast.thenStmt:
                self.visit(ast.thenStmt, c)
                l = func_symbol['isReturn']
            if not ast.elseStmt:
                func_symbol['isReturn'] = False
            else:
                func_symbol['isReturn'] = False
                self.visit(ast.elseStmt, c)
                if not l:
                    func_symbol['isReturn'] = False
        else:
            if ast.thenStmt:
                self.visit(ast.thenStmt, c)
            if ast.elseStmt:
                self.visit(ast.elseStmt, c)

    def visitBlock(self, ast, c):
        func_symbol = self.getCurrentFunc(c)
        if not func_symbol['isReturn']:
            if ast.member:
                c.insert(0, [])
                for x in ast.member:
                    if type(x) is VarDecl:
                        c[0].insert(0, self.visit(x, c[0]))
                    elif type(x) is Return:
                        func_symbol['isReturn'] = True
                    else:
                        self.visit(x, c)
                # When block is over, scope is remove so that errors not caused
                c.pop(0)
            else:
                func_symbol['isReturn'] = False
        else:
            c.insert(0, [])
            for x in ast.member:
                if type(x) is VarDecl:
                    c[0].insert(0, self.visit(x, c[0]))
                else:
                    self.visit(x, c)
            c.pop(0)

    def visitFor(self, ast, c):
        try:
            exp1_type, exp2_type, exp3_type = self.visit(
                ast.expr1, c), self.visit(ast.expr2,
                                          c), self.visit(ast.expr3, c)
        except TypeMismatchInException as e:
            raise TypeMismatchInStatement(ast)

        if (exp1_type is not IntType or exp2_type is not BoolType
                or exp3_type is not IntType):
            raise TypeMismatchInStatement(ast)
        c.insert(0, [True])
        if type(ast.loop) is Block:
            for x in ast.loop.member:
                if type(x) is VarDecl:
                    c[0].insert(0, self.visit(x, c[0]))
                else:
                    self.visit(x, c)
        else:
            self.visit(ast.loop, c)
        func_symbol = self.getCurrentFunc(c)
        if func_symbol['func'].mtype.rettype is not VoidType:
            func_symbol['isReturn'] = False
        c.pop(0)

    def visitDowhile(self, ast, c):
        exp_type = self.visit(ast.exp, c)
        if exp_type is not BoolType:
            raise TypeMismatchInStatement(ast)
        c.insert(0, [True])
        func_symbol = self.getCurrentFunc(c)
        for x in ast.sl:
            if type(x) is VarDecl:
                c[0].insert(0, self.visit(x, c[0]))
            else:
                self.visit(x, c)
        c.pop(0)

    def visitBinaryOp(self, ast, c):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        if ast.op != '=' and (type(ast.left) is StringLiteral
                              or type(ast.right) is StringLiteral):
            raise TypeMismatchInExpression(ast)

        if ast.op == '=':
            if type(ast.left) is not Id and type(ast.left) is not ArrayCell:
                raise NotLeftValue(ast.left)
            if left is ArrayType or left is ArrayPointerType or left is VoidType:
                raise TypeMismatchInExpression(ast)
            if left is not right:
                if left is FloatType and right is IntType:
                    return FloatType
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                return left
        elif ast.op in [
                '>', '>=', '<', '<=', '+', '-', '*', '/', '!=', '==', '%',
                '&&', '||'
        ]:
            if left is BoolType and right is BoolType:
                if ast.op in ['&&', '||', '==', '!=']:
                    return left
                else:
                    raise TypeMismatchInExpression(ast)
            elif left is IntType and right is IntType:
                if ast.op in ['+', '-', '*', '/', '%', ]:
                    return left
                elif ast.op in ['<', '<=', '>', '>=', '==', '!=']:
                    return BoolType
                else:
                    raise TypeMismatchInExpression(ast)
            elif left is FloatType and right is FloatType:
                if ast.op in ['+', '-', '*', '/']:
                    return left
                elif ast.op in ['<', '<=', '>', '>=']:
                    return BoolType
                else:
                    raise TypeMismatchInExpression(ast)
            elif left in (IntType, FloatType) and right in (IntType, FloatType):
                if ast.op in ['+', '-', '*', '/']:
                    return FloatType
                elif ast.op in ['<', '<=', '>', '>=']:
                    return BoolType
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        body_type = self.visit(ast.body, c)
        if (ast.op == '!' and body_type is not BoolType) or (ast.op == '-' and body_type not in [IntType, FloatType]):
            raise TypeMismatchInExpression(ast)
        return self.visit(ast.body, c)

    def visitArrayCell(self, ast, c):
        arr_type = self.visit(ast.arr, c)
        if self.visit(ast.idx, c) is not IntType:
            raise TypeMismatchInExpression(ast)
        if type(arr_type) not in [ArrayPointerType, ArrayType]:
            raise TypeMismatchInExpression(ast)
        return arr_type.eleType

    def visitReturn(self, ast, c):
        rettype = list(
            filter(
                lambda x: type(x) not in [Symbol, dict, str, bool], self.flattenC(c)))[0]
        currentFunc = self.getCurrentFunc(c)
        currentFunc['isReturn'] = True

        if ast.expr:
            expr_type = self.visit(ast.expr, c)
            if rettype is VoidType:
                raise TypeMismatchInStatement(ast)
            if rettype is FloatType and (expr_type is IntType
                                         or expr_type is FloatType):
                return
            elif type(rettype) is ArrayPointerType and (
                    type(expr_type) is ArrayType
                    or type(expr_type) is ArrayPointerType):
                if rettype.eleType is not expr_type.eleType:
                    raise TypeMismatchInStatement(ast)
            elif rettype is not expr_type:
                raise TypeMismatchInStatement(ast)
        else:
            if rettype is not VoidType:
                raise TypeMismatchInStatement(ast)

    def visitCallExpr(self, ast, c):

        already_func_declare = self.getVariableInC(
            self.flattenC(c), ast.method.name)
        if not already_func_declare:
            raise Undeclared(Function(), ast.method.name)

        if type(already_func_declare) is not dict:
            raise TypeMismatchInExpression(ast)

        # Unreachable function, check with current function flow, if name is same -> not count
        func_symbol = self.getCurrentFunc(c)
        if func_symbol['func'].name != ast.method.name:
            already_func_declare['isCalled'] = True

        flat_c = list(filter(lambda x: type(x) is Symbol, self.flattenC(c)))

        ids = []
        for x in ast.param:
            if x is Id:
                ids.append(self.lookup(x.name, flat_c, lambda x: x.name))
            else:
                ids.append(self.visit(x, c))

        if len(already_func_declare['func'].mtype.partype) != len(ids):
            raise TypeMismatchInExpression(ast)

        # zip to check simultaneously
        check_l = list(zip(already_func_declare['func'].mtype.partype, ids))

        for x in check_l:
            if x[0] is not x[1]:
                if x[0] is FloatType and x[1] is IntType:
                    continue
                if type(x[0]) is ArrayPointerType and (type(
                        x[1]) is ArrayPointerType or type(x[1]) is ArrayType):
                    if x[0].eleType is not x[1].eleType:
                        raise TypeMismatchInExpression(ast)
                else:
                    raise TypeMismatchInExpression(ast)

        return already_func_declare['func'].mtype.rettype

    def visitBreak(self, ast, c):
        if not list(filter(lambda x: type(x) is bool, self.flattenC(c))):
            raise BreakNotInLoop()

    def visitContinue(self, ast, c):
        if not list(filter(lambda x: type(x) is bool, self.flattenC(c))):
            raise ContinueNotInLoop()

    def visitArrayType(self, ast, c):
        return ArrayType(ast.dimen, self.visit(ast.eleType, c))

    def visitArrayPointerType(self, ast, c):
        return ArrayPointerType(self.visit(ast.eleType, c))

    def visitIntLiteral(self, ast, c):
        return IntType

    def visitFloatLiteral(self, ast, c):
        return FloatType

    def visitBooleanLiteral(self, ast, c):
        return BoolType

    def visitStringLiteral(self, ast, c):
        return StringType

    def visitIntType(self, ast, c):
        return IntType

    def visitFloatType(self, ast, c):
        return FloatType

    def visitStringType(self, ast, c):
        return StringType

    def visitBoolType(self, ast, c):
        return BoolType

    def visitVoidType(self, ast, c):
        return VoidType
