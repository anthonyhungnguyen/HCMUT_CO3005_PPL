.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getDouble(I)I
.var 0 is arg0 I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	imul
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	iconst_2
	invokestatic MCClass/getMaxDouble(II)I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static getMaxDouble(II)I
.var 0 is arg0 I from Label0 to Label1
.var 1 is arg1 I from Label0 to Label1
Label0:
Label6:
	iload_0
	iload_1
	if_icmple Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	ifle Label2
	iload_0
	invokestatic MCClass/getDouble(I)I
	goto Label1
Label2:
	iload_1
	invokestatic MCClass/getDouble(I)I
	goto Label1
Label1:
	ireturn
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
