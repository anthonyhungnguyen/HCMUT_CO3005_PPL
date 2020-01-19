.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label2 to Label1
Label2:
	iconst_2
	dup
	istore_1
	putstatic MCClass.a I
	getstatic MCClass.a I
	iconst_3
	imul
	iconst_3
	isub
	istore_1
	getstatic MCClass.a I
	iload_1
	if_icmpge Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	invokestatic io/putBool(Z)V
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
