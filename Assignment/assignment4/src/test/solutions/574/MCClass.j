.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass.a I
Label12:
	getstatic MCClass.a I
	iconst_3
	if_icmpge Label3
	iconst_1
	goto Label4
Label3:
	iconst_0
Label4:
	dup
	ifle Label5
	getstatic MCClass.a I
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
Label5:
	dup
	ifle Label8
	getstatic MCClass.a I
	iconst_0
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	iand
Label8:
	ifle Label2
	iconst_5
	putstatic MCClass.a I
Label2:
	getstatic MCClass.a I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 3
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
