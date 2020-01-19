.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
	iconst_3
	iconst_5
	invokestatic MCClass/getPower(II)I
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static getPower(II)I
.var 0 is arg0 I from Label0 to Label1
.var 1 is arg1 I from Label0 to Label1
Label0:
.var 2 is i I from Label2 to Label1
Label2:
.var 3 is c I from Label3 to Label1
Label3:
	iconst_1
	istore_3
Label10:
	iconst_0
	istore_2
	goto Label6
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
Label6:
	iload_2
	iload_1
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	iload_3
	iload_0
	imul
	istore_3
	goto Label4
Label5:
	iload_3
	goto Label1
Label1:
	ireturn
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
