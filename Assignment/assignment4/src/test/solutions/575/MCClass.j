.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static z Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
.var 2 is b I from Label3 to Label1
Label3:
.var 3 is c F from Label4 to Label1
Label4:
	iconst_2
	istore_1
	iconst_3
	istore_2
Label10:
Label12:
	iload_1
	iload_2
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	iload_1
	iload_2
	invokestatic MCClass/sum(II)I
	i2f
	fstore_3
	goto Label6
Label5:
	iload_1
	iload_2
	invokestatic MCClass/mul(II)I
	i2f
	fstore_3
Label6:
	fload_3
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static sum(II)I
.var 0 is arg0 I from Label0 to Label1
.var 1 is arg1 I from Label0 to Label1
Label0:
.var 2 is result I from Label2 to Label1
Label2:
	iload_0
	iload_1
	iadd
	istore_2
	iload_2
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 3
.end method

.method public static mul(II)I
.var 0 is arg0 I from Label0 to Label1
.var 1 is arg1 I from Label0 to Label1
Label0:
.var 2 is result I from Label2 to Label1
Label2:
	iload_0
	iload_1
	imul
	istore_2
	iload_2
	goto Label1
Label1:
	ireturn
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
