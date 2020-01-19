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
.var 3 is c I from Label4 to Label1
Label4:
	iconst_1
	istore_1
	iconst_2
	istore_3
Label14:
Label9:
	goto Label7
Label5:
	iload_1
	iconst_5
	if_icmpge Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifle Label6
Label7:
	iconst_1
	istore_2
	goto Label12
Label10:
	iload_2
	iconst_5
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label11
Label12:
	iload_3
	iconst_2
	imul
	istore_3
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label10
Label11:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label5
Label6:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
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
