.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static printNum(I)V
.var 0 is arg0 I from Label0 to Label1
Label0:
Label6:
	iload_0
	iconst_0
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
	iload_0
	invokestatic io/putInt(I)V
	iload_0
	iconst_1
	isub
	istore_0
	iload_0
	invokestatic MCClass/printNum(I)V
Label2:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 7
	invokestatic MCClass/printNum(I)V
Label1:
	return
.limit stack 1
.limit locals 1
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
