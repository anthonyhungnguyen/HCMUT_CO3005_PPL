import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_print_an_int(self):
        """Simple program: int main() {} """
        input = """
        void main() {
            putInt(1);
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test_print_an_float(self):
        input = """
        void main() {
            putFloat(1.3);
        }

        """
        expect = "1.3"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_print_another_float(self):
        input = """
        void main() {
            putFloatLn(1);
        }

        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_print_a_string(self):
        input = """
        void main() {
            putString("abc");
        }

        """
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_print_a_boolean(self):
        input = """
        void main() {
            putBool(true);
        }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_print_a_global_int_variable_without_assign(self):
        input = """
        int a;
        void main() {
            putInt(a);
        }

        """
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_print_a_global_float_variable_without_assign(self):
        input = """
        float a;
        void main() {
            putFloat(a);
        }

        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_print_a_global_string_variable_without_assign(self):
        input = """
        string a;
        void main() {
            putString(a);
        }

        """
        expect = "null"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_print_a_global_boolean_variable_without_assign(self):
        input = """
        boolean a;
        void main() {
            putBool(a);
        }

        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_print_another_global_int(self):
        input = """
        int a, b;
        void main() {
            putBool(a);
        }

        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_print_another_global_float_with_assign_by_a_integer_number(self):
        input = """
        float a;
        void main() {
            a = 1;
            putFloat(a);
        }

        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_print_a_negative_integer(self):
        input = """
        void main() {
            putInt(-1);
        }
        """
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_print_a_negative_float(self):
        input = """
        void main() {
            putFloat(-12.11);
        }

        """
        expect = "-12.11"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_print_a_not_boolean(self):
        input = """
        void main() {
            putBool(!false);
        }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_print_a_assigned_int_variable(self):
        input = """
        void main() {
            int a;
            a = 1;
            putInt(a);
        }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_print_a_assigned_float_variable(self):
        input = """
        void main() {
            float a;
            a = 1.2;
            putFloatLn(a);
        }

        """
        expect = "1.2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_print_another_assigned_float_variable(self):
        input = """
        void main() {
            float a;
            a = 1;
            putFloatLn(a);
        }

        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_print_a_assigned_string_variable(self):
        input = """
        void main() {
            string a;
            a = "haha";
            putString(a);
        }

        """
        expect = "haha"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_print_another_assigned_string_variable(self):
        input = """
         void main() {
            string a, b;
            a = "haha";
            a = b;

            putString(a);
        }

        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_print_result_of_a_more_complex_assignment_for_int(self):
        input = """
        void main() {
            int a, b;
            a = b = 1;
            putInt(b);
        }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_print_result_of_another_complex_assignment_for_float(self):
        input = """
        void main() {
            float a, b;
            b = 2;
            a = b = b + 1;

            putFloatLn(a);
            putFloatLn(b);
        }

        """
        expect = "3.0\n3.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_print_result_of_another_complex_assignment(self):
        input = """
        void main() {
            int a;
            float b;
            b = a = 1;
            putFloatLn(b);
        }

        """
        expect = "1.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_print_a_result_of_simple_binary_expr_of_plus_and_between_int_int(self):
        input = """
        void main() {
            putIntLn(3+2);
        }

        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_print_a_result_of_more_complex_binary_expr_of_plus_between_int_int(self):
        input = """
        void main() {
            putIntLn(1+2+1+1);
        }

        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_print_a_result_of_simple_binary_expr_of_minus_between_int(self):
        input = """
        void main() {
            putIntLn(3-1);
        }

        """
        expect = "2\n"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_print_a_result_of_more_complex_binary_expr_of_minus_between_int_int(self):
        input = """
        void main() {
            putIntLn(17-2-4);
        }

        """
        expect = "11\n"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_print_a_result_of_simple_binary_expr_of_plus_between_float_int(self):
        input = """
        void main() {
            putFloat(3.1+1);
        }

        """
        expect = "4.1"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_print_a_result_of_more_complex_binary_expr_of_plus_between_float_int(self):
        input = """
        void main() {
            putFloat(3.1+1+4.4+6);
        }

        """
        expect = "14.5"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_print_a_result_of_simple_binary_expr_of_minus_between_float_int(self):
        input = """
        void main() {
            putFloat(3-1.2);
        }

        """
        expect = "1.8"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_print_a_result_of_more_complex_binary_expr_of_plus_minus_between_int(self):
        input = """
        void main() {
            putInt(4-2+1);
        }

        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_print_a_result_of_more_complex_binary_expr_of_plus_minus_between_float_int(self):
        input = """
        void main() {
            putFloat(4-2+1+2.3+5);
        }

        """
        expect = "10.3"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_print_a_result_of_binary_expr_of_mul_between_int(self):
        input = """
        void main() {
            putInt(4*2*3);
        }

        """
        expect = "24"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_print_a_result_of_binary_expr_of_divide_between_int(self):
        input = """
        void main() {
            int a;
            a = 2;
            putInt(42/a/3);
        }

        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_print_a_result_of_binary_expr_of_divide_between_float(self):
        input = """
        void main() {
            float b;
            b = 36.6;
            putFloat(b/3/2);
        }

        """
        expect = "6.1"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_print_a_result_of_more_complex_binary_expr_of_mul_divide_between_int(self):
        input = """
        void main() {
            putInt(36/3/2*2);
        }

        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_print_a_result_of_more_complex_binary_expr_of_mul_divide_between_float(self):
        input = """
        void main() {
            putFloat(2*3.5*2/6*9);
        }

        """
        expect = "21.0"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_print_a_result_of_more_complex_binary_expr_of_add_minus_mul_divide_between_int_float(self):
        input = """
        void main() {
            int a, b;
            a = b = 2;
            putFloat(a*3.5*b/6*9);
        }

        """
        expect = "21.0"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_print_a_result_of_a_simple_binary_expr_of_MOD(self):
        input = """
        void main() {
            int a;
            a = 5;
            putInt(5 % 2);
        }

        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_print_a_result_of_binary_expr_of_MOD_and_other_binary_ops(self):
        input = """
        void main() {
            int a, b;
            float c;
            a = 13;
            b = 3;
            c = a % b + 1.0/2;
            putFloat(c);
        }

        """
        expect = "1.5"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_print_a_result_of_more_complex_binary_expr_of_DIV_MOD_and_other_binary_ops(self):
        input = """
        void main() {
            int a, b;
            float c;
            a = 13;
            b = 3;
            c = (a / 5 + 5) % 4;
            putFloat(c);
        }

        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_print_another_result_of_more_complex_binary_expr_of_DIV_MOD_and_other_binary_ops(self):
        input = """
        void main() {
            int a, b;
            float c;
            a = 13;
            b = 3;
            c = (a / 5 + 5) % 4;
            putFloat(c);
        }

        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_print_a_result_of_a_more_complex_simple_binary_expr_of_MOD_and_other_binary_ops(self):
        input = """
        void main() {
            int a, b;
            float c;
            a = 13;
            b = 3;
            c = (a % 5 + 5) % 5;
            putFloat(c);
        }

        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_print_a_result_of_simple_binary_expr_of_LargerThan_between_int(self):
        input = """
        int a;
        void main() {
            int b;
            a = b = 2;
            b = a * 3 - 3;
            putBool(a < b);
        }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_print_a_result_of_simple_binary_expr_of_AND_between_simple_binary_expressions(self):
        input = """
        float a;
        void main() {
            int b;
            a = b = 2 - 1;
            putBool((a<b+1.2) && (a+3>b));
        }

        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_print_a_result_of_a_more_complex_expr_of_AND_between_element_of_bool_type(self):
        input = """
        boolean a, d;
        void main() {
            int b, c;
            a = true;
            b = 4;
            c = 2 * b - 3;
            putBool((b>2) && (c<10) && a && d);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_print_another_result_of_a_more_complex_expr_of_AND_between_element_of_bool_type(self):
        input = """

       void main() {
           float a;
           int b;
           a = 0;
           b = 1;
           if (a>= b && b < 0) {
               putInt(1);
           }
       }
        """
        expect = ""
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_print_a_result_of_simple_binary_expr_of_OR_between_simple_binary_expressions(self):
        input = """
        void main() {
            int a, b;
            b = a = 1;
            a = b = 2 * 3 - a;
            putBool((a+1>2) || (b-1<3));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_print_a_result_of_a_more_complex_expr_of_OR_between_element_of_bool_type(self):
        input = """
        boolean a;
        void main() {
            int b, c;
            a = true;
            b = 4;
            c = 2 * b - 3;
            putBool((b<2) || (c<10) || a);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_print_another_result_of_a_more_complex_expr_of_OR_between_element_of_bool_type(self):
        input = """
        boolean a;
        void main() {
            int b, c;
            a = true;
            b = 4;
            c = 2 * b - 3;
            putBool((b<2) || !(c<10) || !a);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_print_another_result_of_a_more_complex_expr_of_OR_AND_between_element_of_bool_type(self):
        input = """
        boolean a;
        void main() {
            int b, c;
            a = true;
            b = 4;
            c = 2 * b - 3;
            putBool((b<2) || !(c<10) && a);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_print_result_of_simple_binary_expr_of_EQUAL(self):
        input = """

        void main() {
            int a, b;
            a = 1;
            b = 3 * a - 1;
            putBool(b == 2);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_print_result_of_more_complex_binary_expr_of_EQUAL_with_other_binary_operations(self):
        input = """

        void main() {
            int a, b;
            a = 1;
            b = 3 * a - 1;
            putBool((b==2) && (b % 2 == 0));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_print_result_of_simple_binary_expr_of_DIFFERENT(self):
        input = """
        void main() {
            int a, b;
            a = 1;
            b = 3 * a - 1;
            putBool(b!=2);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_print_result_of_more_complex_simple_binary_expr_of_DIFFERENT_with_other_binary_operations(self):
        input = """
        void main() {
            int a, b;
            a = 1;
            b = 3 * a - 1;
            putBool((b != 1) && (b != 3));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_print_result_of_a_complex_binary_binary_expr_of_DIFFERENT_and_EQUAL_and_other_binary_operations(self):
        input = """
        void main() {
            int a, b;
            a = 1;
            b = 2;
            putBool((b != 1) == (a != 1));
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_print_result_of_another_a_complex_binary_binary_expr_of_DIFFERENT_and_EQUAL_and_other_binary_operations_1(self):
        input = """
        void main() {
            int a, b;
            a = 1;
            b = 2;
            putBool((b!=1) != (a != 1));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_print_result_of_another_a_complex_binary_binary_expr_of_DIFFERENT_and_EQUAL_and_other_binary_operations_2(self):
        input = """
        void main() {
            int a, b;
            a = 1;
            b = 2;
            putBool((b!=1) != (a != 1));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_print_1_using_a_function_call_with_no_input(self):
        input = """
        void print1() {
            putInt(1);
        }
        void main() {
            print1();
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_print_sum_of_2_number_using_a_function_call_with_no_return(self):
        input = """
        void printSum(int a, int b) {
            putInt(a+b);
        }
        void main() {
            printSum(3,4);
        }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_print_result_of_a_sum_of_interger_using_function_return_result(self):
        input = """
        int sum(int a, int b) {
            return a + b;
        }
        void main() {
            int a, b;
            a = b = 1;
            b = a + 1;
            putInt(sum(a,b));
        }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_print_result_of_a_multiplication_of_float_using_function(self):
        input = """
        void main() {
            float a, b;
            b = 3;
            a = mul(1.2,2.0);
            putFloat(mul(b,a));
        }
        float mul(float a, float b) {
            return a * b;
        }
        """
        expect = "7.2000003"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_print_result_of_test_using_integer_into_float_input_function(self):
        input = """
        float x2Float(float a) {
            int i;
            i = 2;
            return a * i;
        }
        void main() {
            int a;
            a = 3;
            putFloat(x2Float(a));
        }
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_print_a_first_element_of_array_that_is_assigned_through_calling_function(self):
        input = """
        int foo() {
            int i;
            i = 2;
            return i;
        }

        void main () {
            putInt(foo());
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_print_another_first_element_of_array_that_is_assigned_through_calling_function(self):
        input = """
        float foo(float i) {
            return i;
        }
        int a;
        void main() {
            a = 3;
            putFloat(foo(3));
        }
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_print_result_of_test_using_a_result_of_a_function_as_input_to_call_other_function(self):
        input = """
        float add(float a) {
            return a + 1;
        }
        void main() {
            int a;
            a = 3;
            putFloatLn(add(add(3)));
        }
        """
        expect = "5.0\n"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_print_list_of_smaller_numbers_than_the_input_value_using_a_simple_recursive_function(self):
        input = """
        void printNum(int a) {
            if (a > 0) {
                putInt(a);
                a = a - 1;
                printNum(a);
            }
        }

        void main() {
            printNum(7);
        }
        """
        expect = "7654321"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_print_result_of_a_recursive_function_call(self):
        input = """
        void printInt(int n) {
            if (n > 0) {
                printInt(n - 1);
                putInt(n);
            }
        }

        void main() {
            printInt(9);
        }
        """
        expect = "123456789"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_print_result_of_sum_of_two_return_result_of_call_expr(self):
        input = """
        int mul(int a, int b) {
            return a * b;
        }

        void main() {
            putInt(mul(2,3) + mul(4,5));
        }
        """
        expect = "26"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_print_result_of_and_of_two_return_result_of_call_expr(self):
        input = """
        boolean bigger(int a, int b) {
            return a > b;
        }

        void main() {
            putBool(bigger(4,3) && bigger(2,5));
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_print_result_of_or_of_two_return_result_of_call_expr(self):
        input = """
        boolean divBy2(int a) {
            return (a % 2) == 0;
        }
        void main() {
            putBool(divBy2(5) || divBy2(4));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_fibonacci_number_function(self):
        input = """
        int fibonacci(int n)
        {
         if(n==1|| n==2)
           return 1;
         else return fibonacci(n-1)+fibonacci(n-2);
        }
        void main()
        {
         putInt(fibonacci(5));
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_return_a_boolean(self):
        input = """
       boolean isOdd(int val)
        {
         return val % 2 ==1;
        }
        void main()
        {
        putBoolLn(isOdd(3));
        putBoolLn(isOdd(2));
        }
        """
        expect = "true\nfalse\n"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def combine_add_mul_op_int_float(self):
        input = """
        void main()
        {
        int x;
        float y;
        x=2;
        y=1.0;
        putFloatLn((x+y)/x);
        putFloatLn((x*y)/(x-y));
        putFloatLn((x+y)/x-(x*y)/(x-y));
        }
        """
        expect = "1.52.0-0.5"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_print_result_of_assigned_variable_using_a_if_stmt_without_else(self):
        input = """
        int a;
        void main() {
            if ((a<3) && (a==0)) {
                a = 2;
            }
            putInt(a);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_print_result_of_assigned_variable_using_a_more_complex_if_stmt_without_else(self):
        input = """
        int a;
        void main() {
            a = 1;
            if ((a<3) && (a==1) && (a>0)) {
                a = 5;
            }
            putInt(a);
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_print_result_of_calling_function_using_a_if_stmt_with_else(self):
        input = """
        void main() {
            int a, b;
            float c;
            a = 2;
            b = 3;
            if (a>b) {
                c = sum(a, b);
            } else {
                c = mul(a, b);
            }
            putFloat(c);
        }

        int sum(int a, int b) {
            int result;
            result = a + b;
            return result;
        }

        boolean z;

        int mul(int a, int b) {
            int result;
            result = a * b;
            return result;
        }
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_print_2_result_of_a_more_complex_if_with_else(self):
        input = """
        void main() {
            int a, b;
            b = 2;
            a = 2*b-1;
            if ((a<b) && ((a+2*b)>=2)) {
                a = b;
                b = 2*a+1;
            } else {
                a = 2;
                b = 3;
                b = b + 1;
            }
            putIntLn(a);
            putIntLn(b);
        }

        """
        expect = "2\n4\n"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_print_result_variable_modified_with_if_statement_inside_another_if_stmt_without_else(self):
        input = """
        void main() {
            int a;
            a = 4;
            if (a > -1) {
                if (a > 1) {
                    if (a % 2 == 0) {
                        a = 3;
                    }
                }
            }
            putInt(a);
        }

        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_print_result_variable_modified_with_another_if_statement(self):
        input = """
        void main() {
            int a;
            a = 2;
            if (a > 1) {
                a = a + 1;
                putInt(a);
            }
            else {
                putInt(a - 1);
            }
        }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_simple_callexpr_to_print_string(self):
        input = """
        string getText(int n){
            if(n%2==0)
            return "so chan";
            else
            return "so le";
            }
        void main()
        {
        putStringLn(getText(2));
        putStringLn(getText(1));
        }
        """
        expect = "so chan\nso le\n"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_print_result_of_boolean_using_call_expr_to_check_if_the_input_is_odd_number(self):
        input = """
        void main() {
            putBool(checkIfOdd(12));
        }
        boolean checkIfOdd(int num) {
            if ((num % 2) == 0) {
                return 0;
            } else {
                return 1;
            }
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_print_resul_of_variable_after_modified_with_a_simple_for_stmt(self):
        input = """
        void main() {
            int a;
            for(a = 0; a <= 5; a=a+1) {
                putInt(a);
            }
        }
        """
        expect = "012345"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_print_result_of_variable_after_modified_with_for_stmt_that_contains_if_stmt(self):
        input = """
        void main() {
            int a, i;
            a = 1;
            for (i = 0 ; i <= 4; i=i+1) {
                a = a + 2;
            }
            putFloat(a);
        }
        """
        expect = "11.0"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_print_result_of_variable_after_modified_with_for_stmt_that_contains_another_for_stmt(self):
        input = """
        void main() {
            int a, i;
            for (i = 0; i <= 2; i = i + 1) {
                for (a = 0; a <= 2; a = a + 1) {
                    putInt(a);
                }
            }
        }
        """
        expect = "012012012"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_print_or_boolean(self):
        input = """
        void main() {
            putBool(true||true);
            putBool(true||false);
            putBool(false||true);
            putBool(false||false);
        }
        """
        expect = "truetruetruefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_print_return_result_of_a_function_that_contain_for_stmt(self):
        input = """
        void main() {
            int a;
            a = getPower(3,5);
            putIntLn(a);
        }

        int getPower(int a, int b) {
            int i, c;
            c = 1;
            for(i = 0; i < b; i=i+1) {
                c = c * a;
            }
            return c;
        }
        """
        expect = "243\n"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_print_result_of_variable_after_modified_with_a_simple_while_stmt(self):
        input = """
        void main() {
            int a;
            a = 1;
            do {
                putInt(a);
                a = a + 1;
            } while(a < 5);
        }
        """
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_print_result_of_variable_after_modified_with_while_stmt_that_contain_another_while_stmt(self):
        input = """
        void main() {
            int a, b, c;
            a = 1;
            c = 2;
            do {
                b = 1;
                do {
                    c = c * 2;
                    b = b + 1;
                } while(b<5);
                a = a+1;
            } while(a<5);
            putInt(c);
        }
        """
        expect = "131072"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_compare_float_greater_than(self):
        input = """
        void main() {
            putBool(1.2>2.0);
            putBool(2.4>2.4);
            putBool(2.2>1.6);
        }
        """
        expect = "falsefalsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_print_result_of_a_variable_after_modified_with_a_simple_for_statement_that_contain_break_stmt(self):
        input = """
        void main() {
            int i;
            for (i = 5; i >= 0; i=i-1) {
                break;
            }
            putInt(i);
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_print_result_of_a_variable_after_modified_with_a_more_complex_for_statement_that_contain_break_stmt(self):
        input = """
        void main() {
            int i;
            for (i = 0; i <= 12; i=i+1) {
                if (i > 8) {
                    break;
                } else {
                    if (i < 5) {
                        i = 2 * i + 1;
                    }
                }
            }
            putIntLn(i);
        }
        """
        expect = "9\n"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_print_result_of_a_variable_after_modified_with_a_simple_while_statement_that_contain_break_stmt(self):
        input = """
        void main() {
            int a;
            a = 1;
            do {
                a = a + 1;
                break;
            } while (a<=10);
            putInt(a);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_print_result_of_a_variable_after_modified_with_a_more_complex_while_statement_that_contain_break_stmt(self):
        input = """
        int x;
        void main() {
            x = 1;
            do {
                x = x + 1;
                if ((x % 2 == 0) && (x>4)) {
                    break;
                }
            } while(x<6);
            putInt(x);
        }
        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_print_not_boolean(self):
        input = """
        void main() {
            putBool(!true);
            putBool(!false);
        }
        """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_print_result_of_a_variable_after_modified_with_a_simple_for_statement_that_contain_continue_stmt(self):
        input = """
        void main() {
            int x, i;
            i = 0;
            for (x = 1; x <= 10; x=x+1) {
                if ((x % 2) == 0) continue;
                i = i + 1;
            }
            putIntLn(i);
        }
        """
        expect = "5\n"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_print_result_of_variable_after_modified_with_a_more_complex_for_statement_that_contain_continue_stmt(self):
        input = """
        void main() {
            int a;
            for (a = 1; a <= 5; a=a+1) continue;
            putInt(a);
        }

        """
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_print_result_of_variable_after_modified_with_a_more_complex_while_statement_that_contain_continue_stmt(self):
        input = """
        void main() {
            int a;
            a = 1;
            do {
                a = a + 1;
                for (a = 5; a <= 12; a = a + 1) continue;
                break;
            } while(a<=10);
            putInt(a);
        }

        """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_print_the_result_of_return_in_function_that_return_the_result_of_another_function(self):
        input = """
        int getDouble(int a) {
            return a * 2;
        }

        void main() {
            putInt(getMaxDouble(5,2));
        }

        int getMaxDouble(int a, int b) {
            if (a > b) {
                return getDouble(a);
            }
            return getDouble(b);
        }

        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_print_the_result_of_return_in_function_that_using_binary_operation_AND(self):
        input = """
        boolean ifBiggerAndDivBy2(int a, int b) {
            return ((a>b) && ((a%2) == 0));
        }

        void main() {
            putBool(ifBiggerAndDivBy2(5,2));
        }

        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_print_the_result_of_return_in_function_that_using_binary_operation_OR(self):
        input = """
        boolean ifBiggerAndDivBy2(int a, int b) {
            return ((a>b) && ((a%2) == 0));
        }

        void main() {
            putBool(ifBiggerAndDivBy2(5,2));
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 599))
