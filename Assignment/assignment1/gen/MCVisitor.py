# Generated from C:/Users/Admin/Desktop/Computer Science/Junior/Principles of Programming Languages (CO3005)/Assignment/assignment1/initial/src/main/mc/parser\MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#decl.
    def visitDecl(self, ctx:MCParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#varDecl.
    def visitVarDecl(self, ctx:MCParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_vars.
    def visitList_vars(self, ctx:MCParser.List_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcDecl.
    def visitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcType.
    def visitFuncType(self, ctx:MCParser.FuncTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_param.
    def visitList_param(self, ctx:MCParser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#paraDecl.
    def visitParaDecl(self, ctx:MCParser.ParaDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express.
    def visitExpress(self, ctx:MCParser.ExpressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#lit.
    def visitLit(self, ctx:MCParser.LitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arr_el.
    def visitArr_el(self, ctx:MCParser.Arr_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_call.
    def visitFunc_call(self, ctx:MCParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#list_express.
    def visitList_express(self, ctx:MCParser.List_expressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#statements.
    def visitStatements(self, ctx:MCParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_s.
    def visitIf_s(self, ctx:MCParser.If_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhile_s.
    def visitDowhile_s(self, ctx:MCParser.Dowhile_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_s.
    def visitFor_s(self, ctx:MCParser.For_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_s.
    def visitBreak_s(self, ctx:MCParser.Break_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_s.
    def visitContinue_s(self, ctx:MCParser.Continue_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_s.
    def visitReturn_s(self, ctx:MCParser.Return_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#express_s.
    def visitExpress_s(self, ctx:MCParser.Express_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_s.
    def visitBlock_s(self, ctx:MCParser.Block_sContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primtype.
    def visitPrimtype(self, ctx:MCParser.PrimtypeContext):
        return self.visitChildren(ctx)



del MCParser