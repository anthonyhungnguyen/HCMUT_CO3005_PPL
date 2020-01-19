# 1752259
from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *


class ASTGeneration(MCVisitor):
    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx: MCParser.ProgramContext):
        declList = []
        for x in ctx.decl():
            decl = self.visitDecl(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)

    def visitList_vars(self, ctx: MCParser.List_varsContext):
        return [self.visit(x) for x in ctx.var()]

    def visitVar(self, ctx: MCParser.VarContext):
        return [ctx.INTLIT().getText(),
                ctx.ID().getText()] if ctx.INTLIT() else ctx.ID().getText()

    # Visit a parse tree produced by MCParser#var_decl
    def visitVarDecl(self, ctx: MCParser.VarDeclContext):
        dataType = self.visit(ctx.primtype())
        return [
            VarDecl(x[1], ArrayType(x[0], dataType))
            if isinstance(x, list) else VarDecl(x, dataType)
            for x in self.visit(ctx.list_vars())
        ]

    # Visit a parse tree produced by MCParser#func_decl
    def visitFuncDecl(self, ctx: MCParser.FuncDeclContext):
        name = Id(ctx.ID().getText())
        param = self.visit(ctx.list_param()) if ctx.list_param() else []
        returnType = self.visit(ctx.funcType())
        body = self.visit(ctx.block_s())
        return FuncDecl(name, param, returnType, body)

    def visitFuncType(self, ctx: MCParser.FuncTypeContext):
        return self.visit(ctx.primtype()) if ctx.primtype() else VoidType(
        ) if ctx.VOIDTYPE() else self.visit(ctx.array_pointer_type())

    def visitArray_pointer_type(self, ctx: MCParser.Array_pointer_typeContext):
        return ArrayPointerType(self.visit(ctx.primtype()))

    def visitList_param(self, ctx: MCParser.List_paramContext):
        return [self.visit(x) for x in ctx.paraDecl()]

    def visitParaDecl(self, ctx: MCParser.ParaDeclContext):
        primtype = self.visit(ctx.primtype())
        return VarDecl(ctx.ID().getText(), ArrayPointerType(
            primtype)) if ctx.getChildCount() == 4 else VarDecl(
                ctx.ID().getText(), primtype)

    def visitExpress(self, ctx: MCParser.ExpressContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_ass())
        left = self.visit(ctx.express_ass())
        right = self.visit(ctx.express())
        return BinaryOp('=', left, right)

    def visitExpress_ass(self, ctx: MCParser.Express_assContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_or())
        left = self.visit(ctx.express_ass())
        right = self.visit(ctx.express_or())
        return BinaryOp('||', left, right)

    def visitExpress_or(self, ctx: MCParser.Express_orContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_and())
        left = self.visit(ctx.express_or())
        right = self.visit(ctx.express_and())
        return BinaryOp('&&', left, right)

    def visitExpress_and(self, ctx: MCParser.Express_andContext):
        # print(ctx.getChildCount())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_not_or_equal(0))
        left = self.visit(ctx.express_not_or_equal(0))
        right = self.visit(ctx.express_not_or_equal(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    def visitExpress_not_or_equal(self,
                                  ctx: MCParser.Express_not_or_equalContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_compare(0))
        left = self.visit(ctx.express_compare(0))
        right = self.visit(ctx.express_compare(1))
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    def visitExpress_compare(self, ctx: MCParser.Express_compareContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_add_sub())
        left = self.visit(ctx.express_compare())
        right = self.visit(ctx.express_add_sub())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    def visitExpress_add_sub(self, ctx: MCParser.Express_add_subContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_div_mul_mod())
        left = self.visit(ctx.express_add_sub())
        right = self.visit(ctx.express_div_mul_mod())
        op = ctx.getChild(1).getText()
        return BinaryOp(op, left, right)

    def visitExpress_div_mul_mod(self,
                                 ctx: MCParser.Express_div_mul_modContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_sub_not())
        body = self.visit(ctx.express_div_mul_mod())
        op = ctx.getChild(0).getText()
        return UnaryOp(op, body)

    def visitExpress_sub_not(self, ctx: MCParser.Express_sub_notContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.express_paren())
        else:
            if ctx.ID():
                return self.visit(ctx.express())
            else:
                arr = self.visit(ctx.express_paren())
                idx = self.visit(ctx.express())
                return ArrayCell(arr, idx)

    def visitExpress_paren(self, ctx: MCParser.Express_parenContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operands())
        return self.visit(ctx.express())

    def visitOperands(self, ctx: MCParser.OperandsContext):
        if ctx.lit():
            return self.visit(ctx.lit())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.func_call())

    def visitLit(self, ctx: MCParser.LitContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.BOOLEANLIT():
            return BooleanLiteral(True if ctx.BOOLEANLIT().getText() ==
                                  'true' else False)

    def visitFunc_call(self, ctx: MCParser.Func_callContext):
        method = Id(ctx.ID().getText())
        param = self.visit(ctx.list_express()) if ctx.list_express() else []
        return CallExpr(method, param)

    def visitList_express(self, ctx: MCParser.List_expressContext):
        return [self.visit(x) for x in ctx.express()]

    # Visit a parse tree produced by MCParser#func_decl
    def visitIf_s(self, ctx: MCParser.If_sContext):
        exp = [self.visit(ctx.express())]
        stmt_list = []
        for x in ctx.statements():
            stmt = self.visit(x)
            if isinstance(stmt, list):
                stmt_list.extend(stmt if stmt else [])
            else:
                stmt_list.append(stmt)
        return If(exp[0], stmt_list[0],
                  stmt_list[1] if len(stmt_list) == 2 else None)

    def visitFor_s(self, ctx: MCParser.For_sContext):
        exp = [self.visit(x) for x in ctx.express()]
        loop = self.visit(ctx.statements())
        return For(exp[0], exp[1], exp[2], loop)

    def visitDowhile_s(self, ctx: MCParser.Dowhile_sContext):
        sl = [self.visit(x) for x in ctx.statements()]
        exp = self.visit(ctx.express())
        return Dowhile(sl, exp)

    def visitBlock_s(self, ctx: MCParser.Block_sContext):
        block_list = []
        for x in ctx.blockmember():
            block = self.visitBlockmember(x)
            if isinstance(block, list):
                block_list.extend(block if block else [])
            else:
                block_list.append(block)
        return Block(block_list)

    def visitBlockmember(self, ctx: MCParser.BlockmemberContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        else:
            return self.visit(ctx.statements())

    def visitStatements(self, ctx: MCParser.StatementsContext):
        if ctx.getChildCount() == 2:
            stmt = ctx.getChild(0)
            return self.visit(stmt)
        else:
            if ctx.for_s():
                return self.visit(ctx.for_s())
            if ctx.if_s():
                return self.visit(ctx.if_s())
            if ctx.block_s():
                return self.visit(ctx.block_s())

    def visitReturn_s(self, ctx: MCParser.Return_sContext):
        if ctx.express():
            return Return(self.visit(ctx.express()))
        else:
            return Return()

    def visitBreak_s(self, ctx: MCParser.Break_sContext):
        return Break()

    def visitContinue_s(self, ctx: MCParser.Continue_sContext):
        return Continue()

    def visitExpress_s(self, ctx: MCParser.Express_sContext):
        return self.visit(ctx.express())

    def visitPrimtype(self, ctx: MCParser.PrimtypeContext):
        if ctx.BOOLEANTYPE():
            return BoolType()
        if ctx.INTTYPE():
            return IntType()
        if ctx.FLOATTYPE():
            return FloatType()
        if ctx.STRINGTYPE():
            return StringType()
