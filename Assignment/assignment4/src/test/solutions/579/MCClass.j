.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static getText(I)Ljava/lang/String;
.var 0 is arg0 I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	irem
	iconst_0
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	ldc "so chan"
	goto Label1
	goto Label3
Label2:
	ldc "so le"
	goto Label1
Label3:
Label1:
	areturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	invokestatic MCClass/getText(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_1
	invokestatic MCClass/getText(I)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
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
