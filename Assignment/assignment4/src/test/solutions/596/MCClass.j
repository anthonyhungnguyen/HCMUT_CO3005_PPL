.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
	iconst_1
	istore_1
Label7:
	goto Label5
Label3:
	iload_1
	bipush 10
	if_icmpgt Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label4
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	iconst_5
	istore_1
	goto Label10
Label8:
	iload_1
	iconst_1
	iadd
	istore_1
Label10:
	iload_1
	bipush 12
	if_icmpgt Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifle Label9
	goto Label8
	goto Label8
Label9:
	goto Label4
	goto Label3
Label4:
	iload_1
	invokestatic io/putInt(I)V
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
