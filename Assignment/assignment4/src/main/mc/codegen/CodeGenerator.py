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

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat",MType([],FloatType()),CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool",MType([BoolType()],VoidType()),CName(self.libName)),
    				Symbol("putBoolLn",MType([BoolType()],VoidType()),CName(self.libName)),
                    Symbol("putString", MType([StringType()],VoidType()),CName(self.libName)),
                    Symbol("putStringLn",MType([StringType()],VoidType()),CName(self.libName)),
    				Symbol("putLn",MType([],VoidType()),CName(self.libName))
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

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

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

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        nenv = self.env[:]
        e = SubBody(None, nenv)
        temp = []
        check = False
        for x in ast.decl:
        	if type(x) is VarDecl:
        		self.emit.printout(self.emit.emitATTRIBUTE(x.variable,x.varType,False,None)) 
        		e.sym.insert(0,Symbol(x.variable,x.varType,CName(self.className))) #
        	else:
        		e.sym.insert(0,Symbol(x.name.name,MType([y.varType for y in x.param],x.returnType),CName(self.className)))
        if check:
        	self.genMETHOD(FuncDecl(Id("<clinit>"),list(), VoidType(),Block(list())),temp,Frame("<clinit>", VoidType()))
        for x in ast.decl:
        	if not type(x) is VarDecl:
        		self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), nenv, Frame("<init>", VoidType()))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame
        isClinit = consdecl.name.name == "<clinit>"
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)
        isInst = not isInit and not isMain  
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        frame.enterScope(True)

        glenv = o
        # Generate code for parameter declarations
        # lst = []
        newtemp = []
        label = {}
        count = 0
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isClinit:
        	for x in glenv:
        		self.emit.printout(self.emit.emitPUSHICONST(x.mtype.dimen,frame))
        		self.emit.printout(self.emit.emitNEWARRAY(x.mtype.eleType))
        		self.emit.printout(self.emit.emitPUTSTATIC(x.value.value +"."+x.name,x.mtype,frame))
        	self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        	self.emit.printout(self.emit.emitENDMETHOD(frame))
        	return
        if isInst:
        	for x in consdecl.param:
        		temp1 = frame.getNewIndex()
        		self.emit.printout(self.emit.emitVAR(temp1, "arg"+str(count), x.varType, frame.getStartLabel(), frame.getEndLabel(), frame))
        		newtemp.append(Symbol(x.variable,x.varType,Index(temp1)))
        		count = count + 1
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        # if isMain:
        lst = newtemp + glenv
        for x in body.member:
        	if type(x) is VarDecl:
        		res = self.visit(x,SubBody(frame,lst))
        		lst.insert(0,res)
        	else:
        		temp , newtemp1 = self.visit(x,SubBody(frame,lst)) if type(x) is Block else self.visit(x,Access(frame,lst,True,True)) if (type(x) is BinaryOp and x.op == "=") else self.visit(x,Access(frame,lst,False,True))
        		self.emit.printout(temp)
        		# print(frame.getStackSize())
        		if frame.getStackSize() != 0:
        			self.emit.printout(self.emit.emitPOP(frame))


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any

        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        res = self.lookup(ast.name.name,subctxt.sym,lambda x:x.name)
        subctxt.sym.remove(res)
        subctxt.sym.append(res)
        self.genMETHOD(ast, subctxt.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)
    def visitVarDecl(self,ast,o):
    	ctxt = o
    	frame = ctxt.frame
    	nenv = ctxt.sym
    	temp = frame.getNewLabel()
    	newtemp = frame.getNewIndex()
    	self.emit.printout(self.emit.emitVAR(newtemp, ast.variable, ast.varType, temp, frame.getEndLabel(), frame))
    	self.emit.printout(self.emit.emitLABEL(temp,frame))
    	return Symbol(ast.variable,ast.varType,Index(newtemp))
    def visitId(self,ast,o):
    	ctxt = o
    	frame = ctxt.frame
    	nenv = ctxt.sym
    	res = self.lookup(ast.name,nenv,lambda x:x.name)
    	if type(ctxt) is SubBody:
    		return self.emit.emitREADVAR(ast.name,res.mtype,res.value.value,frame) , res.mtype
    	elif type(ctxt) is Access and ctxt.isLeft is False:
    		if ctxt.isFirst:
    			if type(res.value) is CName:
    				return self.emit.emitGETSTATIC(res.value.value + "." + res.name,res.mtype,frame) , res.mtype
    			return self.emit.emitREADVAR(ast.name,res.mtype,res.value.value,frame) , res.mtype
    		else:
    			# print(res.mtype)
    			return self.emit.emitALOAD(res.mtype.eleType,frame) , res.mtype.eleType
    	elif type(ctxt) is Access and ctxt.isLeft is True:
    		if ctxt.isFirst:
    			if type(res.value) is CName:
    				return self.emit.emitPUTSTATIC(res.value.value + "." + res.name,res.mtype,frame) , res.mtype
    			return self.emit.emitWRITEVAR(ast.name,res.mtype,res.value.value,frame) , res.mtype
    		else:
    			# print("FFFFF")
    			return self.emit.emitASTORE(res.mtype.eleType,frame) , res.mtype.eleType
    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        
        cname = sym.value.value
        ctype = sym.mtype
        if ctxt.isFirst:
        	in_ = ["", list()]
	        count = 0
	        for x in ast.param:
	        	str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
	        	if type(ctype.partype[count]) is FloatType and type(typ1) is IntType:
	        		str1 = str1 + self.emit.emitI2F(frame)
	        	in_[0] = in_[0] + str1
	        	in_[1].append(typ1)
	        	count = count + 1
	        
        	return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame) , ctype.rettype
        elif not ctxt.isFirst and ctxt.isLeft:
        	return self.emit.emitASTORE(ctype.rettype.eleType,frame) ,ctype.rettype.eleType
        elif not ctxt.isFirst and not ctxt.isLeft:
        	return self.emit.emitALOAD(ctype.rettype.eleType,frame) ,ctype.rettype.eleType
        	# print("ABC",frame.getStackSize())
    def visitBlock(self ,ast ,o):
    	ctxt = o
    	frame = ctxt.frame
    	nenv = ctxt.sym
    	lst = nenv[:]
    	frame.enterScope(False) # true only used for function block , inside is false
    	newlst = []
    	for x in ast.member:
    		if type(x) is VarDecl:
    			temp = self.visit(x,o)
    			lst.insert(0,temp)
    		else:
    			temp , newtemp = self.visit(x,SubBody(frame,lst)) if type(x) is Block else self.visit(x,Access(frame,lst,True,True)) if (type(x) is BinaryOp and x.op == "=") else self.visit(x,Access(frame,lst,False,True))
    			newlst.append(temp)
    			if frame.getStackSize() != 0:
    				newlst.append(self.emit.emitPOP(frame))
    	self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
    	frame.exitScope()
    	# print(frame.getMaxIndex())
    	return ''.join(newlst) , None
    def visitUnaryOp(self ,ast ,o):
    	op = ast.op
    	ctxt = o
    	frame = ctxt.frame
    	nenv =ctxt.sym
    	body , bodyType = self.visit(ast.body,Access(frame,nenv,False,True))
    	if op is "!":
    		# print(frame.getStackSize())
    		return  body + self.emit.emitNOT(bodyType,frame) , bodyType
    	else:
    		return body + self.emit.emitNEGOP(bodyType,frame) , bodyType
    def visitBinaryOp(self, ast, o):
        op = str(ast.op)
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        rhs = lhs =rightType =leftType = temp = newtemp = None
        if not op in ["&&","||"]:
	        if op == '=':
	        	# rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        	# lhs, leftType = self.visit(ast.left, Access(frame,nenv,True,True))
	        	# print(frame.getStackSize())
	        	if type(ast.left) is ArrayCell:
	        		
	        		lhs, leftType = self.visit(ast.left, Access(frame,nenv,True,True))
	        		
	        		# print("uuu",frame.getStackSize())
	        		rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        	else:
	        		if ctxt.isLeft:
	        			rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        			lhs, leftType = self.visit(ast.left, Access(frame,nenv,True,True))
	        		if not ctxt.isLeft:
	        			rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        			newtemp = self.emit.emitDUP(frame)
	        			lhs, leftType = self.visit(ast.left, Access(frame,nenv,True,True))
	        else:
	        	lhs, leftType = self.visit(ast.left, Access(frame,nenv,False,True))
	        	rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        # rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        if type(leftType) == type(rightType) == IntType:
	            resultType = IntType()
	        elif type(rightType) == FloatType and type(leftType) == IntType:
	            resultType = FloatType()
	            # print(lhs)
	            lhs = lhs + self.emit.emitI2F(frame)
	            # print(lhs)
	        elif type(leftType) == FloatType and type(rightType) == IntType:
	            resultType = FloatType()
	            rhs = rhs + self.emit.emitI2F(frame)
	        elif type(leftType) == type(rightType) == FloatType:
	            resultType = FloatType()
	        else:
	        	resultType = rightType

        if op in ['+', '-']:
            return lhs + rhs + self.emit.emitADDOP(op, resultType, frame), resultType
        elif op in ['*', '/']:
            return lhs + rhs + self.emit.emitMULOP(op, resultType, frame), resultType
        elif op in ['%']:
        	return lhs + rhs + self.emit.emitMOD(frame) , resultType
        elif op in ['=']:
        	# print(rhs + lhs)
        	if ctxt.isLeft:
        		if type(ast.left) is ArrayCell:
        			temp , leftType = self.visit(ast.left,Access(frame,nenv,True,False))
        			return lhs + rhs + temp , resultType
        		return rhs + lhs , resultType
        	else:
        		if type(ast.left) is ArrayCell:
        			temp , leftType = self.visit(ast.left,Access(frame,nenv,True,False))
        			newtemp = frame.push()
        			return lhs + rhs + temp + rhs , resultType
        		return rhs + newtemp + lhs ,resultType
        elif op in ['<=','>=','>','<','!=','==']:
        	return lhs + rhs + self.emit.emitREOP(op,resultType,frame) , BoolType()
        elif op in ['&&']:
        	lhs, leftType = self.visit(ast.left, Access(frame,nenv,False,True))
        	labelFalse = frame.getNewLabel()
        	lhs = lhs + self.emit.emitDUP(frame) + self.emit.emitIFFALSE(labelFalse,frame)
	        rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        lhs = lhs + rhs + self.emit.emitANDOP(frame) + self.emit.emitLABEL(labelFalse,frame)
	        return lhs , BoolType()
        	# return lhs + rhs + self.emit.emitANDOP(frame) , BoolType()
        elif op in ['||']:
        	lhs, leftType = self.visit(ast.left, Access(frame,nenv,False,True))
        	labelTrue = frame.getNewLabel()
        	lhs = lhs + self.emit.emitDUP(frame) + self.emit.emitIFTRUE(labelTrue,frame)
	        rhs, rightType = self.visit(ast.right, Access(frame,nenv,False,True))
	        lhs = lhs + rhs + self.emit.emitOROP(frame) + self.emit.emitLABEL(labelTrue,frame)
	        return lhs , BoolType()
        	# return lhs + rhs + self.emit.emitOROP(frame) , BoolType()
    def visitIf(self, ast,o):
    	ctxt = o
    	frame = ctxt.frame
    	nenv = ctxt.sym
    	store = None
    	if ast.elseStmt:
    		newLabel1 = frame.getNewLabel()
    		newLabel2 = frame.getNewLabel()
    		expr , exprType = self.visit(ast.expr,Access(frame,nenv,False,True))
    		expr = expr + self.emit.emitIFFALSE(newLabel1,frame)
    		thenStmt ,thenStmtType = self.visit(ast.thenStmt,SubBody(frame,nenv)) if type(ast.thenStmt) is Block else self.visit(ast.thenStmt,Access(frame,nenv,True,True)) if (type(ast.thenStmt) is BinaryOp and ast.thenStmt.op == "=") else self.visit(ast.thenStmt,Access(frame,nenv,False,True))
    		expr = expr + thenStmt
    		expr = expr + self.emit.emitGOTO(newLabel2,frame) + self.emit.emitLABEL(newLabel1,frame)
    		elseStmt , elseStmtType = self.visit(ast.elseStmt,SubBody(frame,nenv)) if type(ast.elseStmt) is Block else self.visit(ast.elseStmt,Access(frame,nenv,True,True)) if (type(ast.elseStmt) is BinaryOp and ast.elseStmt.op == "=") else self.visit(ast.elseStmt,Access(frame,nenv,False,True))
    		expr = expr + elseStmt + self.emit.emitLABEL(newLabel2,frame)
    		store = expr
    	else:
    		newLabel1 = frame.getNewLabel()
    		expr , exprType = self.visit(ast.expr,Access(frame,nenv,False,True))
    		expr = expr + self.emit.emitIFFALSE(newLabel1,frame)
    		thenStmt ,thenStmtType = self.visit(ast.thenStmt,SubBody(frame,nenv)) if type(ast.thenStmt) is Block else self.visit(ast.thenStmt,Access(frame,nenv,True,True)) if (type(ast.thenStmt) is BinaryOp and ast.thenStmt.op == "=") else self.visit(ast.thenStmt,Access(frame,nenv,False,True))
    		expr = expr + thenStmt + self.emit.emitLABEL(newLabel1,frame)
    		store = expr
    	return store , None
    def visitFor(self, ast ,o):
    	ctxt = o
    	frame = ctxt.frame
    	nenv = ctxt.sym
    	frame.enterLoop()
    	temp = frame.getNewLabel()
    	expr1 ,expr1Type = self.visit(ast.expr1,Access(frame,nenv,True,True))
    	expr1 = expr1 + self.emit.emitGOTO(temp,frame)

    	expr1 = expr1 + self.emit.emitLABEL(frame.getContinueLabel(),frame)
    	label = self.emit.emitLABEL(temp,frame)
    	expr2 , expr2Type = self.visit(ast.expr2,Access(frame,nenv,False,True))
    	
    	newtemp = self.emit.emitIFFALSE(frame.getBreakLabel(),frame)
    	loop , loopType = self.visit(ast.loop,SubBody(frame,nenv)) if type(ast.loop) is Block else self.visit(ast.loop,Access(frame,nenv,True,True)) if (type(ast.loop) is BinaryOp and ast.loop.op == "=") else self.visit(ast.loop,Access(frame,nenv,False,True))
    	# expr1 = expr1 + loop
    	
    	expr3 , expr3Type = self.visit(ast.expr3,Access(frame,nenv,True,True))
    	
    	store = expr1 + expr3 + label + expr2 + newtemp + loop + self.emit.emitGOTO(frame.getContinueLabel(),frame) + self.emit.emitLABEL(frame.getBreakLabel(),frame)
    	frame.exitLoop()
    	return store , None
    def visitDowhile(self ,ast ,o):
    	ctxt = o
    	frame = ctxt.frame
    	nenv = ctxt.sym
    	frame.enterLoop()
    	lst = nenv[:]
    	newtemp = frame.getNewLabel()
    	temp = ""
    	for x in ast.sl:
    		sl , slType = self.visit(x,SubBody(frame,lst)) if type(x) is Block else self.visit(x,Access(frame,lst,True,True)) if (type(x) is BinaryOp and x.op == "=") else self.visit(x,Access(frame,lst,False,True))
    		if type(sl) is Symbol:
    			lst.insert(0,sl)
    		else:
    			temp = temp + sl
    			if frame.getStackSize() != 0:
    				temp = temp + self.emit.emitPOP(frame)
    	exp , expType = self.visit(ast.exp,Access(frame,nenv,False,True))
    	st = self.emit.emitGOTO(newtemp,frame) + self.emit.emitLABEL(frame.getContinueLabel(),frame) + exp + self.emit.emitIFFALSE(frame.getBreakLabel(),frame) + self.emit.emitLABEL(newtemp,frame) + temp + self.emit.emitGOTO(frame.getContinueLabel(),frame) + self.emit.emitLABEL(frame.getBreakLabel(),frame)   
    	frame.exitLoop()
    	return st, None
    def visitBreak(self ,ast ,o):
    	ctxt = o
    	frame = ctxt.frame
    	return self.emit.emitGOTO(frame.getBreakLabel(),frame) , None
    def visitContinue(self, ast ,o):
    	ctxt = o
    	frame = ctxt.frame
    	return self.emit.emitGOTO(frame.getContinueLabel(),frame) , None
    def visitReturn(self, ast,o):
    	ctxt = o
    	frame = ctxt.frame
    	nenv = ctxt.sym
    	if ast.expr:
    		expr ,exprType = self.visit(ast.expr,Access(frame,nenv,False,True))
    		frame.pop()
    		if type(nenv[-1].mtype.rettype) is FloatType and type(exprType) is IntType:
    			expr = expr + self.emit.emitI2F(frame)
    		return expr + self.emit.emitGOTO(frame.endLabel[0],frame) , None
    	# return self.emit.emitRETURN(VoidType(),frame) ,None 
    	return self.emit.emitGOTO(frame.endLabel[0],frame) , None
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()
    def visitFloatLiteral(self, ast, o):
    	ctxt = o
    	frame = ctxt.frame
    	return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()
    def visitStringLiteral(self, ast, o):
    	ctxt = o
    	frame = ctxt.frame
    	return self.emit.emitPUSHCONST('"'+ast.value +'"',StringType(),frame), StringType()
    def visitBooleanLiteral(self, ast ,o):
    	ctxt = o
    	frame = ctxt.frame
    	# print(ast.value)
    	return self.emit.emitPUSHICONST(str(ast.value).lower(),frame) , BoolType()


    
