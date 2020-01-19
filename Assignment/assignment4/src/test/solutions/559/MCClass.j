.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static sum(II)I
.var 0 is arg0 I from Label0 to Label1
.var 1 is arg1 I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
.var 2 is b I from Label3 to Label1
Label3:
	iconst_1
	dup
	istore_2
	istore_1
	iload_1
	iconst_1
	iadd
	istore_2
	iload_1
	iload_2
	invokestatic MCClass/sum(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
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
