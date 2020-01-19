'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt",MType([],IntType()),CName(self.libName),True),
                Symbol("putInt",MType([IntType()],VoidType()),CName(self.libName),True),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName(self.libName),True),
                Symbol("getFloat",MType([],FloatType()),CName(self.libName),True),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName(self.libName),True),
                Symbol("putFloatLn",MType([FloatType()],VoidType()),CName(self.libName),True),
                Symbol("putBool",MType([BoolType()],VoidType()),CName(self.libName),True),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName(self.libName),True),
                Symbol("putString",MType([StringType()],VoidType()),CName(self.libName),True),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName(self.libName),True),
                Symbol("putLn",MType([],VoidType()),CName(self.libName),True)
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)
class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass
class PointerType:
    def __init__(self,ctype):
        self.ctype =ctype

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value
class Symbol:
    def __init__(self,name,mtype,value,isInit):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.isInit = isInit

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        check_type = 0

    def getName(self,ast):
        if type(ast).__name__ == "VarDecl":
            return ast.variable
        else: return ast.name.name

    def getTypeAst(self,ast):
        if type(ast).__name__ == "VarDecl":
            return ast.varType
        else:
            param =[]
            for x in ast.param:
                param.append(x.varType)
            return MType(param,ast.returnType)

    def visitProgram(self, ast, c):
        CodeGenVisitor.check_type = 0
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        glenv = self.env
        for x in ast.decl:
            res = self.lookup(self.getName(x),glenv, lambda x: x.name)
            if res is None:
                # glenv.insert(0,Symbol(self.getName(x),self.getTypeAst(x),CName(self.className),True))
                glenv = [Symbol(self.getName(x),self.getTypeAst(x),CName(self.className),True)] + glenv
        e = SubBody(None,glenv)
        for x in ast.decl:
            if type(x) is VarDecl:
                e = self.visit(x,e)
        for x in ast.decl:
            if type(x) is FuncDecl:
                e = self.visit(x,e)
        # print(e.frame)
        # print("SSSSSSSSSSSSSSSSSSSSSSSSSSS")
        # print([x.name for x in e.sym])
        self.genMETHOD(FuncDecl(Id("<init>"),[],None,Block([])),glenv,Frame("<init>",VoidType()))#VoidType()
        self.emit.emitEPILOG()
        return c
    def getType(self,in_):
        if type(in_).__name__ in ["ArrayType","ArrayPointerType"]:
            return PointerType(in_.eleType)
        elif type(in_).__name__ == "MType":
            return in_.rettype
        else: return in_
    def getTypeP(self,in_):
        if type(in_).__name__ == "ArrayType":
            return in_.eleType
        elif type(in_).__name__ == "ArrayPointerType":
            return PointerType(in_.eleType)
        elif type(in_).__name__ == "MType":
            return self.getTypeP(in_.rettype)
        else: return in_


    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType).__name__ == "VoidType"
        returnType = VoidType() if isInit else consdecl.returnType#()
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [PointerType(StringType())] if isMain else list(map(lambda x : x.varType,consdecl.param))#()
        mtype = MType(intype, returnType)
        # print(methodName, mtype, not isInit, frame)
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)
        glenv = o
        # if isInit:
        #     for x in glenv:
        #         if type(x.mtype).__name__ == "ArrayType":
        #             a = x.mtype
        #             cfield = x.value.value
        #             x1 = self.emit.emitPUSHICONST(a.dimen,frame)
        #             x2 = self.emit.emitNEWARRAY(a.eleType)
        #             x3 = self.emit.emitPUTSTATIC(cfield +"."+x.name,self.getType(x.mtype),frame)
        #             self.emit.printout(x1 + x2 + x3)
        #             print(x1,x2,x3)
        
          # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args",PointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            
    
        para =("",SubBody(frame,glenv))
        for x in consdecl.param:
            (str1,sym) = self.visit(x,para[1])
            sym.isInit =True
            # para[0] = para[0] + str1
            # para[1].sym = [sym] +para[1].sym 
            para = (para[0] +str1,SubBody(frame,[sym] + para[1].sym ))
        self.emit.printout(para[0])
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
            for x in glenv:
                if type(x.mtype).__name__ == "ArrayType":
                    self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
                    a = x.mtype
                    cfield = x.value.value
                    x1 = self.emit.emitPUSHICONST(a.dimen,frame)
                    x2 = self.emit.emitNEWARRAY(a.eleType)
                    x3 = self.emit.emitPUTSTATIC(cfield +"."+x.name,self.getType(x.mtype),frame)
                    self.emit.printout(x1 + x2 + x3)
        symret = Symbol("0_ret",returnType,None,True)
        # print("test")
        # print(para[1])
        
        self.visit(consdecl.body,SubBody(frame,[symret]+para[1].sym))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(self.getType(returnType),frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        # if frame.getStackSize() != 0:
        #     print(methodName+"---"+str(frame.getStackSize())+"---:max: "+str(frame.getMaxOpStackSize()))
        frame.exitScope()
    def emitDEFAULT(self,in_,frame):
        if type(in_) is IntType:
            return self.emit.emitPUSHICONST(0, frame)
        elif type(in_) is BoolType:
            return self.emit.emitPUSHICONST(0, frame)
        elif type(in_) is FloatType :
            return self.emit.emitPUSHFCONST("0.0", frame)
        elif type(in_) is StringType :
            return self.emit.emitPUSHCONST("\"null\"", StringType(), frame)
        elif type(in_) is ArrayType :
            return self.emitDEFAULT(in_.eleType,frame)
        elif type(in_) is ArrayPointerType :
            return self.emitDEFAULT(in_.eleType,frame)

    def visitVarDecl(self, ast,c):
        ctxt = c
        frame =ctxt.frame
        vname =ast.variable
        vtype =self.getType(ast.varType)
        print(type(ast.varType))
        print(frame)
        if frame is not None :
            # print("ITSOKOKOKOKOKOKOKOKOKOKOKOKOKOKOKO")
            print(type(ast.varType))
            index = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index,vname,vtype,frame.getStartLabel(),frame.getEndLabel(),frame))
            if type(ast.varType) is ArrayType:
                art =ast.varType
                self.emit.printout(self.emit.emitINITARRAY(index,art.dimen,art.eleType,frame))
            
            return (self.emit.emitVAR(index,vname,vtype,frame.getStartLabel(),frame.getEndLabel(),frame),Symbol(vname,ast.varType,Index(index),True if(type(ast.varType) is ArrayType)  else False))
        else:
            print("VARDECLAREF")
            self.emit.printout(self.emit.emitATTRIBUTE(vname,vtype,False,None))
            return SubBody(None,[Symbol(vname,ast.varType,CName(self.className),True)]+ctxt.sym)
  

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        
        subctxt = o
        frame = Frame(ast.name.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        # print("B")
        listpara =list(map(lambda x : x.varType,ast.param))
        return SubBody(None, [Symbol(ast.name.name, MType(listpara, ast.returnType), CName(self.className),True)] + subctxt.sym)
    def visitIntType(self,ast,c):
        return ast
    def visitFloatType(self,ast,c):
        return ast
    def visitBoolType(self,ast,c):
        return ast
    def visitStringType(self,ast,c):
        return ast
    def visitVoidType(self,ast,c):
        return ast
    def visitArrayType(self,ast,c):
        return ast
    def visitArrayPointerType(self,ast,c):
        return ast
    def visitBinaryOp(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        op = ast.op
        
        print(str(ast)+" op: stack = "+str(frame.getStackSize()))
        if op != "=":
            right = self.visit(ast.right,Access(frame,nenv,False,False))
            rc = right[0]
            rt = self.getTypeP(right[1])
            left = self.visit(ast.left,Access(frame,nenv,False,False))
            lc = left[0]
            lt = self.getTypeP(left[1])
            
            if op in ["+","-"]: 
                if type(lt).__name__ == type(rt).__name__:
                    return (lc + rc + self.emit.emitADDOP(op,lt,frame),lt)
                elif type(lt) is IntType and type(rt) is FloatType:
                    return (lc + self.emit.emitI2F(frame)+rc+ self.emit.emitADDOP(op,rt,frame),rt)
                else: return (lc+rc+self.emit.emitI2F(frame)+self.emit.emitADDOP(op,lt,frame),lt)
                
            elif op in ["*" , "/"]:
                if type(lt).__name__ == type(rt).__name__:
                    return (lc + rc +self.emit.emitMULOP(op,lt,frame),lt)
                elif type(lt) is IntType and type(rt) is FloatType:
                    return (lc + self.emit.emitI2F(frame)+rc+self.emit.emitMULOP(op,rt,frame),rt)
                else: return (lc+rc+self.emit.emitI2F(frame)+self.emit.emitMULOP(op,lt,frame),lt)
                
            elif op == "%":
                if type(lt) is IntType and type(rt) is IntType:
                    return (lc + rc + self.emit.emitMOD(op,lt,frame),lt)
            elif op in ["&&" , "||"]: 
                falseLabel = frame.getNewLabel()
                truLabel = frame.getNewLabel()
                endLabel = frame.getNewLabel()
                buff = list()

                buff.append(lc)
                if(op == "&&"):
                    buff.append(self.emit.emitIFEQ(falseLabel,frame))
                else:
                    buff.append(self.emit.emitIFNE(truLabel,frame))

                buff.append(rc)
                buff.append(self.emit.emitIFEQ(falseLabel,frame))
                buff.append(self.emit.emitLABEL(truLabel,frame))
                buff.append(self.emit.emitPUSHICONST(1,frame))
                buff.append(self.emit.emitGOTO(endLabel,frame))
                buff.append(self.emit.emitLABEL(falseLabel,frame))
                buff.append(self.emit.emitPUSHICONST(0,frame))
                buff.append(self.emit.emitLABEL(endLabel,frame))
                frame.pop()
                return (''.join(buff), BoolType())
            
            elif op in [">" , "<" , "<=" , ">=" ,"==" , "!="]:
                if type(lt) is type(rt):
                    return (lc + rc +self.emit.emitREOP(op,lt,frame),BoolType())
                if type(lt) is IntType and type(rt) is FloatType:
                    return (lc + self.emit.emitI2F(frame)+rc+self.emit.emitREOP(op,rt,frame),BoolType())
                else: return(lc+rc+self.emit.emitI2F(frame)+self.emit.emitREOP(op,lt,frame),BoolType())
                
            else: raise IllegalOperandException(str(ast))
        
        else : 
            if type(ast.left) is ArrayCell :
                left = self.visit(ast.left,Access(frame,nenv,True,ctxt.isFirst))
                right =  self.visit(ast.right,Access(frame,nenv,False,False))

                rc = right[0]
                rt = self.getTypeP(right[1])
                lc = left[0]
                lt = self.getType(left[1])

                if type(lt).__name__ ==  type(rt).__name__:
                    if (ctxt.isLeft, ctxt.isFirst) is (False, True):
                        store = self.emit.emitASTORE(self.getTypeP(left[1]),frame)
                        return (lc+rc+store,lt)
                    elif (ctxt.isLeft, ctxt.isFirst) is (False, False):
                        return (lc+rc+self.emit.emitDUPX2(frame)+self.emit.emitASTORE(self.getTypeP(left[1]),frame),lt)
                    else: return (lc+rc,lt)
                    

                elif type(lt) is IntType and type(rt) is FloatType:
                    if (ctxt.isLeft, ctxt.isFirst) is (False, True):
                        return (lc+rc+self.emit.emitI2F(frame)+self.emit.emitASTORE(self.getTypeP(left[1]),frame),lt)
                    elif (ctxt.isLeft, ctxt.isFirst) is (False, False):
                        return (lc+rc+self.emit.emitI2F(frame)+self.emit.emitDUPX2(frame)+self.emit.emitASTORE(self.getTypeP(left._2),frame),lt)

                    else:
                        return (lc+rc,lt)
                else: raise IllegalOperandException("")
            else:
                right = self.visit(ast.right,Access(frame,nenv,False,False))
                left = self.visit(ast.left,Access(frame,nenv,True,ctxt.isFirst))
                rc = right[0]
                rt = self.getTypeP(right[1])
                lc = left[0]
                lt = self.getType(left[1])
                if type(lt) is FloatType and type(rt) is IntType:
                    return (rc+self.emit.emitI2F(frame)+lc,lt)
                else: 
                    print("SDSFSGFHSJGFJSGFHGSJGFGFSHGJSDS")
                    print(rc+lc,lt)
                    return  (rc+lc,lt)
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        op = ast.op
        
        # print(str(ast)+" op: stack = "+str(frame.getStackSize()))
        if op != "=":
            right = self.visit(ast.right,Access(frame,nenv,False,False))
            inre = right[0]
            rt = self.getTypeP(right[1])
            left = self.visit(ast.left,Access(frame,nenv,False,True))
            inle = left[0]
            inlt = self.getTypeP(left[1])
            
            # if op in ["+","-"]: 
            #     if type(inlt) is type(inrt):
            #         return (inle + inre + self.emit.emitADDOP(op,inlt,frame),inlt)
            #     elif type(inlt) is IntType and type(inrt) is FloatType:
            #         return (inle + self.emit.emitI2F(frame)+inre+ self.emit.emitADDOP(op,inrt,frame),inrt)
            #     else: return (inle+inre+self.emit.emitI2F(frame)+self.emit.emitADDOP(op,inlt,frame),inlt)
                
            # elif op in ["*" , "/"]:
            #     if type(inlt) is type(inrt):
            #         return (inle + inre +self.emit.emitMULOP(op,inlt,frame),inlt)
            #     elif type(inlt) is IntType and type(inrt) is FloatType:
            #         return (inle + self.emit.emitI2F(frame)+inre+self.emit.emitMULOP(op,inrt,frame),inrt)
            #     else: return (inle+inre+self.emit.emitI2F(frame)+self.emit.emitMULOP(op,inlt,frame),inlt)
            # if ast.op in ['+', '-']:
            lc, lt = self.visit(ast.left, Access(frame, nenv, False, True))
            rc, rt = self.visit(ast.right, Access(frame, nenv, False, False))

            if type(CodeGenVisitor.check_type) is IntType:
                if type(lt) == type(rt) and type(lt) is IntType:
                    return lc + rc + self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
            elif type(CodeGenVisitor.check_type) is FloatType:
                if type(lt) == type(rt):
                    if type(lt) is FloatType:
                        return lc + rc + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                    else:
                        return lc + self.emit.emitI2F(frame) + rc + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
                elif type(lt) is FloatType and type(rt) is IntType:
                    return lc + rc + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()

                elif type(lt) is IntType and type(rt) is FloatType:
                    return lc + self.emit.emitI2F(frame) + rc + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()
            else:
                if type(lt) == type(rt):
                    if type(lt) is IntType:
                        return lc + rc + self.emit.emitADDOP(ast.op, IntType(), frame), IntType()
                    else:
                        return lc + rc + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()

                elif type(lt) is FloatType and type(rt) is IntType:
                    return lc + rc + self.emit.emitI2F(frame) + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()

                elif type(lt) is IntType and type(rt) is FloatType:
                    return lc + self.emit.emitI2F(frame) + rc + self.emit.emitADDOP(ast.op, FloatType(), frame), FloatType()

            if ast.op in ['*', '/']:
                lc, lt = self.visit(ast.left, Access(frame, o.sym, False, True))
                rc, rt = self.visit(ast.right, Access(frame, o.sym, False, False))
                if type(CodeGenVisitor.check_type) is IntType:
                    if type(lt) == type(rt) and type(lt) is IntType:
                        return lc + rc + self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
                elif type(CodeGenVisitor.check_type) is FloatType:
                    if type(lt) == type(rt):
                        if type(lt) is FloatType:
                            return lc + rc + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                        else:
                            return lc + self.emit.emitI2F(frame) + rc + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                    elif type(lt) is FloatType and type(rt) is IntType:
                        return lc + rc + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                    elif type(lt) is IntType and type(rt) is FloatType:
                        return lc + self.emit.emitI2F(frame) + rc + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                else:
                    if type(lt) == type(rt):
                        if type(lt) is IntType:
                            return lc + rc + self.emit.emitMULOP(ast.op, IntType(), frame), IntType()
                        else:
                            return lc + rc + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                    elif type(lt) is FloatType and type(rt) is IntType:
                        return lc + rc + self.emit.emitI2F(frame) + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                    elif type(lt) is IntType and type(rt) is FloatType:
                        return lc + self.emit.emitI2F(frame) + rc + self.emit.emitMULOP(ast.op, FloatType(), frame), FloatType()
                
            elif op == "%":
                if type(inlt) is IntType and type(inrt) is IntType:
                    # print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
                    # print((inle + inre + self.emit.emitMOD(frame),inlt))
                    # print(frame.getStackSize())
                    return (inle + inre + self.emit.emitMOD(frame),inlt)
            elif op in ["&&" , "||"]: 
                falseLabel = frame.getNewLabel()
                truLabel = frame.getNewLabel()
                endLabel = frame.getNewLabel()
                buff = list()

                buff.append(inle)
                if(op == "&&"):
                    buff.append(self.emit.emitIFEQ(falseLabel,frame))
                else:
                    buff.append(self.emit.emitIFNE(truLabel,frame))

                buff.append(inre)
                buff.append(self.emit.emitIFEQ(falseLabel,frame))
                buff.append(self.emit.emitLABEL(truLabel,frame))
                buff.append(self.emit.emitPUSHICONST(1,frame))
                buff.append(self.emit.emitGOTO(endLabel,frame))
                buff.append(self.emit.emitLABEL(falseLabel,frame))
                buff.append(self.emit.emitPUSHICONST(0,frame))
                buff.append(self.emit.emitLABEL(endLabel,frame))
                frame.pop()
                # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
                # print(buff)
                return (''.join(buff), BoolType())
            
            elif op in [">" , "<" , "<=" , ">=" ,"==" , "!="]:
                if type(inlt) is type(inrt):
                    return (inle + inre +self.emit.emitREOP(op,inlt,frame),BoolType())
                if type(inlt) is IntType and type(inrt) is FloatType:
                    return (inle + self.emit.emitI2F(frame)+inre+self.emit.emitREOP(op,inrt,frame),BoolType())
                else: return(inle+inre+self.emit.emitI2F(frame)+self.emit.emitREOP(op,inlt,frame),BoolType())
                
            else: raise IllegalOperandException(str(ast))
        
        else : 
            if type(ast.left) is ArrayCell :
                left = self.visit(ast.left,Access(frame,nenv,True,ctxt.isFirst))
                right =  self.visit(ast.right,Access(frame,nenv,False,False))

                inre = right[0]
                inrt = self.getTypeP(right[1])
                inle = left[0]
                inlt = self.getType(left[1])
                print(type(inlt) is type(inrt))
                if type(inlt) is type(inrt):
                    if ctxt.isLeft == False and ctxt.isFirst == True:
                        store = self.emit.emitASTORE(self.getTypeP(left[1]),frame)
                        return (inle+inre+store,inlt)
                    elif ctxt.isLeft == False and ctxt.isFirst == False:
                        return (inle+inre+self.emit.emitDUPX2(frame)+self.emit.emitASTORE(self.getTypeP(left[1]),frame),inlt)
                    else: return (inle+inre,inlt)
                    

                elif type(inlt) is FloatType and type(inrt) is IntType:
                    if ctxt.isLeft == False and ctxt.isFirst == True:
                        return (inle+inre+self.emit.emitI2F(frame)+self.emit.emitASTORE(self.getTypeP(left[1]),frame),inlt)
                    elif ctxt.isLeft == False and ctxt.isFirst == False:
                        return (inle+inre+self.emit.emitI2F(frame)+self.emit.emitDUPX2(frame)+self.emit.emitASTORE(self.getTypeP(left._2),frame),inlt)

                    else:
                        return (inle+inre,inlt)
                # else: raise IllegalOperandException("")
            else:
                right = self.visit(ast.right,Access(frame,nenv,False,False))
                left = self.visit(ast.left,Access(frame,nenv,True,ctxt.isFirst))
                inre = right[0]
                inrt = self.getTypeP(right[1])
                inle = left[0]
                inlt = self.getType(left[1])
                if type(inlt) is FloatType and type(inrt) is IntType:
                    return (inre+self.emit.emitI2F(frame)+inle,inlt)
                else: return  (inre+inle,inlt)
            

    def visitUnaryOp(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        op = ast.op

        (be,bt) = self.visit(ast.body,Access(frame,nenv,False,False))
        et = self.getTypeP(bt)
        
        if op == "-" : return (be+self.emit.emitNEGOP(et,frame),bt)
        elif op == "!" : return (be+self.emit.emitNOT(et,frame),BoolType())
        else: return IllegalOperandException(str(ast))
    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        in_ = (list(), list())
        for x in ast.param:
            # print(x)
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + [str1], in_[1]+[typ1])
        # print(type(in_[1]).__name__)
        listT =list(zip(list(zip(ctype.partype,in_[1])),in_[0]))
        # print(listT)
        emitpara =""
        for x in listT:
            if type(x[0][0]) is FloatType and type(x[0][1]) is IntType:
                emitpara = emitpara + x[1] + self.emit.emitI2F(frame)
            else: 
                # print(x[1])
                emitpara = emitpara + x[1]
                
         
        # print(frame.getStackSize())
        # print("before CallExpr: stack = " + str(frame.getStackSize()))
        emits = emitpara+self.emit.emitINVOKESTATIC(cname+"/"+ast.method.name,ctype,frame)
        # print("end CallExpr: stack = "+str(frame.getStackSize()))
        return (emits, ctype)
    def visitId(self,ast, c): 
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.name,nenv,lambda x :x.name)
        isInit = sym.isInit
        ctype = self.getType(sym.mtype)
        print(sym.isInit)
        if(isinstance(sym.value,Index)): 
            print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
            cindex = sym.value.value

            if ctxt.isLeft == True and ctxt.isFirst == True:
                sym.isInit = True
                return (self.emit.emitWRITEVAR(ast.name,ctype,cindex,frame),sym.mtype)
                
            if ctxt.isLeft == True and ctxt.isFirst == False:
                sym.isInit = True
                return (self.emit.emitDUP(frame)+self.emit.emitWRITEVAR(ast.name,ctype,cindex,frame),sym.mtype)
            else:
                return (self.emit.emitREADVAR(ast.name,ctype,cindex,frame),sym.mtype)

        else:
            cfield = sym.value.value
            if ctxt.isLeft == True and ctxt.isFirst == True:
                return (self.emit.emitPUTSTATIC(cfield+"."+ast.name,ctype,frame),sym.mtype)

            if ctxt.isLeft == True and ctxt.isFirst == False:
                return (self.emit.emitDUP(frame)+self.emit.emitPUTSTATIC(cfield+"."+ast.name,ctype,frame),sym.mtype)
            else: 
                return (self.emit.emitGETSTATIC(cfield+"."+ast.name,ctype,frame),sym.mtype)
      
    def visitArrayCell(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        
        (arr,arrt) = self.visit(ast.arr,Access(frame,nenv,False,False))
        (idx,idxt) = self.visit(ast.idx,Access(frame,nenv,False,False))
        if type(arrt) is ArrayType:
            inType = arrt.eleType
        elif type(arrt) is ArrayPointerType: inType = arrt.eleType
        elif type(arrt) is MType: 
            if type(arrt.rettype) is ArrayPointerType: 
                inType = arrt.rettype.eletype
            else: inType =arrt.rettype
        else: inType = arrt
 
        if(not ctxt.isLeft):
            return (arr+idx+self.emit.emitALOAD(inType,frame),inType)  
        else:
            return (arr+idx,inType)
    def visitBlock(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        vari = ("",SubBody(frame,nenv))
        for x in ast.member:
            if type(x) is VarDecl:
                (str1 ,sym) = self.visit(x,vari[1])
                vari = (vari[0]+ str1 ,SubBody(frame,[sym] + vari[1].sym))
                
            else:
                local = vari[1].sym
                # print(isinstance(x,Expr))
                if isinstance(x,Expr):
                    expr = self.visit(x,Access(frame,local,False,True))
                    self.emit.printout(expr[0])
                else:
                    self.visit(x,SubBody(frame,local))
        
        
    
    def visitIf(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        condition = self.visit(ast.expr,Access(frame,nenv,False,False))

        if type(self.getTypeP(condition[1])) is BoolType :
            # print("GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
            # print(condition)
            self.emit.printout(condition[0])

            labelF = frame.getNewLabel()

            self.emit.printout(self.emit.emitIFFALSE(labelF,frame))
            if isinstance(ast.thenStmt,Expr):
                self.emit.printout(self.visit(ast.thenStmt,Access(frame,nenv,False,True))[0])
            else:
                self.visit(ast.thenStmt,SubBody(frame,nenv))

            if ast.elseStmt is not None :
                labelT = frame.getNewLabel()

                self.emit.printout(self.emit.emitGOTO(labelT,frame) + self.emit.emitLABEL(labelF,frame))
                if isinstance(ast.elseStmt,Expr):
                    self.emit.printout(self.visit(ast.elseStmt,Access(frame,nenv,False,True))[0])
                else:
                    self.visit(ast.elseStmt,SubBody(frame,nenv))
                self.emit.printout(self.emit.emitLABEL(labelT,frame))
                
            else: 
                self.emit.printout(self.emit.emitLABEL(labelF,frame))

        else: raise IllegalOperandException(ast.expr+"")

        if frame.getStackSize()>1: frame.pop()

    def visitFor(self,ast,c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym
        frame.enterScope(False)
        frame.enterLoop()
        expr1 = self.visit(ast.expr1, Access(frame,nenv,False,True))
        condition = self.visit(ast.expr2,Access(frame,nenv,False,False))
        if type(condition[1]) is BoolType:
            self.emit.printout(expr1[0])
            labelLoop = frame.getStartLabel()
            labelF = frame.getBreakLabel()
            self.emit.printout(self.emit.emitLABEL(labelLoop,frame))
            self.emit.printout(condition[0])
            self.emit.printout(self.emit.emitIFFALSE(labelF,frame))

            if isinstance(ast.loop,Expr):
                self.emit.printout(self.visit(ast.loop,Access(frame,nenv,False,True))[0])
            else:
                self.visit(ast.loop,SubBody(frame,nenv))
            expr3 = self.visit(ast.expr3,Access(frame,nenv,False,True))

            self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(),frame))

            self.emit.printout(expr3[0])

            self.emit.printout(self.emit.emitGOTO(labelLoop,frame))

            self.emit.printout(self.emit.emitLABEL(labelF,frame))

            self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
            
        else: raise IllegalOperandException(ast.expr1+"")
        frame.exitLoop()
        frame.exitScope()
  
    
    def visitBreak(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        self.emit.printout(emit.emitGOTO(frame.getBreakLabel(),frame))


    def visitContinue(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))
    

    def visitReturn(self,ast, c):

        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym

        if ast.expr is not None :
            x = self.visit(ast.expr, Access(frame,nenv,False,False))
        else: x = ("", VoidType())

     
        res = self.lookup("0_ret",nenv,lambda x : x.name) 
        # if res is not None: 
        #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        #     ret = res.mtype
        # else: ret = VoidType()
        ret = res.mtype
        # print("")
        # print("##############################################")
        # print(type(ret).__name__)
        if type(ret) is FloatType and type(self.getTypeP(x[1])) is IntType:
            self.emit.printout(x[0] + self.emit.emitI2F(frame) + self.emit.emitGOTO(1,frame))
        else:
            self.emit.printout(x[0] + self.emit.emitGOTO(1,frame))
        # if type(ret) is not VoidType:
        #     print("Void")
            # frame.pop()
    def visitDowhile(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        nenv = ctxt.sym

        frame.enterScope(False)
        frame.enterLoop()

        labelLoop = frame.getStartLabel()
        labelF = frame.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(labelLoop,frame))
        for x in ast.sl:
            if isinstance(x,Expr):
                expr = self.visit(x,Access(frame,nenv,True,True))
                self.emit.printout(expr[0])

            else:
                self.visit(x,SubBody(frame,nenv))

        exp = self.visit(ast.exp,Access(frame,nenv,True,True))

        self.emit.printout(self.emit.emitLABEL(frame.getContinueLabel(),frame))

        self.emit.printout(exp[0])

        self.emit.printout(self.emit.emitIFTRUE(labelLoop,frame))

        self.emit.printout(self.emit.emitLABEL(labelF,frame))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))

        frame.exitLoop()
        frame.exitScope()
    

    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any

        ctxt = o
        frame = ctxt.frame
        return (self.emit.emitPUSHICONST(ast.value, frame), IntType())
    def visitFloatLiteral(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        return (self.emit.emitPUSHFCONST(str(float(ast.value)), frame),FloatType()) 
  

    def visitStringLiteral(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        return (self.emit.emitPUSHCONST("\""+ast.value+"\"", StringType(), frame),StringType())


    def visitBooleanLiteral(self,ast, c):
        ctxt = c
        frame = ctxt.frame
        # print("SSSSSSSSSSSSSSSSSSSSSSSS")
        return (self.emit.emitPUSHICONST(str(ast.value).lower(), frame),BoolType())

    
