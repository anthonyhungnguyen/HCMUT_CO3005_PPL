.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label2 to Label1
Label2:
.var 2 is b I from Label3 to Label1
Label3:
	iconst_0
	i2f
	fstore_1
	iconst_1
	istore_2
Label11:
	fload_1
	iload_2
	i2f
	fcmpl
	iflt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	dup
	ifle Label7
	iload_2
	iconst_0
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
Label7:
	ifle Label4
	iconst_1
	invokestatic io/putInt(I)V
Label4:
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
