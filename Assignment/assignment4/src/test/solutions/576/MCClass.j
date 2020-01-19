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
	iconst_2
	istore_2
	iconst_2
	iload_2
	imul
	iconst_1
	isub
	istore_1
Label12:
Label14:
	iload_1
	iload_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	dup
	ifle Label8
	iload_1
	iconst_2
	iload_2
	imul
	iadd
	iconst_2
	if_icmplt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	iand
Label8:
	ifle Label4
	iload_2
	istore_1
	iconst_2
	iload_1
	imul
	iconst_1
	iadd
	istore_2
	goto Label5
Label4:
	iconst_2
	istore_1
	iconst_3
	istore_2
	iload_2
	iconst_1
	iadd
	istore_2
Label5:
	iload_1
	invokestatic io/putIntLn(I)V
	iload_2
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 4
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
