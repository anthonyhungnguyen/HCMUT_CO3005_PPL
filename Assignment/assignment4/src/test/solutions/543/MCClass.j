.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label2 to Label1
Label2:
	iconst_2
	iconst_1
	isub
	dup
	istore_1
	i2f
	putstatic MCClass.a F
	getstatic MCClass.a F
	iload_1
	i2f
	ldc 1.2
	fadd
	fcmpl
	ifge Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	dup
	ifle Label5
	getstatic MCClass.a F
	iconst_3
	i2f
	fadd
	iload_1
	i2f
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
Label5:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
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
