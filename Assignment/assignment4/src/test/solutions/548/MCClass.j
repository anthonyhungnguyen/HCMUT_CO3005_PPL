.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label2 to Label1
Label2:
.var 2 is c I from Label3 to Label1
Label3:
	iconst_1
	putstatic MCClass.a Z
	iconst_4
	istore_1
	iconst_2
	iload_1
	imul
	iconst_3
	isub
	istore_2
	iload_1
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	dup
	ifgt Label6
	iload_2
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ior
Label6:
	dup
	ifgt Label11
	getstatic MCClass.a Z
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ior
Label11:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
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
