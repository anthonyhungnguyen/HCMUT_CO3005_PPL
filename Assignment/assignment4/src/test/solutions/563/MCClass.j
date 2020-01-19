.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static foo(F)F
.var 0 is arg0 F from Label0 to Label1
Label0:
	fload_0
	goto Label1
Label1:
	freturn
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	putstatic MCClass.a I
	iconst_3
	i2f
	invokestatic MCClass/foo(F)F
	invokestatic io/putFloat(F)V
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
