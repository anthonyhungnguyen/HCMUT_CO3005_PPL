.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static mul(II)I
.var 0 is arg0 I from Label0 to Label1
.var 1 is arg1 I from Label0 to Label1
Label0:
	iload_0
	iload_1
	imul
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_3
	invokestatic MCClass/mul(II)I
	iconst_4
	iconst_5
	invokestatic MCClass/mul(II)I
	iadd
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
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
