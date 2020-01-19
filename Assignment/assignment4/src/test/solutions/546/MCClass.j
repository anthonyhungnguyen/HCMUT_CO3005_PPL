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
	iconst_1
	dup
	istore_1
	istore_2
	iconst_2
	iconst_3
	imul
	iload_1
	isub
	dup
	istore_2
	istore_1
	iload_1
	iconst_1
	iadd
	iconst_2
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	dup
	ifgt Label6
	iload_2
	iconst_1
	isub
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ior
Label6:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
.limit locals 3
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
