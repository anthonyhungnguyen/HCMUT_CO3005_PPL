"""
 * @author nhphung
"""
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
        Symbol("getInt", MType([], IntType), [True, True]),
        Symbol("putIntLn", MType([IntType], VoidType), [True, True]),
        Symbol("putInt", MType([IntType], VoidType), [True, True]),
        Symbol("getFloat", MType([], FloatType), [True, True]),
        Symbol("putFloat", MType([FloatType], VoidType), [True, True]),
        Symbol("putFloatLn", MType([FloatType], VoidType), [True, True]),
        Symbol("putBool", MType([BoolType], VoidType), [True, True]),
        Symbol("putBoolLn", MType([BoolType], VoidType), [True, True]),
        Symbol("putString", MType([StringType], VoidType), [True, True]),
        Symbol("putStringLn", MType([StringType], VoidType), [True, True]),
        Symbol("putLn", MType([], VoidType), [True, True])
    ]

    def __init__(self, ast):
        #print(ast)
        #print(ast)
        #print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def getFunctionName(self, c):
        method_name = list(
            filter(lambda x: type(x) is str, reduce(lambda x, y: x + y, c)))[0]
        return self.lookup(method_name, c[-1], lambda x: x.name)

    def visitProgram(self, ast, c):
        l = []
        l.extend(c)
        for x in ast.decl:
            l.insert(0, self.visit(x, l))

        # check no entry point
        hasentry = self.lookup('main', l, lambda x: x.name)
        if not hasentry:
            raise NoEntryPoint()
        total_l = [l]
        for x in ast.decl:
            if type(x) is FuncDecl:
                self.visit(x, total_l)

        # check func not return
        check_func_not_return = list(
            filter(
                lambda x: type(x.mtype) is MType and x.value[0] == False , total_l[0]))
        if check_func_not_return:
            raise FunctionNotReturn(check_func_not_return[0].name)

        # Check unreachable
        check_func_unreachable = list(
            filter(
                lambda x: type(x.mtype) is MType and x.name != 'main' and x.
                value[1] == False, total_l[0]))

        if check_func_unreachable:
            raise UnreachableFunction(check_func_unreachable[0].name)

        return total_l

    def visitVarDecl(self, ast, c):
        if c:
            symbol_filter = list(filter(lambda x: type(x) is Symbol, c))
            if self.lookup(ast.variable, symbol_filter, lambda x: x.name):
                raise Redeclared(Variable(), ast.variable)
            return Symbol(ast.variable, self.visit(ast.varType, c))
        return Symbol(ast.variable, self.visit(ast.varType, c))

    def visitFuncDecl(self, ast, c):
        pr = []
        pr_type = []

        if not c:
            # When function has param
            pr = [self.visit(x, pr) for x in ast.param]
            pr_type = [x.mtype for x in pr]
            if self.lookup(ast.name.name, c, lambda x: x.name):
                raise Redeclared(Function(), ast.name.name)
            return Symbol(ast.name.name, MType(pr_type, self.visit(ast.returnType,c)), [
                False, False
            ]) if self.visit(ast.returnType, c) is not VoidType else Symbol(
                ast.name.name, MType(pr_type, self.visit(ast.returnType,c)), [True, False])
        # If already travelled once -> insert param list
        if isinstance(c[0], list):
            c.insert(0, [])
            for x in ast.param:
                try:
                    c[0].insert(0, self.visit(x, c[0]))
                except Redeclared as e:
                    raise Redeclared(Parameter(), e.n)

        else:
            # When function has param
            pr = [self.visit(x, pr) for x in ast.param]
            pr_type = [x.mtype for x in pr]
            if self.lookup(ast.name.name, c, lambda x: x.name):
                raise Redeclared(Function(), ast.name.name)
            return Symbol(ast.name.name, MType(pr_type, self.visit(ast.returnType,c)), [
                False, False
            ]) if self.visit(ast.returnType, c) is not VoidType else Symbol(
                ast.name.name, MType(pr_type, self.visit(ast.returnType,c)), [True, False])

        # Insert rettype to check return type is correct
        c[0].insert(0,self.lookup(ast.name.name,c[-1], lambda x: x.name).mtype.rettype)

        # Insert function name
        c[0].insert(0, ast.name.name)
        for x in ast.body.member:
            if isinstance(x, VarDecl):
                c[0].insert(0, self.visit(x, c[0]))
            else:
                self.visit(x, c)
        # Final list only keeps global variable and function
        c.pop(0)

    def visitIf(self, ast, c):
        exp_type = self.visit(ast.expr, c)
        if exp_type is not BoolType:
            raise TypeMismatchInStatement(ast)
        func_symbol = self.getFunctionName(c)

        if not func_symbol.value[0]:
            if ast.thenStmt:
                if type(ast.thenStmt) is Block:
                    self.visit(ast.thenStmt, c)
                    if not func_symbol.value[0]:
                        return
                elif type(ast.thenStmt) is Return:
                    self.visit(ast.thenStmt, c)
                    func_symbol.value[0] = True
                elif type(ast.thenStmt) is If:
                    self.visit(ast.thenStmt, c)
                else:
                    return
            if not ast.elseStmt:
                func_symbol.value[0] = False
            else:
                func_symbol.value[0] = False
                if type(ast.elseStmt) is Block:
                    self.visit(ast.elseStmt, c)
                    if not func_symbol.value[0]:
                        return
                elif type(ast.elseStmt) is Return:
                    self.visit(ast.elseStmt, c)
                    func_symbol.value[0] = True
                elif type(ast.elseStmt) is If:
                    self.visit(ast.elseStmt, c)
                else:
                    return
        else:
            if ast.thenStmt:
                self.visit(ast.thenStmt, c)
            if ast.elseStmt:
                self.visit(ast.elseStmt, c)

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
        func_symbol = self.getFunctionName(c)
        func_symbol.value[0] = False
        c.pop(0)

    def visitDowhile(self, ast, c):
        exp_type = self.visit(ast.exp, c)
        if exp_type is not BoolType:
            raise TypeMismatchInStatement(ast)
        c.insert(0, [True])
        func_symbol = self.getFunctionName(c)
        func_symbol.value[0] = False
        for x in ast.sl:
            if type(x) is VarDecl:
                c[0].insert(0, self.visit(x, c[0]))
            else:
                self.visit(x, c)
        c.pop(0)

    def visitBinaryOp(self, ast, c):
        if ast.op != '=' and (type(ast.left) is StringLiteral
                              or type(ast.right) is StringLiteral):
            raise TypeMismatchInExpression(ast)

        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        if ast.op == '=':
            if left is ArrayType or left is ArrayPointerType or left is VoidType:
                raise TypeMismatchInExpression(ast)
            if type(ast.left) is not Id and type(ast.left) is not ArrayCell:
                raise NotLeftValue(ast)
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
                    return BoolType
                else:
                    raise TypeMismatchInExpression(ast)
            if left not in [IntType, FloatType
                            ] or right not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            if ast.op == '%':
                if left is IntType and right is IntType:
                    return IntType
                else:
                    raise TypeMismatchInExpression(ast)
            if ast.op in ['>', '>=', '<', '<=', '!=', '==']:
                return BoolType
            if ast.op in ['+', '-', '*', '/']:
                if left is IntType and right is IntType:
                    return IntType
                else:
                    return FloatType

    def visitUnaryOp(self, ast, c):
        return self.visit(ast.body, c)

    def visitId(self, ast, c):
        flat_c = list(
            filter(lambda x: type(x) is Symbol, reduce(lambda x, y: x + y, c)))
        if not self.lookup(ast.name, flat_c, lambda x: x.name) or type(
                :
            raise Undeclared(Identifier(), ast.name)

        return self.lookup(ast.name, flat_c, lambda x: x.name).mtype

    def visitBlock(self, ast, c):
        func_symbol = self.getFunctionName(c)
        if not func_symbol.value[0]:
            if ast.member:
                c.insert(0, [])
                for x in ast.member:
                    if isinstance(x, VarDecl):
                        c[0].insert(0, self.visit(x, c[0]))
                    elif type(x) is Return:
                        func_symbol.value[0] = True
                    else:
                        self.visit(x, c)
                # When block is over, scope is remove so that errors not caused
                c.pop(0)
            else:
                func_symbol.value[0] = False
        else:
            c.insert(0, [])
            for x in ast.member:
                if isinstance(x, VarDecl):
                    c[0].insert(0, self.visit(x, c[0]))
                else:
                    self.visit(x, c)
            c.pop(0)

    def visitArrayCell(self, ast, c):
        arr_type = self.visit(ast.arr, c)
        if self.visit(ast.idx,c) is not IntType:
            raise TypeMismatchInExpression(ast)
        if type(arr_type) not in [ArrayPointerType, ArrayType]:
            raise TypeMismatchInExpression(ast)
        return arr_type.eleType

    def visitReturn(self, ast, c):
        flat_c = reduce(lambda x, y: x + y, c)
        rettype = list(
            filter(
                lambda x: type(x) is not Symbol and type(x) is not bool and
                type(x) is not str, flat_c))[0]
        symbol_lst = list(filter(lambda x: type(x) is Symbol, flat_c))
        func_symbol = self.getFunctionName(c)
        func_symbol.value[0] = True

        if ast.expr:
            expr_type = self.visit(ast.expr, c)

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
        already_func_declare = self.lookup(
            ast.method.name,
            list(
                filter(lambda x: type(x) is Symbol,
                       reduce(lambda x, y: x + y, c))), lambda x: x.name)
        if not already_func_declare or not already_func_declare.value:
            raise Undeclared(Function(), ast.method.name)

        # Unreachable function, check with current function flow, if name is same -> not count
        func_symbol = self.getFunctionName(c)

        if func_symbol.name != ast.method.name:
            already_func_declare.value[1] = True

        flat_c = list(
            filter(lambda x: type(x) is Symbol, reduce(lambda x, y: x + y, c)))
        ids = []
        for x in ast.param:
            if x is Id:
                ids.append(self.lookup(x.name, flat_c, lambda x: x.name))
            else:
                ids.append(self.visit(x, c))
        
        if len(already_func_declare.mtype.partype) != len(ids):
            raise TypeMismatchInExpression(ast)


        # zip to check simultaneously
        check_l = list(zip(already_func_declare.mtype.partype, ids))
        
        
        for x in check_l:
            if x[0] is not x[1]:
                if x[0] is FloatType and x[1] is IntType:
                    return
                if type(x[0]) is ArrayPointerType and (type(
                        x[1]) is ArrayPointerType or type(x[1]) is ArrayType):
                    if x[0].eleType is not x[1].eleType:
                        raise TypeMismatchInExpression(ast)
                else:
                    raise TypeMismatchInExpression(ast)
    
        return already_func_declare.mtype.rettype

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

    def visitBreak(self, ast, c):
        hasLoop = list(
            filter(lambda x: type(x) is bool, reduce(lambda x, y: x + y, c)))
        if not hasLoop:
            raise BreakNotInLoop()

    def visitContinue(self, ast, c):
        hasLoop = list(
            filter(lambda x: type(x) is bool, reduce(lambda x, y: x + y, c)))
        if not hasLoop:
            raise ContinueNotInLoop()