.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a F from Label2 to Label1
Label2:
.var 2 is b F from Label3 to Label1
Label3:
	iconst_3
	i2f
	fstore_2
	ldc 1.2
	ldc 2.0
	invokestatic MCClass/mul(FF)F
	fstore_1
	fload_2
	fload_1
	invokestatic MCClass/mul(FF)F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static mul(FF)F
.var 0 is arg0 F from Label0 to Label1
.var 1 is arg1 F from Label0 to Label1
Label0:
	fload_0
	fload_1
	fmul
	goto Label1
Label1:
	freturn
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
