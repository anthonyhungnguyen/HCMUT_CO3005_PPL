.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label2 to Label1
Label2:
.var 2 is i I from Label3 to Label1
Label3:
	iconst_1
	istore_1
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
	iconst_4
	if_icmpgt Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
	iload_1
	iconst_2
	iadd
	istore_1
	goto Label4
Label5:
	iload_1
	i2f
	invokestatic io/putFloat(F)V
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
