import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var1(self):
        input = """int x, y, x[4];
        """
        expect = """Program([VarDecl(x,IntType),VarDecl(y,IntType),VarDecl(x,ArrayType(IntType,4))])"""
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var2(self):
        input = """int x, y, k[4];
        """
        expect = """Program([VarDecl(x,IntType),VarDecl(y,IntType),VarDecl(k,ArrayType(IntType,4))])"""
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_var3(self):
        input = """ int x, y;
        float k[3]; 
        """
        expect = """Program([VarDecl(x,IntType),VarDecl(y,IntType),VarDecl(k,ArrayType(FloatType,3))])"""
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_if(self):
        input = """
        int main(){
            if(i > 2){
                int i;
            }
        } """
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(i),IntLiteral(2)),Block([VarDecl(i,IntType)]))]))])"""
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_if_else(self):
        input = """
        int main(){
            if(i > 2){
                int i;
            }else{
                z + 3;
                println(fsdf);
            }
        } """
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(i),IntLiteral(2)),Block([VarDecl(i,IntType)]),Block([BinaryOp(+,Id(z),IntLiteral(3)),CallExpr(Id(println),[Id(fsdf)])]))]))])"""
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_exp1(self):
        input = """
        int main(){
            i = 2;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("i"),IntLiteral(2))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_exp2(self):
        input = """
        int main(){
            i = 2 || 3;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([BinaryOp("=",Id("i"),BinaryOp("||",IntLiteral(2),IntLiteral(3)))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_exp3(self):
        input = """
        int main(){
            if (i == 2 && z != 2){

            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("&&",BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("!=",Id("z"),IntLiteral(2))),Block([]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_exp4(self):
        input = """
        int main(){
            if (i == 2 || z != 2){
                1 < 2 && 4 > 3;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("!=",Id("z"),IntLiteral(2))),Block([BinaryOp("&&",BinaryOp("<",IntLiteral(1),IntLiteral(2)),BinaryOp(">",IntLiteral(4),IntLiteral(3)))]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_exp5(self):
        input = """
        int main(){
            if (i > 2){
                1 <= 2 && 4 >= 3;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp(">",Id("i"),IntLiteral(2)),Block([BinaryOp("&&",BinaryOp("<=",IntLiteral(1),IntLiteral(2)),BinaryOp(">=",IntLiteral(4),IntLiteral(3)))]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_exp6(self):
        input = """
        int main(){
            if (i == 2 || z != 2){
                i = 5 + 3 - 2;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("!=",Id("z"),IntLiteral(2))),Block([BinaryOp("=",Id("i"),BinaryOp("-",BinaryOp("+",IntLiteral(5),IntLiteral(3)),IntLiteral(2)))]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_exp7(self):
        input = """
        int main(){
            if (i == 2 || z != 2){
                2 / 3 + 4 * 5;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("!=",Id("z"),IntLiteral(2))),Block([BinaryOp("+",BinaryOp("/",IntLiteral(2),IntLiteral(3)),BinaryOp("*",IntLiteral(4),IntLiteral(5)))]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_exp8(self):
        input = """
        int main(){
            if (i == 2 || z != 2){
                -8;
                !i;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("!=",Id("z"),IntLiteral(2))),Block([UnaryOp("-",IntLiteral(8)),UnaryOp("!",Id("i"))]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_exp9(self):
        input = """
        int main(){
            if (i == 2 || z != 2){
                foo(2)[3+x] = a[b[2]] +3;
            }
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(||,BinaryOp(==,Id(i),IntLiteral(2)),BinaryOp(!=,Id(z),IntLiteral(2))),Block([BinaryOp(=,ArrayCell(CallExpr(Id(foo),[IntLiteral(2)]),BinaryOp(+,IntLiteral(3),Id(x))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLiteral(2))),IntLiteral(3)))]))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_exp10(self):
        input = """
        int main(){
            if (i == 2 || z != 2){
                (1 + 2) * 3;
                5 / (1 - 3);
                (i = 6 * 3) * 2;
            }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([If(BinaryOp("||",BinaryOp("==",Id("i"),IntLiteral(2)),BinaryOp("!=",Id("z"),IntLiteral(2))),Block([BinaryOp("*",BinaryOp("+",IntLiteral(1),IntLiteral(2)),IntLiteral(3)),BinaryOp("/",IntLiteral(5),BinaryOp("-",IntLiteral(1),IntLiteral(3))),BinaryOp("*",BinaryOp("=",Id("i"),BinaryOp("*",IntLiteral(6),IntLiteral(3))),IntLiteral(2))]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_invocationexp(self):
        input = """
        void main(){
            println(sdfs);
            {
                read(abc);
            }
        } """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([CallExpr(Id(println),[Id(sdfs)]),Block([CallExpr(Id(read),[Id(abc)])])]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_for(self):
        input = """
        void main(){
            for(i = 1; i < 10; i + 1) foo();
        } """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),CallExpr(Id("foo"),[]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_for2(self):
        input = """
        void main(){
            for(i = 1; i < 10; i + 1) {
                foo();
                }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([CallExpr(Id("foo"),[])]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_for3(self):
        input = """
        void main(){
            for(i = 1; i < 10; i + 1) {
                int i;
                foo();
                }
        } """
        expect = "Program([FuncDecl(Id(main),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(+,Id(i),IntLiteral(1));Block([VarDecl(i,IntType),CallExpr(Id(foo),[])]))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_break(self):
        input = """
        void main(){
            for(i = 1; i < 10; i + 1) {
                break;
                }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([Break()]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_continue(self):
        input = """
        void main(){
            for(i = 1; i < 10; i + 1) {
                continue;
                }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([Continue()]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_complex(self):
        input = """
        void main(){
            for(i = 1; i < 10; i + 1) {
                continue;
                {
                    break;
                    foo(i, 2);
                }
                }
        } """
        expect = str(Program([FuncDecl(Id("main"),[],VoidType(),Block([For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),BinaryOp("+",Id("i"),IntLiteral(1)),Block([Continue(),Block([Break(),CallExpr(Id("foo"),[Id("i"),IntLiteral(2)])])]))]))]))
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    
    def test_arr_poi_type(self):
        input = """
        int[] foo(int a, float b[]) {} """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_complex1(self):
        input = """
        int[] foo(int a, float b[]) {
            int c[3];
            if (a>0) foo(a-1,b);
            return c; 
        } """
        expect = "Program([FuncDecl(Id(foo),[VarDecl(a,IntType),VarDecl(b,ArrayTypePointer(FloatType))],ArrayTypePointer(IntType),Block([VarDecl(c,ArrayType(IntType,3)),If(BinaryOp(>,Id(a),IntLiteral(0)),CallExpr(Id(foo),[BinaryOp(-,Id(a),IntLiteral(1)),Id(b)])),Return(Id(c))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
        
    def test_multiple_func_in_param(self):
        input = """
        int main(int c[]){
            foo();
            foo(foo());
            foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo())))))))))))))))));
        }"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([CallExpr(Id(foo),[]),CallExpr(Id(foo),[CallExpr(Id(foo),[])]),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[])])])])])])])])])])])])])])])])])])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    
    def test_multiple_empty_block(self):
        input = """
        int main(int c[]){
           {
               {
                   {
                       {
                           {
                               {
                                   {
                                       {
                                           {
                                               {

                                               }
                                           }
                                       }
                                   }
                               }
                           }
                       }
                   }
               }
           }
           {

           }
        }"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])])])]),Block([])]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_complicated_program(self):
        input = """
        int main(int c[]){
           for(i = 0; i < 10; i + 1){
               if(i < 10) return 0;
               else{
                   do
                        i + 1;
                        c[0] = foo(foo(foo(foo(foo(foo())))));
                    while
                        i > 100;
               }
           }
        }"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(+,Id(i),IntLiteral(1));Block([If(BinaryOp(<,Id(i),IntLiteral(10)),Return(IntLiteral(0)),Block([Dowhile([BinaryOp(+,Id(i),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(c),IntLiteral(0)),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[])])])])])]))],BinaryOp(>,Id(i),IntLiteral(100)))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_complicated_program1(self):
        input = """
        int main(int c[]){
           for(i = 0; i < 10; i + 1){
               if(i < 10) return 0;
               else{
                   do{
                       div(mul(sub(i[3], 10), 10), 10);
                       float j[4];
                   }
                        i + 1;
                        c[0] = foo(foo(foo(foo(foo(foo())))));
                    while
                        i > 100;
               }
           }
        }"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(+,Id(i),IntLiteral(1));Block([If(BinaryOp(<,Id(i),IntLiteral(10)),Return(IntLiteral(0)),Block([Dowhile([Block([CallExpr(Id(div),[CallExpr(Id(mul),[CallExpr(Id(sub),[ArrayCell(Id(i),IntLiteral(3)),IntLiteral(10)]),IntLiteral(10)]),IntLiteral(10)]),VarDecl(j,ArrayType(FloatType,4))]),BinaryOp(+,Id(i),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(c),IntLiteral(0)),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[])])])])])]))],BinaryOp(>,Id(i),IntLiteral(100)))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_complicated_program2(self):
        input = """
        int main(int c[]){
           for(i = 0; i < 10; i + 1){
               if(i < 10) {
                   return 0;
                   div(mul(sub(foo(func(rand(i[3], 10), 10), 10), c[10]), 10), 10);
                }
               else{
                   do{
                       div(mul(sub(i[3], 10), 10), 10);
                       float j[4];
                       {
                           print("hello world");
                       }
                       i + 1;
                        c[0] = foo(foo(foo(foo(foo(foo())))));
                   }
                    while i > 100;
               }
           }
        }"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(+,Id(i),IntLiteral(1));Block([If(BinaryOp(<,Id(i),IntLiteral(10)),Block([Return(IntLiteral(0)),CallExpr(Id(div),[CallExpr(Id(mul),[CallExpr(Id(sub),[CallExpr(Id(foo),[CallExpr(Id(func),[CallExpr(Id(rand),[ArrayCell(Id(i),IntLiteral(3)),IntLiteral(10)]),IntLiteral(10)]),IntLiteral(10)]),ArrayCell(Id(c),IntLiteral(10))]),IntLiteral(10)]),IntLiteral(10)])]),Block([Dowhile([Block([CallExpr(Id(div),[CallExpr(Id(mul),[CallExpr(Id(sub),[ArrayCell(Id(i),IntLiteral(3)),IntLiteral(10)]),IntLiteral(10)]),IntLiteral(10)]),VarDecl(j,ArrayType(FloatType,4)),Block([CallExpr(Id(print),[StringLiteral(hello world)])]),BinaryOp(+,Id(i),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(c),IntLiteral(0)),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[])])])])])]))])],BinaryOp(>,Id(i),IntLiteral(100)))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    def test_complicated_program3(self):
        input = """
        int main(int c[]){
           for(i = 0; i < 10; i + 1){
               if(i < 10) {
                   return 0;
                   div(mul(sub(foo(func(rand(i[3], 10), 10), 10), c[10]), 10), 10);
                }
               else{
                   do{
                       div(mul(sub(i[3], 10), 10), 10);
                       float j[4];
                       {
                           print("hello world");
                       }
                       i + 1;
                        c[0] = foo(foo(foo(foo(foo(foo())))));
                   }
                    while i > 100;
               }
           }
        }"""
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(+,Id(i),IntLiteral(1));Block([If(BinaryOp(<,Id(i),IntLiteral(10)),Block([Return(IntLiteral(0)),CallExpr(Id(div),[CallExpr(Id(mul),[CallExpr(Id(sub),[CallExpr(Id(foo),[CallExpr(Id(func),[CallExpr(Id(rand),[ArrayCell(Id(i),IntLiteral(3)),IntLiteral(10)]),IntLiteral(10)]),IntLiteral(10)]),ArrayCell(Id(c),IntLiteral(10))]),IntLiteral(10)]),IntLiteral(10)])]),Block([Dowhile([Block([CallExpr(Id(div),[CallExpr(Id(mul),[CallExpr(Id(sub),[ArrayCell(Id(i),IntLiteral(3)),IntLiteral(10)]),IntLiteral(10)]),IntLiteral(10)]),VarDecl(j,ArrayType(FloatType,4)),Block([CallExpr(Id(print),[StringLiteral(hello world)])]),BinaryOp(+,Id(i),IntLiteral(1)),BinaryOp(=,ArrayCell(Id(c),IntLiteral(0)),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[])])])])])]))])],BinaryOp(>,Id(i),IntLiteral(100)))]))]))]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    def test_program_many_declare(self):
        input = """
        int main(int c[]){}
        float[] func(int j){}
        """
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([])),FuncDecl(Id(func),[VarDecl(j,IntType)],ArrayTypePointer(FloatType),Block([]))])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_program_many_declare1(self):
        input = """
        int main(int c[]){}
        float[] func(int j){}
        int i,j,k;
        """
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([])),FuncDecl(Id(func),[VarDecl(j,IntType)],ArrayTypePointer(FloatType),Block([])),VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(k,IntType)])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_program_many_declare2(self):
        input = """
        int main(int c[]){}
        float[] func(int j){}
        int i,j,k;
        string f;
        float helloW;
        boolean isTrue;
        """
        expect = """Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([])),FuncDecl(Id(func),[VarDecl(j,IntType)],ArrayTypePointer(FloatType),Block([])),VarDecl(i,IntType),VarDecl(j,IntType),VarDecl(k,IntType),VarDecl(f,StringType),VarDecl(helloW,FloatType),VarDecl(isTrue,BoolType)])"""
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    def test_if1(self):
        input = """
        int main(){
            if(i > 2)
                if(j < 5)
                    if(k == 0)
                        i = 1;
                    else
                        j + 1;
                else
                    k - 1;
            else
                i + k;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(i),IntLiteral(2)),If(BinaryOp(<,Id(j),IntLiteral(5)),If(BinaryOp(==,Id(k),IntLiteral(0)),BinaryOp(=,Id(i),IntLiteral(1)),BinaryOp(+,Id(j),IntLiteral(1))),BinaryOp(-,Id(k),IntLiteral(1))),BinaryOp(+,Id(i),Id(k)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_if2(self):
        input = """
        int main(){
            if(i > 2)
                if(j < 5)
                    if(k == 0)
                        i = 1;
                    else
                        j + 1;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(i),IntLiteral(2)),If(BinaryOp(<,Id(j),IntLiteral(5)),If(BinaryOp(==,Id(k),IntLiteral(0)),BinaryOp(=,Id(i),IntLiteral(1)),BinaryOp(+,Id(j),IntLiteral(1)))))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_if3(self):
        input = """
        int main(){
            if(i > 2)
                if(j < 5)
                    if(k == 0)
                        i = 1;
                    else
                        if(m - 1 == 0)
                            return 0;
                        else
                            foo();
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>,Id(i),IntLiteral(2)),If(BinaryOp(<,Id(j),IntLiteral(5)),If(BinaryOp(==,Id(k),IntLiteral(0)),BinaryOp(=,Id(i),IntLiteral(1)),If(BinaryOp(==,BinaryOp(-,Id(m),IntLiteral(1)),IntLiteral(0)),Return(IntLiteral(0)),CallExpr(Id(foo),[])))))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_dowhile(self):
        input = """
        int main(){
            do
            {}
            while i + 1 = 0;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([])],BinaryOp(=,BinaryOp(+,Id(i),IntLiteral(1)),IntLiteral(0)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_dowhile1(self):
        input = """
        int main(){
            do
            {}{}{}
            while i + 1 = 0;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([]),Block([]),Block([])],BinaryOp(=,BinaryOp(+,Id(i),IntLiteral(1)),IntLiteral(0)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_dowhile2(self):
        input = """
        int main(){
            do
            {}{}{}
            i;
            while i + 1 = 0;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([]),Block([]),Block([]),Id(i)],BinaryOp(=,BinaryOp(+,Id(i),IntLiteral(1)),IntLiteral(0)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_dowhile3(self):
        input = """
        int main(){
            do
            {}{}{func(2);}
            i;
            foo(a[0]);
            while i + 1 = 0;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([Block([]),Block([]),Block([CallExpr(Id(func),[IntLiteral(2)])]),Id(i),CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(0))])],BinaryOp(=,BinaryOp(+,Id(i),IntLiteral(1)),IntLiteral(0)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_funcDecl(self):
        input = """
        int main(){}
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_funcDecl1(self):
        input = """
        int main(){}
        float[] func(int a){}
        void foo(string b[]){}
        """
        expect = """Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(func),[VarDecl(a,IntType)],ArrayTypePointer(FloatType),Block([])),FuncDecl(Id(foo),[VarDecl(b,ArrayTypePointer(StringType))],VoidType,Block([]))])"""
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_funcDecl2(self):
        input = """
        int main(){}
        float[] func(int a){}
        boolean isTrue;
        void foo(string b[], int c){
            isTrue = 1;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(func),[VarDecl(a,IntType)],ArrayTypePointer(FloatType),Block([])),VarDecl(isTrue,BoolType),FuncDecl(Id(foo),[VarDecl(b,ArrayTypePointer(StringType)),VarDecl(c,IntType)],VoidType,Block([BinaryOp(=,Id(isTrue),IntLiteral(1))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_LB_RB_exp(self):
        input = """
        int main(){
            (1 + 2) * 3 / 2;
        }
        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(/,BinaryOp(*,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),IntLiteral(2))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_math(self):
        input = """
        int main(){
            1 + 2 * 3 / 2;
        }
        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(+,IntLiteral(1),BinaryOp(/,BinaryOp(*,IntLiteral(2),IntLiteral(3)),IntLiteral(2)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_math1(self):
        input = """
        int main(){
            6 / 4 * 3 / 2;
        }
        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(/,BinaryOp(*,BinaryOp(/,IntLiteral(6),IntLiteral(4)),IntLiteral(3)),IntLiteral(2))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_math2(self):
        input = """
        int main(){
            6 / 4 * (3 / 2);
        }
        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(*,BinaryOp(/,IntLiteral(6),IntLiteral(4)),BinaryOp(/,IntLiteral(3),IntLiteral(2)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_math3(self):
        input = """
        int main(){
            6 % 4 + 3 * 2 - 9 / 8;
        }
        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(-,BinaryOp(+,BinaryOp(%,IntLiteral(6),IntLiteral(4)),BinaryOp(*,IntLiteral(3),IntLiteral(2))),BinaryOp(/,IntLiteral(9),IntLiteral(8)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_varDecl(self):
        input = """
        float a, b, i[1000], d[8099999458];
        """
        expect = "Program([VarDecl(a,FloatType),VarDecl(b,FloatType),VarDecl(i,ArrayType(FloatType,1000)),VarDecl(d,ArrayType(FloatType,8099999458))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_dowhile_if_else(self):
        input = """
        string[] main(int k[]){
            do
                if(i < 1)
                    j = j + 1;
                else
                    foo(j);
            while j < 100;
        }
        """
        expect = "Program([FuncDecl(Id(main),[VarDecl(k,ArrayTypePointer(IntType))],ArrayTypePointer(StringType),Block([Dowhile([If(BinaryOp(<,Id(i),IntLiteral(1)),BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1))),CallExpr(Id(foo),[Id(j)]))],BinaryOp(<,Id(j),IntLiteral(100)))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_for_if_else(self):
        input = """
        string[] main(int k[]){
            for(i = true; i < 100; i = false)
                if(!true)
                    if (x > -400)
                        x = 3 + -500;
                    else
                        x = -500;
        }
        """
        expect = "Program([FuncDecl(Id(main),[VarDecl(k,ArrayTypePointer(IntType))],ArrayTypePointer(StringType),Block([For(BinaryOp(=,Id(i),BooleanLiteral(true));BinaryOp(<,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BooleanLiteral(false));If(UnaryOp(!,BooleanLiteral(true)),If(BinaryOp(>,Id(x),UnaryOp(-,IntLiteral(400))),BinaryOp(=,Id(x),BinaryOp(+,IntLiteral(3),UnaryOp(-,IntLiteral(500)))),BinaryOp(=,Id(x),UnaryOp(-,IntLiteral(500))))))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_float_var(self):
        input = """
        int main(){
            i = 2345.35;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(i),FloatLiteral(2345.35))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    
    def test_string_var(self):
        input = """
        int main(){
            i = "sldkfjlsdfjlksdjfk";
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,Id(i),StringLiteral(sldkfjlsdfjlksdjfk))]))])"
        print(expect)
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_complex_program1(self):
        input = """float i[234];
        float main(float x, int n){ 
            float res; 
            for (i = 1; i < 5; i+1){ 
                k[0] = k[7457] * -1; 
                "somerandomstring" = "somerandomstring"; 
                res = res + sign * fact; 
            } 
            return res;  
        }"""
        expect = "Program([VarDecl(i,ArrayType(FloatType,234)),FuncDecl(Id(main),[VarDecl(x,FloatType),VarDecl(n,IntType)],FloatType,Block([VarDecl(res,FloatType),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(5));BinaryOp(+,Id(i),IntLiteral(1));Block([BinaryOp(=,ArrayCell(Id(k),IntLiteral(0)),BinaryOp(*,ArrayCell(Id(k),IntLiteral(7457)),UnaryOp(-,IntLiteral(1)))),BinaryOp(=,StringLiteral(somerandomstring),StringLiteral(somerandomstring)),BinaryOp(=,Id(res),BinaryOp(+,Id(res),BinaryOp(*,Id(sign),Id(fact))))])),Return(Id(res))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_complex_program2(self):
        input = """int main(){
		                    for(j=1; j<=i; j+6) {
			                    printString(k,"nn");
			                    k+4;
		                    }
		                    printString("w");
                    }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(j),IntLiteral(1));BinaryOp(<=,Id(j),Id(i));BinaryOp(+,Id(j),IntLiteral(6));Block([CallExpr(Id(printString),[Id(k),StringLiteral(nn)]),BinaryOp(+,Id(k),IntLiteral(4))])),CallExpr(Id(printString),[StringLiteral(w)])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_complex_program3(self):
        input = """int randomFunc(string s[], string c){
	                int length;
	                int i;
	                for(i=(2-1); i>=0; i-1){
	                }
	                return -1;	
                }"""
        expect = "Program([FuncDecl(Id(randomFunc),[VarDecl(s,ArrayTypePointer(StringType)),VarDecl(c,StringType)],IntType,Block([VarDecl(length,IntType),VarDecl(i,IntType),For(BinaryOp(=,Id(i),BinaryOp(-,IntLiteral(2),IntLiteral(1)));BinaryOp(>=,Id(i),IntLiteral(0));BinaryOp(-,Id(i),IntLiteral(1));Block([])),Return(UnaryOp(-,IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_complex_program4(self):
        input = """int main(){
	                int index;  
	                printString("Enter string: ");
	                func(func(func(func(10, c[2], k[f[5]]), c[4]), 454), k[j[6]]);
	                index;
	                
                }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(index,IntType),CallExpr(Id(printString),[StringLiteral(Enter string: )]),CallExpr(Id(func),[CallExpr(Id(func),[CallExpr(Id(func),[CallExpr(Id(func),[IntLiteral(10),ArrayCell(Id(c),IntLiteral(2)),ArrayCell(Id(k),ArrayCell(Id(f),IntLiteral(5)))]),ArrayCell(Id(c),IntLiteral(4))]),IntLiteral(454)]),ArrayCell(Id(k),ArrayCell(Id(j),IntLiteral(6)))]),Id(index)]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_complex_program5(self):
        input = """int main(){	
	                string alps[26];
                    int i;
	                do {
		                temp = rand() % 26;
		                i=i+1;
	                }
                    while ( k<20);
                }"""
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(alps,ArrayType(StringType,26)),VarDecl(i,IntType),Dowhile([Block([BinaryOp(=,Id(temp),BinaryOp(%,CallExpr(Id(rand),[]),IntLiteral(26))),BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)))])],BinaryOp(<,Id(k),IntLiteral(20)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_complex_program6(self):
        input = """void nextNum(string num[]){  
	                int i,j;
	                for(i=size-1;i>0;i-1){
		                break;
	                }
	                
	                int x,num[1],smaller,i;
	                return ;
                }"""
        expect = """Program([FuncDecl(Id(nextNum),[VarDecl(num,ArrayTypePointer(StringType))],VoidType,Block([VarDecl(i,IntType),VarDecl(j,IntType),For(BinaryOp(=,Id(i),BinaryOp(-,Id(size),IntLiteral(1)));BinaryOp(>,Id(i),IntLiteral(0));BinaryOp(-,Id(i),IntLiteral(1));Block([Break()])),VarDecl(x,IntType),VarDecl(num,ArrayType(IntType,1)),VarDecl(smaller,IntType),VarDecl(i,IntType),Return()]))])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_complex_program7(self):
        input = """int main()
                    {
                        if (x>=y) x=1;
                        if (x<=y) x=2;
                        if (x!=y) x=3;
                    }
                """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([If(BinaryOp(>=,Id(x),Id(y)),BinaryOp(=,Id(x),IntLiteral(1))),If(BinaryOp(<=,Id(x),Id(y)),BinaryOp(=,Id(x),IntLiteral(2))),If(BinaryOp(!=,Id(x),Id(y)),BinaryOp(=,Id(x),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_complex_program8(self):
        input = """int main()
                    {
                        do z = 1 ; while x && y = z; 
                    }
                """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([BinaryOp(=,Id(z),IntLiteral(1))],BinaryOp(=,BinaryOp(&&,Id(x),Id(y)),Id(z)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_complex_program9(self):
        input = """int main()
                    {
                        do z = 1 ; while x;
                    }
                """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Dowhile([BinaryOp(=,Id(z),IntLiteral(1))],Id(x))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_complex_program10(self):
        input = """int main()
                    {
                       z[3] = x[2] + 3;
                    }
                """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(Id(z),IntLiteral(3)),BinaryOp(+,ArrayCell(Id(x),IntLiteral(2)),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_complex_program11(self):
        input = """int main()
                    {
                       z[t[3+a]] = x[y[2]] +3;
                    }
                """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([BinaryOp(=,ArrayCell(Id(z),ArrayCell(Id(t),BinaryOp(+,IntLiteral(3),Id(a)))),BinaryOp(+,ArrayCell(Id(x),ArrayCell(Id(y),IntLiteral(2))),IntLiteral(3)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_complex_program12(self):
        input = """ int main(){
                    int i, s, ro, k;
	                for(i=1; i<=randomNumber; i+1){
		            do {
			            printString("* ");
			            k+1;
		            }
                    while(k!=(2*i-1));
		            printString("n");
	            }
	            return 0;
                } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),VarDecl(s,IntType),VarDecl(ro,IntType),VarDecl(k,IntType),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<=,Id(i),Id(randomNumber));BinaryOp(+,Id(i),IntLiteral(1));Block([Dowhile([Block([CallExpr(Id(printString),[StringLiteral(* )]),BinaryOp(+,Id(k),IntLiteral(1))])],BinaryOp(!=,Id(k),BinaryOp(-,BinaryOp(*,IntLiteral(2),Id(i)),IntLiteral(1)))),CallExpr(Id(printString),[StringLiteral(n)])])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))
    
    def test_complex_program13(self):
        input = """ int main(){
            int size;
	        for(i=0; i<size; i+1) {
		        printString("n");
	        }
	        return 0;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(size,IntType),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),Id(size));BinaryOp(+,Id(i),IntLiteral(1));Block([CallExpr(Id(printString),[StringLiteral(n)])])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))
    
    def test_complex_program14(self):
        input = """ int main(){
	        for(i=0;i<58;i+1){	
		        if(count1[i]<count2[i]){
			        ans=false;
			        break;
		        }
	        }
	        if(ans)           
		        printString("Yes",endl);
	        return 0;
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(58));BinaryOp(+,Id(i),IntLiteral(1));Block([If(BinaryOp(<,ArrayCell(Id(count1),Id(i)),ArrayCell(Id(count2),Id(i))),Block([BinaryOp(=,Id(ans),BooleanLiteral(false)),Break()]))])),If(Id(ans),CallExpr(Id(printString),[StringLiteral(Yes),Id(endl)])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_complex_program15(self):
        input = """string pName[30];
            int  qty[3];
            int  i; 
            int main(){
                printString(setw(30),"Product Name",setw(20),"Quantity",endl);
                for(i=0; i< 3; i+1){
                    printString(setw(30),setfill("-"),pName[i],setw(20),setfill("#"),qty[i],endl);
                }
            return 0;
        } """
        expect = "Program([VarDecl(pName,ArrayType(StringType,30)),VarDecl(qty,ArrayType(IntType,3)),VarDecl(i,IntType),FuncDecl(Id(main),[],IntType,Block([CallExpr(Id(printString),[CallExpr(Id(setw),[IntLiteral(30)]),StringLiteral(Product Name),CallExpr(Id(setw),[IntLiteral(20)]),StringLiteral(Quantity),Id(endl)]),For(BinaryOp(=,Id(i),IntLiteral(0));BinaryOp(<,Id(i),IntLiteral(3));BinaryOp(+,Id(i),IntLiteral(1));Block([CallExpr(Id(printString),[CallExpr(Id(setw),[IntLiteral(30)]),CallExpr(Id(setfill),[StringLiteral(-)]),ArrayCell(Id(pName),Id(i)),CallExpr(Id(setw),[IntLiteral(20)]),CallExpr(Id(setfill),[StringLiteral(#)]),ArrayCell(Id(qty),Id(i)),Id(endl)])])),Return(IntLiteral(0))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))
        
    def test_complex_program16(self):
        input = """ int main(){
            {
                if (this != b) {
                    return helloWorld();
                    helloWorld() = new[i];
                }
                return this;
            }
        } """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([Block([If(BinaryOp(!=,Id(this),Id(b)),Block([Return(CallExpr(Id(helloWorld),[])),BinaryOp(=,CallExpr(Id(helloWorld),[]),ArrayCell(Id(new),Id(i)))])),Return(Id(this))])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))
    
    def test_complex_program17(self):
        input = """
        int main(int c[]){
            foo();
            foo(foo());
            foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo(foo())))))))))))));
        }"""
        expect = "Program([FuncDecl(Id(main),[VarDecl(c,ArrayTypePointer(IntType))],IntType,Block([CallExpr(Id(foo),[]),CallExpr(Id(foo),[CallExpr(Id(foo),[])]),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[])])])])])])])])])])])])])])]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_complex_program18(self):
        input = """
        int main(){}
        float sort(int i[], float k[]){}
        
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([])),FuncDecl(Id(sort),[VarDecl(i,ArrayTypePointer(IntType)),VarDecl(k,ArrayTypePointer(FloatType))],FloatType,Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_complex_program19(self):
        input = """
        int main(){
            int i;
            j + 1 = (9 + 1) * 2;
        }
        """
        expect = "Program([FuncDecl(Id(main),[],IntType,Block([VarDecl(i,IntType),BinaryOp(=,BinaryOp(+,Id(j),IntLiteral(1)),BinaryOp(*,BinaryOp(+,IntLiteral(9),IntLiteral(1)),IntLiteral(2)))]))])"
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_complex_program20(self):
        input = """
		int a[5],b[6];
		
		void abc(int x, float y) {
			x = x*x;
			y = y*y;
		}
		void main() {
			a = a + a;
			b = b + b;
		}
		"""
        expect = "Program([VarDecl(a,ArrayType(IntType,5)),VarDecl(b,ArrayType(IntType,6)),FuncDecl(Id(abc),[VarDecl(x,IntType),VarDecl(y,FloatType)],VoidType,Block([BinaryOp(=,Id(x),BinaryOp(*,Id(x),Id(x))),BinaryOp(=,Id(y),BinaryOp(*,Id(y),Id(y)))])),FuncDecl(Id(main),[],VoidType,Block([BinaryOp(=,Id(a),BinaryOp(+,Id(a),Id(a))),BinaryOp(=,Id(b),BinaryOp(+,Id(b),Id(b)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,375))
    
    def test_complex_program21(self):
        input = """void abc() {
			int i,j;
			for(i = 1;i < 100;i = i*10)
			{
				do
					if(j == 15)
						break;
					if(j == 20)
						continue;
					j = j*2;
				while j <= 25;
				if(i == 50)
					return j;
				if(j == 25)
					return i;
			}
			return;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([VarDecl(i,IntType),VarDecl(j,IntType),For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(10)));Block([Dowhile([If(BinaryOp(==,Id(j),IntLiteral(15)),Break()),If(BinaryOp(==,Id(j),IntLiteral(20)),Continue()),BinaryOp(=,Id(j),BinaryOp(*,Id(j),IntLiteral(2)))],BinaryOp(<=,Id(j),IntLiteral(25))),If(BinaryOp(==,Id(i),IntLiteral(50)),Return(Id(j))),If(BinaryOp(==,Id(j),IntLiteral(25)),Return(Id(i)))])),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_complex_program22(self):
        input = """void abc() {
			for(i = 1;i < 100;i = i*10)
			{
				foo(c[3], foo(k[foo(x[2]) + 1]));
			}
			return;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(100));BinaryOp(=,Id(i),BinaryOp(*,Id(i),IntLiteral(10)));Block([CallExpr(Id(foo),[ArrayCell(Id(c),IntLiteral(3)),CallExpr(Id(foo),[ArrayCell(Id(k),BinaryOp(+,CallExpr(Id(foo),[ArrayCell(Id(x),IntLiteral(2))]),IntLiteral(1)))])])])),Return()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_complex_program23(self):
        input = """void abc() {
				foo("asdf"[123]);
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([CallExpr(Id(foo),[ArrayCell(StringLiteral(asdf),IntLiteral(123))])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_complex_program24(self):
        input = """void abc() {
				foo("9999" = 1 + 2)[123];
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([ArrayCell(CallExpr(Id(foo),[BinaryOp(=,StringLiteral(9999),BinaryOp(+,IntLiteral(1),IntLiteral(2)))]),IntLiteral(123))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_complex_program25(self):
        input = """void abc() {
				do
                    if(a)
                        return 0;
                while i;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Dowhile([If(Id(a),Return(IntLiteral(0)))],Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_complex_program26(self):
        input = """void abc() {
				do
                    if(a)
                        if(b)
                            return;
                        else
                            c;
                while i;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Dowhile([If(Id(a),If(Id(b),Return(),Id(c)))],Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_complex_program27(self):
        input = """void abc() {
				do
                    {

                    }
                    k + 1;
                while foo(a[3]);
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Dowhile([Block([]),BinaryOp(+,Id(k),IntLiteral(1))],CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(3))]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_complex_program28(self):
        input = """void abc() {
				print("xin chao", 10.2e2)
		}"""
        expect = str(Program([FuncDecl(Id("abc"),[],VoidType(),Block([CallExpr(Id("print"),[StringLiteral("xin chao"),FloatLiteral(10.2e2)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_complex_program29(self):
        input = """
        float i[100], motcailist[129], x;
        int[] main(int i, string k[]) {}
        """
        expect = "Program([VarDecl(i,ArrayType(FloatType,100)),VarDecl(motcailist,ArrayType(FloatType,129)),VarDecl(x,FloatType),FuncDecl(Id(main),[VarDecl(i,IntType),VarDecl(k,ArrayTypePointer(StringType))],ArrayTypePointer(IntType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_complex_program30(self):
        input = """void abc() {
				do
                    if(a)
                        return 0;
                while i;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Dowhile([If(Id(a),Return(IntLiteral(0)))],Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_complex_program31(self):
        input = """void abc() {
				if(j == 15)
						break;
					if(j == 20)
						continue;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([If(BinaryOp(==,Id(j),IntLiteral(15)),Break()),If(BinaryOp(==,Id(j),IntLiteral(20)),Continue())]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_complex_program32(self):
        input = """void abc() {
				helloWorld() = new[i];
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([BinaryOp(=,CallExpr(Id(helloWorld),[]),ArrayCell(Id(new),Id(i)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_complex_program33(self):
        input = """void abc() {
				do
                    return 0;
                while i;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Dowhile([Return(IntLiteral(0))],Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_complex_program34(self):
        input = """void abc() {
				printSomething("sfasdf")
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([CallExpr(Id(printSomething),[StringLiteral(sfasdf)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_complex_program35(self):
        input = """void abc() {}
        int isThisTheRealLife;
        """
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([])),VarDecl(isThisTheRealLife,IntType)])"
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_complex_program36(self):
        input = """void abc() {}
        string[] orJustSomeFantasy(){}
        
        """
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([])),FuncDecl(Id(orJustSomeFantasy),[],ArrayTypePointer(StringType),Block([]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_complex_program37(self):
        input = """void abc() {
				for (i[234]; sadPepe(); func()){

                }
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([For(ArrayCell(Id(i),IntLiteral(234));CallExpr(Id(sadPepe),[]);CallExpr(Id(func),[]);Block([]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_complex_program38(self):
        input = """void abc() {
				for (i[234]; sadPepe(); func()){
                    print(whatIsThis);
                }
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([For(ArrayCell(Id(i),IntLiteral(234));CallExpr(Id(sadPepe),[]);CallExpr(Id(func),[]);Block([CallExpr(Id(print),[Id(whatIsThis)])]))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_complex_program39(self):
        input = """void abc() {
				break; return; continue;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Break(),Return(),Continue()]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_complex_program40(self):
        input = """void abc() {
				return x + 1 + 2 / 3;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Return(BinaryOp(+,BinaryOp(+,Id(x),IntLiteral(1)),BinaryOp(/,IntLiteral(2),IntLiteral(3))))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_complex_program41(self):
        input = """void abc() {
				callsomeFuncHere();
                if (isItTrue)
                    i + 1;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([CallExpr(Id(callsomeFuncHere),[]),If(Id(isItTrue),BinaryOp(+,Id(i),IntLiteral(1)))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_complex_program42(self):
        input = """void abc() {
				do
                    return;
                    break;
                    continue;
                while i;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Dowhile([Return(),Break(),Continue()],Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_complex_program43(self):
        input = """void abc() {
				do
                    if(a)
                        break;
                    continue;
                while i;
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([Dowhile([If(Id(a),Break()),Continue()],Id(i))]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_complex_program44(self):
        input = """void abc() {
				print("thank you for your attention")
                say("avenger assemble")
		}"""
        expect = "Program([FuncDecl(Id(abc),[],VoidType,Block([CallExpr(Id(print),[StringLiteral(thank you for your attention)]),CallExpr(Id(say),[StringLiteral(avenger assemble)])]))])"
        self.assertTrue(TestAST.checkASTGen(input,expect,399))


    