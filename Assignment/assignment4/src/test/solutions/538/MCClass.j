.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
.var 2 is b I from Label3 to Label1
Label3:
.var 3 is c F from Label4 to Label1
Label4:
	bipush 13
	istore_1
	iconst_3
	istore_2
	iload_1
	iload_2
	irem
	i2f
	ldc 1.0
	iconst_2
	i2f
	fdiv
	fadd
	fstore_3
	fload_3
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
