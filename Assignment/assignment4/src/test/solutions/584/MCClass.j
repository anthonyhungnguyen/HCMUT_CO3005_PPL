.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	dup
	ifgt Label2
	iconst_1
	ior
Label2:
	invokestatic io/putBool(Z)V
	iconst_1
	dup
	ifgt Label3
	iconst_0
	ior
Label3:
	invokestatic io/putBool(Z)V
	iconst_0
	dup
	ifgt Label4
	iconst_1
	ior
Label4:
	invokestatic io/putBool(Z)V
	iconst_0
	dup
	ifgt Label5
	iconst_0
	ior
Label5:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
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
