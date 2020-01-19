import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_undeclared_variable(self):
        input = """
        void main() {
            a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared_global_variable(self):
        input = """int a;
        int b;
        int a;
        void main() {

        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared_function(self):
        input = """void main(int a, int b) {

        }
        void main() {

        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared_function_variable(self):
        input = """void main () {
            return;
        }
        int foo(int a) {
            int a;
            return a;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_declared_but_using_in_different_block(self):
        input = """void main () {
            {
                int a;
            }
            {
                a;
            }
        }"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared_parameter(self):
        input = """void main() {

        }
        int foo(int a, int a) {

        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_break_alone(self):
        input = """void main() {
            break;
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_continue_alone(self):
        input = """void main() {
            continue;
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_break_in_if(self):
        input = """void main() {
            if(true) {
                break;
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_continue_in_if(self):
        input = """void main() {
            if(true) {
                continue;
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_break_outside_forloop(self):
        input = """
        void main() {
            int a;
            for (a=5; a<10; a=a+1) {

            }
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_continue_outside_forloop(self):
        input = """
        void main() {
            int a;
            for (a=5; a<10; a=a+1) {

            }
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_break_outside_dowhile(self):
        input = """
        void main() {
            int a;
            do {

            } while(a<1);
            continue;
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_has_entry_point_main_with_param(self):
        input = """
        void main(int a) {
            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_no_entry_point_no_main(self):
        input = """
        int foo() {

        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_has_entry_point_main_not_with_void_type(self):
        input = """
        int main() {
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_no_entry_point_with_complex_program(self):
        input = """
        float foo(int a) {

        }
        string[] lala(float b) {

        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_simple_unreachable_function(self):
        input = """
        void main() {

        }
        int foo() {
            int a;
            return a;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_unreachable_function_self_call(self):
        input = """
        void main() {

        }
        int foo() {
            int a;
            foo();
            return a;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_complex_unreachable_function(self):
        input = """
        void main() {
            int a;
            if (a==1) {

            } else {
                {
                    {
                        {
                            foo();
                        }
                    }
                }
            }
        }
        void foo() {
            int a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_simple_function_not_return(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_function_return_in_if(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a;
            if (a==1) {
                return a;
            }
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_function_return_in_else(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a;
            if (a==1) {

            } else {
                return a;
            }
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_function_return_in_if_else(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a;
            if (a==1) {
                return a;
            } else {
                return a;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_function_return_in_nesed_if_else(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a,b,c,d,e,f;
            if (a==1) {
                if(b==2) {
                    if(c==3) {
                        if(d==4) {
                            if(e==5) {
                                if(f==6) {
                                    return a;
                                } else {
                                    return b;
                                }
                            }
                        }
                    }
                }
            }
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_function_return_outmost(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a,b,c,d,e,f;
            if (a==1) {
                if(b==2) {
                    if(c==3) {
                        if(d==4) {
                            if(e==5) {
                                if(f==6) {
                                    a=a+1;
                                } else {
                                    b=b+1;
                                }
                            }
                        }
                    }
                }
            }
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_function_in_for(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a;
            for(a=5;a<10;a=a+1) {
                return a;
            }
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_function_in_do_while(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a;
            do {
                return a;
            } while(a<1);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_function_in_if_and_for(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a;
            if(a<10) {
                for (a=1; a<5; a=a+1) {
                    return a;
                }
            } else {
                return a;
            }
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_function_in_if_and_dowhile(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a;
            if(a<10) {
                do {
                    return a;
                } while(a>5);
            } else {
                return a;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_function_in_two_continuous_if_else(self):
        input = """
        void main() {
            foo();
        }
        int foo() {
            int a,b;
            if (a==1) {
                return a;
            } else {
                return a;
            } if (b==1) {

            } else {

            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_simple_not_left_value(self):
        input = """
        void main() {
            int a;
            3 = a+1;
        }
        """
        expect = "Not Left Value: BinaryOp(=,IntLiteral(3),BinaryOp(+,Id(a),IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_okay_left_value_with_variable(self):
        input = """
        void main() {
            int a;
            a = a+1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_okay_left_value_index_expression(self):
        input = """
        void main() {
            int a[5];
            a[4] = 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_mismatchexp_left_int_right_boolean(self):
        input = """
        void main() {
            int a;
            boolean b;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_mismatchexp_left_int_right_string(self):
        input = """
        void main() {
            int a;
            string b;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_mismatchexp_left_int_right_float(self):
        input = """
        void main() {
            int a;
            float b;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_mismatchexp_left_int_right_int(self):
        input = """
        void main() {
            int a,b ;
            a = b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_mismatchexp_left_float_right_int(self):
        input = """
        void main() {
            float a;
            int b;
            a = b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_mismatchexp_left_float_right_float(self):
        input = """
        void main() {
            float a, b;
            a = b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_mismatchexp_left_boolean_right_not_boolean(self):
        input = """
        void main() {
            boolean a;
            int b;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_mismatchexp_left_boolean_right_boolean(self):
        input = """
        void main() {
            boolean a,b;
            a = b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_mismatchexp_left_string_right_not_string(self):
        input = """
        void main() {
            string a;
            float b;
            a = b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_mismatchexp_left_string_right_string(self):
        input = """
        void main() {
            string a, b;
            a = b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_mismatchexp_array_subing_E1_not_array_type(self):
        input = """
        void main() {
            int a;
            a[5] = 3;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_mismatchexp_array_subing_E2_not_integer(self):
        input = """
        void main() {
            int a[5];
            a[5.5] = 3;
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_mismatchexp_funcall_actual_param_not_same_as_formal_param(self):
        input = """
        void main() {
            foo();
        }
        void foo(int a) {

        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_mismatchexp_funcall_not_same_type(self):
        input = """
        void main() {
            float a;
            foo(a);
        }
        void foo(int a) {

        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_mismatchexp_funcall_LHS_float_RHS_int(self):
        input = """
        void main() {
            int a;
            foo(a);
        }
        void foo(float a) {

        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_mismatchexp_funcall_LHS_float_RHS_float(self):
        input = """
        void main() {
            float a;
            foo(a);
        }
        void foo(float a) {

        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_mismatchexp_plus_LHS_string_RHS_string(self):
        input = """
        
        void main() {
        string a;
        a="a" + "abc";   
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,StringLiteral(a),StringLiteral(abc))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_redeclared_function_in_global_scope(self):
        input = """
        int foo;
        int foo() {

        }
        void main() {

        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_mismatchstmt_if_exp_string(self):
        input = """
        void main() {
            if ("hello") {

            }
        }
        """
        expect = "Type Mismatch In Statement: If(StringLiteral(hello),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_mismatchstmt_else_if_float(self):
        input = """
        void main() {
            if (5.5) {

            } else {

            }
        }
        """
        expect = "Type Mismatch In Statement: If(FloatLiteral(5.5),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_mismatchstmt_for_exp1_error(self):
        input = """
        void main() {
            float i;
            for (i=1.1; i< 10; i=i+1) {

            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),FloatLiteral(1.1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_mismatchstmt_for_exp2_error(self):
        input = """
        void main() {
            int i;
            for (i=1; i=1; i=i+1) {

            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_mismatchstmt_for_exp3_error(self):
        input = """
        void main() {
            int i;
            for (i=1; i<10; true) {

            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BooleanLiteral(true);Block([]))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_mismatchstmt_do_while_exp_error(self):
        input = """
        void main() {
            int i;
            do {

            } while("lala");
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],StringLiteral(lala))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_mismatchstmt_void_return_something(self):
        input = """
        void main() {
            return 1.5;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(1.5))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_mismatchstmt_int_return_void(self):
        input = """
        void main() {
            
        }
        int a() {
            return;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_mismatchstmt_int_return_float(self):
        input = """
        void main() {
            
        }
        int a() {
            return 5.5;
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_mismatchstmt_float_return_int(self):
        input = """
        void main() {
            a();
        }
        float a() {
            return 5;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_mismatchstmt_int_return_int(self):
        input = """
        void main() {
            a();
        }
        int a() {
            return 5;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_mismatchstmt_array_pointer_type_return_int(self):
        input = """
        void main() {
            a();
        }
        int[] a() {
            return 5;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(5))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_mismatchstmt_int_array_pointer_type_return_int_array_type(self):
        input = """
        void main() {
            a();
        }
        int[] a() {
            int a[5];
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_mismatchstmt_float_array_pointer_type_return_int_array_type(self):
        input = """
        void main() {
            a();
        }
        float[] a() {
            int a[5];
            return a;
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_undeclared_used_before_declare(self):
        input = """
        void main() {
            a;
            int a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_undeclared_used_before_declare(self):
        input = """
        void main() {
            a;
            int a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_undeclared_declared_inner_scope_used_outer_scope(self):
        input = """
        void main() {
            {
                {
                    {
                        int a;
                    }
                }
            }
            a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_undeclared_declared_inner_scope_used_outer_scope(self):
        input = """
        void main() {
            {
                {
                    {
                        int a;
                    }
                }
            }
            a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_redeclared_function_samename_with_variable_global(self):
        input = """
        void main() {
            
        }
        int foo;
        void foo() {
            
        }
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_redeclared_variable_samename_with_function_global(self):
        input = """
        void main() {
            
        }
        void foo() {
            
        }
        int foo;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_redeclared_variable_different_type_global(self):
        input = """
        void main() {
            
        }
        string a;
        int a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_redeclared_variable_every_new_scope(self):
        input = """
        void main() {
            int a;
            {
                string a;
                {
                    boolean a;
                    {
                        float a;
                    }
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_redeclared_function_different_type(self):
        input = """
        void main() {
           
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))
