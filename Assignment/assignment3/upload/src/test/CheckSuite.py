import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    # def test_undeclared_function(self):
    #     """Simple program: int main() {} """
    #     input = """int main() {foo();}"""
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,400))

    # def test_diff_numofparam_stmt(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn();
    #     }"""
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,401))
    
    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """int main () {
    #         putIntLn(getInt(4));
    #     }"""
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,402))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: int main() {} """
    #     input = Program([FuncDecl(Id("main"),[],IntType(),Block([
    #         CallExpr(Id("foo"),[])]))])
    #     expect = "Undeclared Function: foo"
    #     self.assertTrue(TestChecker.test(input,expect,403))
    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[
    #                     CallExpr(Id("getInt"),[IntLiteral(4)])
    #                     ])]))])
    #     expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[IntLiteral(4)])"
    #     self.assertTrue(TestChecker.test(input,expect,404))
    # def test_diff_numofparam_stmt_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #             FuncDecl(Id("main"),[],IntType(),Block([
    #                 CallExpr(Id("putIntLn"),[])]))])
    #     expect = "Type Mismatch In Statement: CallExpr(Id(putIntLn),[])"
    #     self.assertTrue(TestChecker.test(input,expect,405))
    
# --------------------------------------------------------------------
    def test_rede_global(self):
        """Redeclared simple case"""
        input = """
                int main () {
                    int a; int a;
                }   
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,400))
    
    def test_rede_global_func(self):
        """Redeclare global function"""
        input = """
                int a(){
                    return 0;
                }
                int a(){
                    return 1;
                }
                int main (){
                    int a; 
                }
                """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input,expect,401))
# -----------------------------------------------------------------
    def test_rede_global_func_para(self):
        """Redeclare Parameter on global function (Test scope)"""
        input = """
                int a; 
                int b(int a){
                    return 8;
                }
                int main() {
                    b(5);
                    return 9;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,402))
# -----------------------------------------------------------------
    def test_global_func_local_decl(self):
        """Test Scope"""
        input = """
                int main() {
                    b();
                    return 0;
                }
                int a; 
                int b(){
                    int a;
                    return 9;
                }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_rede_global_func_local_decl_para(self):
        """Redeclare local variable"""
        input = """
                int a; 
                int foo(int a){
                    int a;
                    return 9;
                }
                int main(){
                    return 0;
                }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_rede_global_func_2_para(self):
        """Redeclare Parameter in function"""
        input = """
                int a; 
                int foo(int a,int a){
                    return 0;
                }
                void main() {

                }
                """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_rede_global_func_local_decl_para_2(self):
        """Redeclare Variable in local scope and the parameter"""
        input = """
                int a; 
                int foo(int a){
                    int c;
                    int a;
                    return 2;
                }
                int main() {
                    foo(5);
                }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_rede_global_func_local_decl_para_3(self):
        """Redeclare Variable in local scope"""
        input = """
                int a; 
                int foo(int b, int c){ 
                    b = 1; 
                    int a; 
                    int a;
                    return 8;
                }
                void main(){
                    foo(888888,999999);
                }
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_rede_global_func_no_para(self):
        """Redeclare function"""
        input = """
                    int a; 
                    int foo(int a){ 
                        int b;
                        b = 1; 
                        {
                            int a;
                            return 8888888;
                        }
                    } 
                    int foo(){
                        return 999999;
                    }
                    void main(){
                        foo(8);
                    }
                """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,408))

# ------------------------------------------------------------------------
    def test_unde_simple(self):
        input = """
                    void main() {
                        int a; 
                        a = b;
                    }
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_unde(self):
        """Undeclare Identifier in the function"""
        input = """
                    int a; 
                    int foo(int a){
                        b;
                        return 99999;
                    }
                    void main (){
                        foo(888888);
                    }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_unde_exp(self):
        """Undeclare Identifier in the function (expression)"""
        input = """
                int x; 
                int thisIssOlOnG(int a){ 
                    y = 888888;
                    return 999999;
                }
                void main(){
                    thisIssOlOnG(888888);
                }
                """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input,expect,411))
 
    def test_unde_complex(self):
        """Undeclare Identifier in the function"""
        input = """
                    int a; 
                    float foo(int a){ 
                        int c; 
                        x; 
                        {
                            int a;
                            return 9999.9999;
                        }
                    }
                    float main(){
                        foo(8888.8888);
                    }
                """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_unde_within_block(self):
        """Undeclare Identifier in the function (nested block)"""
        input = """
                int a; 
                int foo(int m){
                    int c; 
                    int n; 
                    {
                        int a; 
                        int b; 
                        d;
                        return 8888;
                    }
                }
                void main(){
                    foo(8888888);
                }
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input,expect,413))
# ---------------------------------------------------------------
    def test_unde_para(self):
        input = """
                int a; 
                int foo(int b){
                    return c + 8888;
                }
                int main(){
                    foo(999);
                }
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input,expect,414))

# ----------------------------------------------------------------------------
    def test_if_mismatch_true(self):
        """Test if else stmt"""
        input = """
                int foo(){
                    boolean tof;
                    if (tof){}
                    else {}
                    return 9;
                }
                int main(){
                    foo();
                    return 0;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_if_mismatch(self):
        """Mismatch on Expression"""
        input = """
                    int foo(){
                        if (2 + 1){}
                        else {}
                        return 8;
                    }
                    int main(){
                        foo();
                        return 0;
                    }
                    """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,IntLiteral(2),IntLiteral(1)),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_if_mismatch_int_string(self):
        """Mismatch on Expression: int vs. string"""
        input = """
                int foo(){
                    int a;
                    a = 0;
                    if (a >= "asd"){}
                    else {}
                    return a;
                }
                int main(){
                    foo();
                    return 0;
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(a),StringLiteral(asd))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_if_mismatch_int_float(self):
        """Mismatch on Expression: int vs. float"""
        input = """
                int foo(){
                    int a;
                    a = 0;
                    if (a == 888.888){}
                    else {}
                    return 9999;
                }
                void main(){
                    foo();
                }
                """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(a),FloatLiteral(888.888))"
        self.assertTrue(TestChecker.test(input,expect,418))

# ------------------------------------------------------------------------
    def test_for_mismatch_exp2(self):
        """Mismatch on Expression: boolean vs. int"""
        input = """
                int foo(){
                    int a;
                    int b;
                    int c;
                    for (a; b; c){

                    }
                    return 8888;
                }
                void main(){
                    foo();
                }
                """
        expect = "Type Mismatch In Statement: For(Id(a);Id(b);Id(c);Block([]))"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_for_mismatch_true(self):
        """No mismatch: for stmt"""
        input = """
                int foo(){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        return 8;
                    }
                    return 789;
                }
                int main(){
                    foo();
                    return 0;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_for_mismatch_int_exp3(self):
        """Mismatch on Express 3: int vs. float"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    float c;
                    for (a + 1; b; c){
                        return 999;
                    }
                    return 888;
                }
                void main(){
                    foo(8,9);
                }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(+,Id(a),IntLiteral(1));Id(b);Id(c);Block([Return(IntLiteral(999))]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_for_mismatch_exp3_binaryop(self):
        """Mismatch on Express 3: int vs. float (c: int plus 9.99 => float)"""
        input = """
                void main(){
                    foo(31, 12, 2019);
                }
                int foo(int x, int y, int z){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c + 9.99){
                        return 888;
                    }
                    return a;
                }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(+,Id(a),IntLiteral(1));Id(b);BinaryOp(+,Id(c),FloatLiteral(9.99));Block([Return(IntLiteral(888))]))"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_for_mismatch_int_exp1(self):
        """Mismatch on Expression 1: int vs. float"""
        input = """
                void main(){
                    foo();
                }
                int foo(){
                    float a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        c = c + 99;
                        return c * 88;
                    }
                    return c;
                }
                """
        expect = "Type Mismatch In Statement: For(BinaryOp(+,Id(a),IntLiteral(1));Id(b);Id(c);Block([BinaryOp(=,Id(c),BinaryOp(+,Id(c),IntLiteral(99))),Return(BinaryOp(*,Id(c),IntLiteral(88)))]))"
        self.assertTrue(TestChecker.test(input,expect,423))

# -----------------------------------------------------------------------
    def test_exp_mismatch_bool_una_sub(self):
        """Mismatch on Unary Expression: boolean"""
        input = """
                boolean foo(){
                    boolean a;
                    -a;
                    return a;
                }
                void main(){
                    foo();
                }
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_exp_mismatch_string_una_sub(self):
        """Mismatch on Unary Expression: string"""
        input = """
                void main(){
                    foo();
                }
                int foo(){
                    string a;
                    -a;
                    return 0;
                }"""
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(a))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_exp_unary_int(self):
        """No Mismatch on Unary Expression: int"""
        input = """
                int foo(){
                    int a;
                    -a;
                    return a;
                }
                int main(){
                    foo();
                    return 0;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_exp_unary_float(self):
        """No Mismatch on Unary Expression: float"""
        input = """
                void main(){
                    foo();
                }
                float foo(){
                    float a;
                    -a;
                    return a;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,427))

# ---------------------------------------------------------------------
    def test_visitNestedDowhile(self):
        """Test do while in function"""
        input = """
                float thIsIssOlOnG(){
                    int x;
                    int y;
                    do {
                        x = x * y;
                        return y;
                    }
                    while(true);
                    return x;
                }
                float main(){
                    thIsIssOlOnG();
                    return 0;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_Dowhile_in_Main(self):
            """Test do while in main"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            x = x * y;
                            return y;
                        }
                        while(true);
                        return x;
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 429))

    def test_Mismatch_string_Dowhile_in_Main(self):
            """Mismatch do while in main: int vs. string"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            x = x * y;
                            return y;
                        }
                        while(x != "as");
                        return x;
                    }
                    """
            expect = "Type Mismatch In Expression: BinaryOp(!=,Id(x),StringLiteral(as))"
            self.assertTrue(TestChecker.test(input, expect, 430))

    def test_Mismatch_float_Dowhile_in_Main(self):
            """Mismatch do while in main: int vs. float"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            x = x * y;
                            return y;
                        }
                        while(x != 9.99);
                        return x;
                    }
                    """
            expect = "Type Mismatch In Expression: BinaryOp(!=,Id(x),FloatLiteral(9.99))"
            self.assertTrue(TestChecker.test(input, expect, 431))

    def test_No_Mismatch_Dowhile_in_Main(self):
            """No Mismatch do while in main: int vs. int"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            x = x * y;
                            return y;
                        }
                        while(x != 9999);
                        return x;
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 432))

    def test_Mismatch_Dowhile_in_Main_int(self):
            """Mismatch Do While on Expression: boolean vs. int"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            x = x * y;
                            return y;
                        }
                        while(x);
                        return x;
                    }
                    """
            expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(x),BinaryOp(*,Id(x),Id(y))),Return(Id(y))])],Id(x))"
            self.assertTrue(TestChecker.test(input, expect, 433))

    def test_Mismatch_Dowhile_in_Main_string(self):
            """Mismatch Do While on Expression: boolean vs. int"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            x = x * y;
                            return y;
                        }
                        while("99999");
                        return x;
                    }
                    """
            expect = "Type Mismatch In Statement: Dowhile([Block([BinaryOp(=,Id(x),BinaryOp(*,Id(x),Id(y))),Return(Id(y))])],StringLiteral(99999))"
            self.assertTrue(TestChecker.test(input, expect, 434))

    # ------------------------------------------------------------
    

# -------------------------------------------------------------------
    def test_break_not_in_do_while(self):
            """Break not in do while"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            return y;
                        }
                        while(true);
                        break;
                        return x;
                    }
                    """
            expect = "Break Not In Loop"
            self.assertTrue(TestChecker.test(input, expect, 435))

    def test_break_in_if(self):
        """Break in if stmt"""
        input = """
                int foo(){
                    int a;
                    a = 0;
                    if (a == 888){
                        break;
                    }
                    else {}
                    return 9999;
                }
                void main(){
                    foo();
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_break_in_else(self):
        """Break in else stmt"""
        input = """
                int foo(){
                    int a;
                    a = 0;
                    if (a == 888){
                        return 999;
                    }
                    else {
                        break;
                    }
                    return 9999;
                }
                void main(){
                    foo();
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_break_not_in_for(self):
        """Break not in for stmt"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        return 999;
                    }
                    break;
                    return 888;
                }
                void main(){
                    foo(8,9);
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,438))
# --------------------------------------------------------------------
# Nested:
    def test_break_in_for_if_else(self):
        """Break in for stmt"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        if (a == c){
                            break;
                        }
                        return 999;
                    }
                    return 888;
                }
                void main(){
                    foo(8,9);
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_break_in_do_while_if_else(self):
            """Break in do while"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            if (x == y)
                                break;
                            return y;
                        }
                        while(true);
                        return x;
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 440))


# -------------------------------------------------------------------
    def test_continue_not_in_do_while(self):
                """Continue not in do while"""
                input = """
                        float main(){
                            int x;
                            int y;
                            do {
                                return y;
                            }
                            while(true);
                            continue;
                            return x;
                        }
                        """
                expect = "Continue Not In Loop"
                self.assertTrue(TestChecker.test(input, expect, 441))

    def test_continue_in_if(self):
        """Continue in if stmt"""
        input = """
                int foo(){
                    int a;
                    a = 0;
                    if (a == 888){
                        continue;
                    }
                    else {}
                    return 9999;
                }
                void main(){
                    foo();
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_continue_in_else(self):
        """Continue in else stmt"""
        input = """
                int foo(){
                    int a;
                    a = 0;
                    if (a == 888){
                        return 999;
                    }
                    else {
                        continue;
                    }
                    return 9999;
                }
                void main(){
                    foo();
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_continue_not_in_for(self):
        """Continue not in for stmt"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        return 999;
                    }
                    continue;
                    return 888;
                }
                void main(){
                    foo(8,9);
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,444))
# --------------------------------------------------------------------
# Nested:
    def test_continue_in_for_if_else(self):
        """Continue in for stmt"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        if (a == c){
                            continue;
                        }
                        return 999;
                    }
                    return 888;
                }
                void main(){
                    foo(8,9);
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_continue_in_do_while_if(self):
            """Continue in do while"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            if (x == y)
                                continue;
                            return y;
                        }
                        while(true);
                        return x;
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 446))
# -------------------------------------------------------------------
    def test_break_continue_in_for_else(self):
            """Break, Continue in for stmt"""
            input = """
                    int foo(int x, int y){
                        int a;
                        boolean b;
                        int c;
                        for (a + 1; b; c){
                            if (a == c){
                                continue;
                            }
                            else
                                break;
                            return 999;
                        }
                        return 888;
                    }
                    void main(){
                        foo(8,9);
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_continue_in_do_while_if_else(self):
            """Break, Continue in do while"""
            input = """
                    float main(){
                        int x;
                        int y;
                        do {
                            if (x == y)
                                break;
                            else
                                continue;
                            return y;
                        }
                        while(true);
                        return x;
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 448))
# -------------------------------------------------------------------
    def test_no_entry(self):
            """Test no main function"""
            input = """
                    int a(int z){
                        return 0;
                    }
                    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 449))

    def test_no_entry_2(self):
            """Test no main function"""
            input = """
                    int foo(int x, int y){
                        int a;
                        boolean b;
                        int c;
                        for (a + 1; b; c){
                            return 999;
                        }
                        return 888;
                    }
                    int a(int z){
                        return 0;
                    }
                    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_no_entry_3(self):
            """Test no main function"""
            input = """
                    int foo(int x, int y){
                        int a;
                        boolean b;
                        int c;
                        for (a + 1; b; c){
                            return 999;
                        }
                        return 888;
                    }
                    int a(int z){
                        foo(8,9);
                        return 0;
                    }
                    """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 451))
# -------------------------------------------------------------------
# Test Unreachable Function:
    def test_unreached_func(self):
        """No Raise Error About Unreachable Function"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        return 999;
                    }
                    return 888;
                }
                int a(int z){
                    int m;
                    m = foo(8,9);
                    return m;
                }
                int main(){
                    a(3);
                    return 1;
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_unreached_func_not_using(self):
        """Unreachable Function"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        return 999;
                    }
                    return 888;
                }
                void tired(){
                    putIntLn(9);
                }
                int a(int z){
                    tired();
                    return 888888;
                }
                int main(){
                    a(3);
                    return 0;
                }
                """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_nested_unreached_func_not_using(self):
        """Nested Unreachable Function"""
        input = """
                int foo(int x, int y){
                    int a;
                    boolean b;
                    int c;
                    for (a + 1; b; c){
                        return 999;
                    }
                    return 888;
                }
                void tired(){
                    putIntLn(9);
                }
                int a(int z){
                    tired();
                    return 888888;
                }
                int main(){
                    a(3);
                    return 0;
                }
                """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_unreachable_function_simple(self):
            """Not Raise Unreachable Function: simple"""
            input = """
                    int a(int z){
                        return 0;
                    }
                    void main(){
                        a(9);
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 455))

    def test_unreachable_function_arrayCell(self):
        """Not Raise Unreachable Function: arraycell"""
        input = """
            void main(){ 
                int x, array[99];
                x = 999;
                arr()[tired(x - -8888)] = x;
            }
            int[] arr(){
                int theArray[88];
                return theArray;
            }
            int tired(int a){
                tired(a);
                return 10;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_unreachable_function_for(self):
        """Raise Unreachable Function: foo"""
        input = """
            void print(){
                int i;
                i = 0;
                for (i; i < 9; i = i + 1){
                    putIntLn(i);
                }
            }
            int foo(){
                return 9;
            }
            int main(){
                print();
                return 0;
            }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_unreachable_function_for_2(self):
        """Not Raise Unreachable Function: foo"""
        input = """
            void print(){
                int i;
                i = 0;
                for (i; i < foo(); i = i + 1){
                    putIntLn(i);
                }
            }
            int foo(){
                return 9;
            }
            int main(){
                print();
                return 0;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_unreachable_function_do_while(self):
        """Not Raise Unreachable Function: foo"""
        input = """
            void print(){
                int i;
                i = 0;
                do {
                    putIntLn(i);
                }
                while (i < foo());
            }
            int foo(){
                return 9;
            }
            int main(){
                print();
                return 0;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_unreachable_function_nested_do_while(self):
        """Not Raise Unreachable Function: foo"""
        input = """
            void print(){
                int i;
                i = 0;
                do {
                    do {
                        putFloatLn(i);
                    }
                    while (i != foo());
                }
                while (i < 100);
            }
            int foo(){
                return 9;
            }
            int main(){
                print();
                return 0;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_unreachable_function_nested_do_while_2(self):
        """Raise Unreachable Function: foo"""
        input = """
            void print(){
                int i;
                i = 0;
                do {
                    do {
                        putFloatLn(i);
                    }
                    while (i != 999);
                }
                while (i < 100);
            }
            int foo(){
                return 9;
            }
            int main(){
                print();
                return 0;
            }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_unreachable_function_if_else(self):
        """Not Raise Unreachable Function: foo"""
        input = """
            void print(){
                int i;
                i = 0;
                if (i < foo()){
                    putFloatLn(i);
                }
                else{
                    getInt();
                }
            }
            int foo(){
                return 9;
            }
            int main(){
                print();
                return 0;
            }
            """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_unreachable_function_if_else_2(self):
        """Raise Unreachable Function: foo"""
        input = """
            void print(){
                int i;
                i = 0;
                if (i < 999){
                    putFloatLn(i);
                }
                else{
                    getInt();
                }
            }
            int foo(){
                return 9;
            }
            int main(){
                print();
                return 0;
            }
            """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_unreachable_function_complex(self):
        """Test Unreachable Function: complex"""
        input = """
            int x(int a){
                x(5);
                return 5;
            }

            float y(int a){
                x(a);
                return 5.5;
            }
            void z(int a){
                z(a);
            }
            boolean w(int a){
                return true;
            }
            string t(int a){
                return "5";
            }

            void main (float a, float b) {
                if(a <= b){
                    y(888);
                }
                else
                    y(888);
                do {
                    if (a >= b)
                        t(5);

                }
                while(a > b);

                int c;
                c = 999;
                int i;

                for(i = 888; a < c; c = c + 1){
                    w(5);
                    t(5);
                }
                x(5);
            }
            """
        expect = "Unreachable Function: z"
        self.assertTrue(TestChecker.test(input, expect, 464))

# -------------------------------------------------------------------
# Test NotLeftVale
    def test_notleftvalue_leftisIntLiteral(self):
        """Test No Left Value: LHS: func"""
        input = """
                int a(int z){
                    return z;
                }
                void main() {
                    a(1) = 1;
                }
                """
        expect = "Not Left Value: CallExpr(Id(a),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_notleftvalue_biOp(self):
        """Test No Left Value: LHS: can't assign"""
        input = """
                void main(){ 
                    int x, arr[8];
                    x * 888 = 999 + arr[0];            
                }
                """
        expect = "Not Left Value: BinaryOp(*,Id(x),IntLiteral(888))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_notleftvalue_biOp_2(self):
        """Test No Left Value: LHS: can't assign"""
        input = """
                void main(){ 
                    int x, arr[8];
                    x * 888 = arr[0];            
                }
                """
        expect = "Not Left Value: BinaryOp(*,Id(x),IntLiteral(888))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_notleftvalue_biOp_literals_int(self):
        """Test No Left Value: LHS: intLiteral"""
        input = """
                void main(){ 
                    int arr[8];
                    888 = arr[0];            
                }
                """
        expect = "Not Left Value: IntLiteral(888)"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_notleftvalue_biOp_literals_string(self):
        """Test No Left Value: LHS: stringLiteral"""
        input = """
                void main(){ 
                    int arr[8];
                    "888.888" = arr[0];            
                }
                """
        expect = "Not Left Value: StringLiteral(888.888)"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_notleftvalue_biOp_literals_float(self):
        """Test No Left Value: LHS: stringLiteral"""
        input = """
                void main(){ 
                    int arr[8];
                    888.888 = arr[0];            
                }
                """
        expect = "Not Left Value: FloatLiteral(888.888)"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_notleftvalue_biOp_literals_boolean(self):
        """Test No Left Value: LHS: stringLiteral"""
        input = """
                void main(){ 
                    int arr[8];
                    true = arr[0];            
                }
                """
        expect = "Not Left Value: BooleanLiteral(true)"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_notleftvalue_unaryOp(self):
        """Test No Left Value: LHS: unary"""
        input = """
                void main(){ 
                    int x; 
                    int arr[99];
                    -x = arr[8] * 20 - (8888 * arr[9]) / 9;             
                }
                """
        expect = "Not Left Value: UnaryOp(-,Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_notleftvalue_funcall(self):
        """Test No Left Value: LHS: funcall"""
        input = """
                void main(){ 
                    int x; 
                    int arr[99];
                    alterEgo() = -(x + arr[88] / 9999 * 888);             
                }
                int alterEgo(){
                    return 888888;
                }
                """
        expect = "Not Left Value: CallExpr(Id(alterEgo),[])"
        self.assertTrue(TestChecker.test(input, expect, 473))

    
# -------------------------------------------------------------------
# Test Function Not Return:
    def test_func_not_return_in_body(self):
        """Not Return in the Function"""
        input = """
                int sum() {
                    int a, b, c, x, y, z;
                }
                void main(){
                    sum();
                }
                """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_func_not_return_in_nested_block(self):
        """Return in nested block"""
        input = """
                int sum(){
                    {
                        return 1;
                    }
                }
                void main(){
                    sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_func_not_return_in_if_else(self):
        """Not Return in if else"""
        input = """
                int sum(){
                    if (!true){

                    }
                    else{
                        
                    }
                    return 1;
                }
                void main(){
                    sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_func_not_return_in__nested_if_else(self):
        """Not Return in if else"""
        input = """
                int sum(){
                    if (!true){
                        if (true){

                        }
                        else{

                        }
                        return 888;
                    }
                    else{
                        
                    }
                    return 1;
                }
                void main(){
                    sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_func_not_return_in__nested_if_else_no_return_outside(self):
        """Not Return outside block if else"""
        input = """
                int sum(){
                    if (!true){
                        if (true){

                        }
                        else{

                        }
                    }
                    else{
                        if (3 < 5){

                        }
                        else{

                        }
                    }
                    return 1;
                }
                void main(){
                    sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_func_not_return_in_do_while(self):
        """Not Return in do while"""
        input = """
                int sum(){
                    string x;
                    do {
                        x = "This Is So Tired!";
                    }
                    while (true);
                }
                void main(){
                    sum();
                }
                """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test_func_not_return_in_nested_do_while(self):
        """Not Return in nested do while"""
        input = """
                int sum(){
                    int x;
                    do {
                        do {
                            x = x * 999;

                        }
                        while(x < 888);
                    }
                    while (true);
                }
                void main(){
                    sum();
                }
                """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_func_not_return_in_nested_do_while_2(self):
        """Not Return in nested do while"""
        input = """
                int sum(){
                    int x;
                    do {
                        do {
                            x = x * 999;
                        }
                        while(x < 888);
                        return 1;
                    }
                    while (true);
                }
                void main(){
                    sum();
                }
                """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 481))
# -------------------------------------------------------------------
# Test Actual Parameters vs. Formal Parameters
    def test_actual_vs_formal(self):
        """Test actual > formal parameters"""
        input = """
                int sum(){
                    int x;
                    return x;
                }
                void main(){
                    sum(8,9);
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[IntLiteral(8),IntLiteral(9)])"
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test_actual_vs_formal_2(self):
        """Test actual < formal parameters 2"""
        input = """
                int sum(int x, int y){
                    return x + y;
                }
                void main(){
                    sum();
                }
                """
        expect = "Type Mismatch In Expression: CallExpr(Id(sum),[])"
        self.assertTrue(TestChecker.test(input, expect, 483))

# -------------------------------------------------------------------
# Test Type Mismatch:
    def test_func_return_int(self):
        """Test on return type is matching or not: featuring arraycell"""
        input = """
                int[] foo(){
                    int a[3];
                    a[1] = 1;
                    return a[1];
                }
                int main(){
                    foo();
                }
                """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_func_return_float(self):
        """Test on return type is matching or not: float vs. float"""
        input = """
                float sum(){
                    return 8.8888888888888;
                }
                void main(){
                    sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_func_return_int_2(self):
        """Test on return type is matching or not: int vs. float"""
        input = """
                int sum(){
                    return 8.8888888;
                }
                void main(){
                    sum();
                }
                """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(8.8888888))"
        self.assertTrue(TestChecker.test(input, expect, 486))

# # -------------------------------------------------------------------
# Test Undeclare Function
    def test_unreachable_function_for_3(self):
        """Undeclare Function in for stmt"""
        input = """
            void printArray(){
                int theArray[88];
                int i;
                i = 0;
                int value;
                for (i; i < 9; i = i + 1){
                    value = theArray()[i];
                }
            }
            int main(){
                printArray();
                return 0;
            }
            """
        expect = "Undeclared Function: theArray"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_undecl_function_do_while_3(self):
        """Undeclare Function in for stmt"""
        input = """
            void printArray(){
                int theArray[88];
                int i;
                i = 0;
                int value;
                do {
                    value = theArray()[i];
                }
                while (true);
            }
            int main(){
                printArray();
                return 0;
            }
            """
        expect = "Undeclared Function: theArray"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_undeclared_function_used_as_parameter(self):
        """More complex program"""
        input = """
                void so(int x, float y){
                    return;
                }
                float z;
                void main(){
                    so(getInt(), z);
                    so(tired(), z);     
                }
                """
        expect = "Undeclared Function: tired"
        self.assertTrue(TestChecker.test(input, expect, 489))

# -------------------------------------------------------------------
# Test ArrayCell: type of eleType
    def test_eleType_float(self):
        """Test Float eleType"""
        input = """
                float y; 
                int x[88]; 
                void main() {
                    x[y / y];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),BinaryOp(/,Id(y),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_array_wrong_index_boolean(self):
        """Test Boolean eleType"""
        input = """
                boolean y; 
                int x[88]; 
                void main() {
                    x[y || y];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),BinaryOp(||,Id(y),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,491))
    
    def test_array_wrong_index_string(self):
        """test String eleType"""
        input = """
                string y; 
                int x[88]; 
                void main() {
                    x[y];
                }
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),Id(y))"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_return(self):
        """Test Return Mismatch"""
        input = """
                int main() {
                    return 888888.888;
                }
                """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(888888.888))"
        self.assertTrue(TestChecker.test(input,expect,493))

# -------------------------------------------------------------------
# More Complex Tests:
    def test_2_Nested_Dowhile_in_function(self):
            """Test 2 nested do while in function"""
            input = """
                    float nested(){
                        int x;
                        int y;
                        do {
                            do {
                                do {
                                    x = x * y;
                                    return y;
                                }
                                while (y == x);
                                return 888888;
                            }
                            while(x != y);
                        }
                        while(true);
                        return x;
                    }
                    void main(){
                        nested();
                    }
                    """
            expect = ""
            self.assertTrue(TestChecker.test(input, expect, 494))

# --------------------------------------------------------------------
# Extra:
    def test_unreach(self):
        """Test unreachable function"""
        input = """
                int minus(){
                    return 1;
                }
                int sum(){
                    return 2;
                }
                int div(){
                    return 3;
                }
                int mul(){
                    return minus();
                }
                void main(){
                    sum();
                    mul();
                }
                """
        expect = "Unreachable Function: div"
        self.assertTrue(TestChecker.test(input, expect, 495)) 
# --------------------------------------------------------------------
    def test_func_not_return_in_if_else(self):
        """Test Function Return in both If and Else"""
        input = """
                int sum(){
                    if (!true){
                        int a;
                        return 1;
                    }
                    else {
                        int b;
                        return 2;
                    }
                }
                void main(){
                    sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_func_not_return_in_if_else_3(self):
        """Test Function Return in only Else"""
        input = """
                int sum(){
                    if (!true){

                    }
                    else{
                        return 8;
                    }
                    return 9;
                }
                int main(){
                    return sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_func_not_return_in_if_else_4(self):
        """Test Function Return in onyly If"""
        input = """
                int sum(){
                    if (true){
                        return 888888;
                    }
                    else{

                    }
                    return 99999;
                }
                int main(){
                    return sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_func_not_return_in_for(self):
        input = """
                int sum(){
                    int i;
                    int sum;
                    for (i = 0; i < 9; i = i + 1){
                        sum = sum + i;
                    }
                }
                int main(){
                    return sum();
                }
                """
        expect = "Function sum Not Return "
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_func_not_return_in_for_outside(self):
        input = """
                int sum(){
                    int i;
                    int sum;
                    for (i = 0; i < 9; i = i + 1){
                        sum = sum + i;
                    }
                    return 888888;
                }
                int main(){
                    return sum();
                }
                """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))
# --------------------------------------------------------------------