.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label2 to Label1
Label2:
Label15:
Label22:
Label17:
Label9:
	iconst_0
	istore_1
	goto Label5
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
Label5:
	iload_1
	bipush 12
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
	iload_1
	bipush 8
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
	goto Label4
	goto Label11
Label10:
	iload_1
	iconst_5
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label18
	iconst_2
	iload_1
	imul
	iconst_1
	iadd
	istore_1
Label18:
Label11:
	goto Label3
Label4:
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
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
