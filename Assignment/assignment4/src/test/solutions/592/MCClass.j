.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MCClass.x I
Label14:
Label6:
	goto Label4
Label2:
	getstatic MCClass.x I
	bipush 6
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label3
Label4:
	getstatic MCClass.x I
	iconst_1
	iadd
	putstatic MCClass.x I
	getstatic MCClass.x I
	iconst_2
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	dup
	ifle Label10
	getstatic MCClass.x I
	iconst_4
	if_icmple Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	iand
Label10:
	ifle Label7
	goto Label3
Label7:
	goto Label2
Label3:
	getstatic MCClass.x I
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
