.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static divBy2(I)Z
.var 0 is arg0 I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
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
	invokestatic MCClass/divBy2(I)Z
	dup
	ifgt Label2
	iconst_4
	invokestatic MCClass/divBy2(I)Z
	ior
Label2:
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
