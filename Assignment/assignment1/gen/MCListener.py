# Generated from C:/Users/Admin/Desktop/Computer Science/Junior/Principles of Programming Languages (CO3005)/Assignment/assignment1/initial/src/main/mc/parser\MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete listener for a parse tree produced by MCParser.
class MCListener(ParseTreeListener):

    # Enter a parse tree produced by MCParser#program.
    def enterProgram(self, ctx:MCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MCParser#program.
    def exitProgram(self, ctx:MCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MCParser#decl.
    def enterDecl(self, ctx:MCParser.DeclContext):
        pass

    # Exit a parse tree produced by MCParser#decl.
    def exitDecl(self, ctx:MCParser.DeclContext):
        pass


    # Enter a parse tree produced by MCParser#varDecl.
    def enterVarDecl(self, ctx:MCParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MCParser#varDecl.
    def exitVarDecl(self, ctx:MCParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MCParser#list_vars.
    def enterList_vars(self, ctx:MCParser.List_varsContext):
        pass

    # Exit a parse tree produced by MCParser#list_vars.
    def exitList_vars(self, ctx:MCParser.List_varsContext):
        pass


    # Enter a parse tree produced by MCParser#var.
    def enterVar(self, ctx:MCParser.VarContext):
        pass

    # Exit a parse tree produced by MCParser#var.
    def exitVar(self, ctx:MCParser.VarContext):
        pass


    # Enter a parse tree produced by MCParser#funcDecl.
    def enterFuncDecl(self, ctx:MCParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by MCParser#funcDecl.
    def exitFuncDecl(self, ctx:MCParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by MCParser#funcType.
    def enterFuncType(self, ctx:MCParser.FuncTypeContext):
        pass

    # Exit a parse tree produced by MCParser#funcType.
    def exitFuncType(self, ctx:MCParser.FuncTypeContext):
        pass


    # Enter a parse tree produced by MCParser#array_pointer_type.
    def enterArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        pass

    # Exit a parse tree produced by MCParser#array_pointer_type.
    def exitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        pass


    # Enter a parse tree produced by MCParser#list_param.
    def enterList_param(self, ctx:MCParser.List_paramContext):
        pass

    # Exit a parse tree produced by MCParser#list_param.
    def exitList_param(self, ctx:MCParser.List_paramContext):
        pass


    # Enter a parse tree produced by MCParser#paraDecl.
    def enterParaDecl(self, ctx:MCParser.ParaDeclContext):
        pass

    # Exit a parse tree produced by MCParser#paraDecl.
    def exitParaDecl(self, ctx:MCParser.ParaDeclContext):
        pass


    # Enter a parse tree produced by MCParser#express.
    def enterExpress(self, ctx:MCParser.ExpressContext):
        pass

    # Exit a parse tree produced by MCParser#express.
    def exitExpress(self, ctx:MCParser.ExpressContext):
        pass


    # Enter a parse tree produced by MCParser#operands.
    def enterOperands(self, ctx:MCParser.OperandsContext):
        pass

    # Exit a parse tree produced by MCParser#operands.
    def exitOperands(self, ctx:MCParser.OperandsContext):
        pass


    # Enter a parse tree produced by MCParser#lit.
    def enterLit(self, ctx:MCParser.LitContext):
        pass

    # Exit a parse tree produced by MCParser#lit.
    def exitLit(self, ctx:MCParser.LitContext):
        pass


    # Enter a parse tree produced by MCParser#arr_el.
    def enterArr_el(self, ctx:MCParser.Arr_elContext):
        pass

    # Exit a parse tree produced by MCParser#arr_el.
    def exitArr_el(self, ctx:MCParser.Arr_elContext):
        pass


    # Enter a parse tree produced by MCParser#func_call.
    def enterFunc_call(self, ctx:MCParser.Func_callContext):
        pass

    # Exit a parse tree produced by MCParser#func_call.
    def exitFunc_call(self, ctx:MCParser.Func_callContext):
        pass


    # Enter a parse tree produced by MCParser#list_express.
    def enterList_express(self, ctx:MCParser.List_expressContext):
        pass

    # Exit a parse tree produced by MCParser#list_express.
    def exitList_express(self, ctx:MCParser.List_expressContext):
        pass


    # Enter a parse tree produced by MCParser#statements.
    def enterStatements(self, ctx:MCParser.StatementsContext):
        pass

    # Exit a parse tree produced by MCParser#statements.
    def exitStatements(self, ctx:MCParser.StatementsContext):
        pass


    # Enter a parse tree produced by MCParser#if_s.
    def enterIf_s(self, ctx:MCParser.If_sContext):
        pass

    # Exit a parse tree produced by MCParser#if_s.
    def exitIf_s(self, ctx:MCParser.If_sContext):
        pass


    # Enter a parse tree produced by MCParser#dowhile_s.
    def enterDowhile_s(self, ctx:MCParser.Dowhile_sContext):
        pass

    # Exit a parse tree produced by MCParser#dowhile_s.
    def exitDowhile_s(self, ctx:MCParser.Dowhile_sContext):
        pass


    # Enter a parse tree produced by MCParser#for_s.
    def enterFor_s(self, ctx:MCParser.For_sContext):
        pass

    # Exit a parse tree produced by MCParser#for_s.
    def exitFor_s(self, ctx:MCParser.For_sContext):
        pass


    # Enter a parse tree produced by MCParser#break_s.
    def enterBreak_s(self, ctx:MCParser.Break_sContext):
        pass

    # Exit a parse tree produced by MCParser#break_s.
    def exitBreak_s(self, ctx:MCParser.Break_sContext):
        pass


    # Enter a parse tree produced by MCParser#continue_s.
    def enterContinue_s(self, ctx:MCParser.Continue_sContext):
        pass

    # Exit a parse tree produced by MCParser#continue_s.
    def exitContinue_s(self, ctx:MCParser.Continue_sContext):
        pass


    # Enter a parse tree produced by MCParser#return_s.
    def enterReturn_s(self, ctx:MCParser.Return_sContext):
        pass

    # Exit a parse tree produced by MCParser#return_s.
    def exitReturn_s(self, ctx:MCParser.Return_sContext):
        pass


    # Enter a parse tree produced by MCParser#express_s.
    def enterExpress_s(self, ctx:MCParser.Express_sContext):
        pass

    # Exit a parse tree produced by MCParser#express_s.
    def exitExpress_s(self, ctx:MCParser.Express_sContext):
        pass


    # Enter a parse tree produced by MCParser#block_s.
    def enterBlock_s(self, ctx:MCParser.Block_sContext):
        pass

    # Exit a parse tree produced by MCParser#block_s.
    def exitBlock_s(self, ctx:MCParser.Block_sContext):
        pass


    # Enter a parse tree produced by MCParser#primtype.
    def enterPrimtype(self, ctx:MCParser.PrimtypeContext):
        pass

    # Exit a parse tree produced by MCParser#primtype.
    def exitPrimtype(self, ctx:MCParser.PrimtypeContext):
        pass


