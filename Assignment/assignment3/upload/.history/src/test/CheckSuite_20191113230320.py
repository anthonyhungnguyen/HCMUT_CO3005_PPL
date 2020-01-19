import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_NoEnTryPoint(self):
        input = """
        int foo(){return 1;}
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_Redeclare_Var_Var_Global(self):
        input = """
        int a;
        int a;
        void main(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_Redeclare_Var_Var_Not_adjacent_Global(self):
        input = """
        int a;
        void main(){}
        int a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_Redeclare_Var_Var_DifferentType_Global(self):
        input = """
        int a;
        void main(){}
        string a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test__Var_Global_Var_local(self):
        input = """
        int a;
        void main(){
            string a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test__Redeclare_Var__Var_local(self):
        input = """
        int a;
        void main(){
            string a;
            boolean a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test__Var_Global_Var_local_param(self):
        input = """
        int a;
        void foo(int a){
        }
        void main(){foo(1);}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test__Redeclare_Var_param__Var_local(self):
        input = """
        int a;
        void foo(int a){
            float a;
        }
        void main(){foo(1);}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test__Redeclare_Var_local_new_block_scope(self):
        input = """
        int a;
        void foo(int a){
            {
                float a;
            }
        }
        void main(){foo(1);}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test__Redeclare_Var_local_new_block_scope_2_level(self):
        input = """
        int a;
        void foo(int a){
            {
                float a;
                {
                    string a;
                }
            }
        }
        void main(){foo(1);}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test__Var_Var_param(self):
        input = """
        int a;
        void foo(int b,int b){
        }
        void main(){foo(1);}
        """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_Redeclare_Func_Func_(self):
        input = """
        void main(){}
        void main(){}
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_Redeclare_Func_Func_Different(self):
        input = """
        void b(){}
        int b(){return 1;}
        void main(){}
        """
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_Redeclare_Func_Separate_Func_Different(self):
        input = """
        void b(){}
        void main(){}
        int b(){return 1;}
        """
        expect = "Redeclared Function: b"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_Id_declared_in_global(self):
        input = """
        int a;
        void main(){
            a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_Id_undeclared(self):
        input = """
        void main(){
            a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_Id_in_level_1_declared_in_global(self):
        input = """
        int a;
        void main(){
            {
                a;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_Id_in_level_2_declared_in_global(self):
        input = """
        int a;
        void main(){
            {
                {
                    a;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_Id__declared_in_global_after_that_func(self):
        input = """
        void main(){
            {
                {
                    a;
                }
            }
        }
        int a;
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_Id__declared_in_param(self):
        input = """
        int foo(int a){
            a;
            return a;
        }
        void main(){
            foo(1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_Id__declared_in_local(self):
        input = """
        int foo(){
            int a;
            a;
            return a;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_Id__undeclared_in_other_func(self):
        input = """
        int foo(){
            int a;
            a;
            return a;
        }
        void main(){
            a;
            foo();
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_Id_used_befor_declared(self):
        input = """
        void main(){
            a;
            int a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_Id_in_level_2_declared_in_local(self):
        input = """
        void main(){
            int a;
            {
                {
                    a;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_Id_declared_in_level_1_use_in_outer(self):
        input = """
        void main(){
            int a;
            {
                a;
                int b;
            }
            b;
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_Id_in_level_2_declared_in_lvl_1(self):
        input = """
        void main(){
            int a;
            {
                {
                    a;
                    int b;
                }
                b;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_Var_declared_in_level_2_Var_declared_in_lvl_1(self):
        input = """
        void main(){
            int a;
            {
                {
                    a;
                    int b;
                }
                int b;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test__Redeclare_Var__scope_1_level(self):
        input = """

        void foo(int a){
            {
                float b;
                {
                    string a;
                }
                boolean b;
            }
        }
        void main(){foo(1);}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test__Func__undeclared(self):
        input = """
        void main(){foo(1);}
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test__Id_same_func__undeclared(self):
        input = """
        void main(){main;}
        """
        expect = "Undeclared Identifier: main"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test__Func__scope_deep_level(self):
        input = """

        void foo(int a){
        }
        void main(){
            {
                {
                    foo(1);
                }
            }
        }

        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test__If(self):
        input = """
        void main(){
            if(true){}
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test__If_else(self):
        input = """
        void main(){
            if(true){}
            else{}
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test__If_exp_declared(self):
        input = """
        void main(){
            boolean a;
            if(a){}
            else{}
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test__If_exp_not_boolean(self):
        input = """
        void main(){
            int a;
            if(a){}
            else{}
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test__For(self):
        input = """
        void main(){
            int a;
            for(a = 1 ; a < 10 ; a = a + 1){}
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test__For_exp1_exp3_not_Int(self):
        input = """
        void main(){
            float a;
            for(a = 1 ; a < 10 ; a = a + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(<,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test__For_exp2_not_boolean(self):
        input = """
        void main(){
            int a;
            for(a = 1 ; a - 10 ; a = a + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(a),IntLiteral(1));BinaryOp(-,Id(a),IntLiteral(10));BinaryOp(=,Id(a),BinaryOp(+,Id(a),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test__do_While(self):
        input = """
        void main(){
            int a;
            do{}while(a != 1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test__do_While_exp_not_boolean(self):
        input = """
        void main(){
            int a;
            do{}while(a);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test__return_in_int_func(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test__return_nothing_in_not_void_func(self):
        input = """
        int foo(){
            return;
        }
        void main(){
            foo();
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test__return_float_in_int_func(self):
        input = """
        int foo(){
            return 1.1;
        }
        void main(){
            foo();
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test__return__float_func(self):
        input = """
        float foo(){
            return 1.1;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test__return_int_in_float_func(self):
        input = """
        float foo(){
            return 1;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test__return_ArPointer_func(self):
        input = """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            int a[1];
            foo(a);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test__return__arrayType_ArPointer_func(self):
        input = """
        int[] foo(int a[]){
            int b[1];
            return b;
        }
        void main(){
            int a[1];
            foo(a);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test__return_ArPointer_Float_func(self):
        input = """
        float[] foo(int a[]){
            return a;
        }
        void main(){
            int a[1];
            foo(a);
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test__return__float_arrayType_ArPointer__func(self):
        input = """
        int[] foo(int a[]){
            float b[1];
            return b;
        }
        void main(){
            int a[1];
            foo(a);
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test__return__string_arrayType_ArPointer__func(self):
        input = """
        string[] foo(string a[]){
            float b[1];
            return a;
        }
        void main(){
            string a[1];
            foo(a);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test__return__string_arrayType_ArPointer__func(self):
        input = """
        boolean[] foo(string a[]){
            boolean b[1];
            return b;
        }
        void main(){
            boolean a[1];
            foo(a);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_no_return_void__func(self):
        input = """
        void foo(){

        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test__return_void__func(self):
        input = """
        void foo(){
            return;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test__return_something_in_void__func(self):
        input = """
        void foo(){
            return 1;
        }
        void main(){
            foo();
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test__assign_exp_int(self):
        input = """
        int a;
        void main(){
            a = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test__assign_exp_int_with_not_int(self):
        input = """
        int a;
        void main(){
            a = 1.1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test__assign_exp_float_with_float(self):
        input = """
        void main(){
            float a;
            a = 1.1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test__assign_exp_float_with_int(self):
        input = """
        void main(){
            float a;
            a = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test__assign_exp_lhs_is_arraytype(self):
        input = """
        void main(){
            int a[10];
            a = 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test__assign_exp_lhs_is_arraypointertype(self):
        input = """
        void foo(boolean a[]){
            a = true ;
        }
        void main(){
            boolean a[5];
            foo(a);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test__assign_exp_with_String(self):
        input = """
        void main(){
            string a;
            a = "PPL\\n";
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test__NOT_assign_exp_with_String(self):
        input = """
        void main(){
            string a;
            a = "PPL\\n" + "Ass3";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(PPL\\n),StringLiteral(Ass3))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test__index_expression_arraytype(self):
        input = """
        void main(){
            string a[10];
            a[1] = "a";
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test__index_expression_arraypointertype(self):
        input = """
        void foo(boolean a[]){
            a[1] = true;
        }
        void main(){
            boolean a[10];
            foo(a);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test__index_expression_anothertype(self):
        input = """
        void main(){
            float a;
            a[1] = 1.1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test__index_expression_wrong_idx_type(self):
        input = """
        void main(){
            float a[10];
            a[1.1] = 1.1;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test__add_int_expression_(self):
        input = """
        void main(){
            int a; 
            a = 1 + 1 + 1;
            a = 1 + a + 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test__add_int_float_expression_(self):
        input = """
        void main(){
            int a; 
            a = 1 + 1.1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),BinaryOp(+,IntLiteral(1),FloatLiteral(1.1)))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test__add_float_in_expression_(self):
        input = """
        void main(){
            float a[10];
            a[1] = 1.1 + 1;

        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test__add_wrong_type_in_expression_(self):
        input = """
        void main(){
            float a[10];
            a[1] = 1.1 + true;

        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,FloatLiteral(1.1),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test__all_true_op_with_numbers_in_expression_(self):
        input = """
        void main(){
            int a;
            float b;
            int test;
            float test1;
            //INT
            test = a + 1 * a - 10 / 8;
            test = a + a + a + 89 + a + 12 + a;
            test = a - a - a - 89 - a - 12 - a;
            test = a * a * a * 89 * a * 12 * a;
            test = a / a / a / 89 / a / 12 / a;
            //FLOAT
            test1 = a + 1.1 * a - 10e1 / 8.1e8;
            test1 = a + a + a + 89 + a + 12e8 + a;
            test1 = a - a - a - 89 - a - 0.1 - a;
            test1 = a * a * a * 89 * a * 1.2 * a;
            test1 = a / a / a / 89.01 / a / 1.22 / a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test__mod_int_type_in_expression_(self):
        input = """
        void main(){
            int a;
            a = 10 % 1 % a % 9;

        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test__mod_float_type_in_expression_(self):
        input = """
        void main(){
            int a;
            a = 10 % 1.1;

        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,IntLiteral(10),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test__all_true_compare_with_numbers_in_expression_(self):
        input = """
        void main(){
            boolean a;
            //INT
            a = 1 < 2;
            a = 1 > 2;
            a = 1 >= 2;
            a = 1 <= 2;
            //FLOAT
            a = 1.1 < 2.1;
            a = 1e1 > 2e1;
            a = 1.3e9 >= 2.3e9;
            a = 1.0001 <= 2.0001;
            a = 1 < 2.1;
            a = 1e1 > 2;
            a = 1 >= 2.3e9;
            a = 1.0001 <= 2;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test__compare_with_not_numbers_in_expression_(self):
        input = """
        void main(){
            boolean a;
            a = true < 8; 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(<,BooleanLiteral(true),IntLiteral(8))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test__all_true_bool_op_with_bool_int_in_expression_(self):
        input = """
        void main(){
            boolean a;
            a = true && true && true && true;
            a = false || true || true || true; 
            a = false || true && true || true; 
            a = 1 == 1;
            a = 2 != 1;
            a = true == true;
            a = false != true;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test__EQ_NEQ_op_with_diff_type_in_expression_(self):
        input = """
        void main(){
            boolean a;
            a = true == 1;

        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,BooleanLiteral(true),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test__return_in_main_path_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) a = a +1;
            return a;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test__return_in_main_path_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) a = a +1;
            return a;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test__not_return_in_main_path_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) a = a +1;
        }
        void main(){
            foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test___return_in_if_main_path_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) return a = a + 1;
        }
        void main(){
            foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test___return_in_if_not_in_else_main_path_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) return a = a + 1;
            else{}
        }
        void main(){
            foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test___return_in_if_and_in_else_main_path_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) return a = a + 1;
            else return a;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test___return_in_if_esle_in_if_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) if(a>0) return a = a + 1;
            else return a;
        }
        void main(){
            foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test___return_in_nested_if_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) 
                if(a>0) return a = a + 1; 
                else return a;
            else return a;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test___return_in_if__in_else_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) return a = a + 1;
            else if(a>0) return a = a + 1;
        }
        void main(){
            foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test___return_in_if_else__in_else_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) 
                return a = a + 1;
            else 
                if(a>0) 
                    return 1;
                else 
                    return a = a + 1;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test___return_in_if_else__in_else_(self):
        input = """
        int foo(){
            int a;
            a = 1 / 2;
            if (a < 1) 
                {
                    return a = a + 1;
                }
            else
            {
                if(a>0) 
                    return 1;
                else 
                    return a = a + 1;
            }
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test___return_for_(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            for (b = 1 ; b < 2 + 1 ; b = b--1) return 1;
        }
        void main(){
            foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test___return_for_and_in_main_path_(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            for (b = 1 ; b < 2 + 1 ; b = b--1) return 1;
            return b;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test___return__if_for__(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            for (b = 1 ; b < 2 + 1 ; b = b--1)
            {
                if (a == true) 
                    {
                        return b*8;
                    }
                else
                {
                    if(!a) 
                        return 1;
                    else 
                        return 1+-1;
                }
            }
            
        }
        void main(){
            foo();
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test___return___dowhile__(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            do 
                b = 1 + 1;
                return -10;
            while(a != true);
            
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test___return___dowhile_Block__(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            do 
                {
                    if (a == true) 
                        {
                            return b*8;
                        }
                    else
                        {
                            if(!a) 
                                return 1;
                            else 
                                return 1+-1;
                        }
                }
            while(a != true);
            
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test___continue___dowhile___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            do 
               b = b - -1;
                continue;
            while(a != true);
            return 1;
            
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test___continue__not_dowhile___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            do 
               b = b - -1;
                continue;
            while(a != true);
            continue;
        }
        void main(){
            foo();
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test___continue___for___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            for( b = 0; a = true ; b = b + 1)
            {
                if(b == 99999) continue;
            }
            return 1;
            
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test___continue__not_for___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            for( b = 0; a = true ; b = b + 1)
            {
                if(b == 99999) continue;
            }
            continue;
        }
        void main(){
            foo();
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test___break___dowhile___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            do 
               b = b - -1;
                break;
            while(a != true);
            return  b;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test___break__not_dowhile___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            do 
               b = b - -1;
                break;
            while(a != true);
            break;
        }
        void main(){
            foo();
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test___break___for___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            for( b = 0; a = true ; b = b + 1)
            {
                if(b == 99999) break;
            }
            return 1 - -b;
            
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test___break__not_for___(self):
        input = """
        int foo(){
            boolean a;
            int b;
            a =  false || true ;
            for( b = 0; a = true ; b = b + 1)
            {
                if(b == 99999) break;
            }
            break;
        }
        void main(){
            foo();
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test____invoke_func___(self):
        input = """
        int foo(){
            return 1;
        }
        void main(){
            foo();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test____invoke_func_in_itself___(self):
        input = """
        int foo(){
            foo();
            return 1;
        }
        void main(){
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test____invoke_func_in_itsel___(self):
        input = """
        int foo(int a[] ,float b[] ,boolean c[], string d[] ,int a1, float b1 ,float b2,boolean c2)
        {
            return 1;
        }
        boolean[] bool(){
            boolean a[1];
            return a;
        }
        void main(float b[]){
            int a[2];
            string d[99];
            foo(a,b,bool(),d,a[0],b[1],a[1],bool()[0]);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test____void_in_Assign___(self):
        input = """
        void foo(){
        }
        void main(){
            foo() = 1; 
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,CallExpr(Id(foo),[]),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 501))

    def test____func_return_array_pointer_in_Assign___(self):
        input = """
        int[] foo(int a[]){
            return a;
        }
        void main(){
            foo() = 1; 
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 502))

    def test____IntLit_LHS_in_Assign___(self):
        input = """
        void main(){
            1 = 1; 
        }
        """
        expect = "Not Left Value: BinaryOp(=,IntLiteral(1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 503))

    def test____FloatLit_LHS_in_Assign___(self):
        input = """
        void main(){
            1.1 = 1; 
        }
        """
        expect = "Not Left Value: BinaryOp(=,FloatLiteral(1.1),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input, expect, 504))

    def test____BooleanLit_LHS_in_Assign___(self):
        input = """
        void main(){
            true = 1.1; 
        }
        """
        expect = "Not Left Value: BinaryOp(=,BooleanLiteral(true),FloatLiteral(1.1))"
        self.assertTrue(TestChecker.test(input, expect, 505))

    def test____StringLit_LHS_in_Assign___(self):
        input = """
        void main(){
            "PPL" = true; 
        }
        """
        expect = "Not Left Value: BinaryOp(=,StringLiteral(PPL),BooleanLiteral(true))"
        self.assertTrue(TestChecker.test(input, expect, 506))

    def test____Built_in_func_for_StringLit_in_Assign___(self):
        input = """
        void main(){
            string a;
            a = "PPL";
            putString("PPL");
            putStringLn(a); 
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 507))

    def test____Redeclared_built_int_func___(self):
        input = """
        int getInt(){
            return 1;
        }
        int main(){
            return 1; 
        }
        """
        expect = "Redeclared Function: getInt"
        self.assertTrue(TestChecker.test(input, expect, 508))

    def test____Undeclared_variable____(self):
        input = """
        int foo(){
            return 1;
        }
        int main(){ 
            foo = 1;
            return 1;
        }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 509))

    def test____Undeclared_Function___(self):
        input = """
        int foo;

        int main(){ 
            foo();
            return 1;
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 510))

    def test____Undeclared_Var_Same_name_with_Func___(self):
        input = """
        int foo(){
            return 1;
        }

        int main(){ 
            foo[1] = 1;
            return 1;
        }
        """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input, expect, 511))

    def test____NOT_OP___(self):
        input = """
        int foo(){
            return 1;
        }

        int main(){ 
            boolean a;
            a = !true;
            a = !!!!!!false;
            foo();
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 512))

    def test____SUB_UNARY_OP___(self):
        input = """
        int foo(){
            return 1;
        }

        int main(){ 
            int a;
            a = -1;
            return foo()-------a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 513))

    def test____NUMBER_OP_WITH_FUNC_RETURN_NUMBER_TYPE___(self):
        input = """
        int fooInt(){
            return 1;
        }
        
        float fooFloat(){
            return 1.1e-8;
        }

        void main(){ 
            int a ;
            float b;
            a = -fooInt() + fooInt() - fooInt() * fooInt() / fooInt() %  fooInt();
            b = -fooInt() + fooFloat() - fooInt() * fooFloat() / fooInt();
            int c[100];
            c[getInt()] = 1;
            c[fooInt() - 1] = 1;
            c[c[c[fooInt() - c [getInt()]]]] = fooInt() - getInt();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 514))
