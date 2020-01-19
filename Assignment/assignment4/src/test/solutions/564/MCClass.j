.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static add(F)F
.var 0 is arg0 F from Label0 to Label1
Label0:
	fload_0
	iconst_1
	i2f
	fadd
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
	iconst_3
	istore_1
	iconst_3
	i2f
	invokestatic MCClass/add(F)F
	invokestatic MCClass/add(F)F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
.limit locals 2
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
