import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_one_int_var_decl(self):
        input = """int main() {
            int a;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))

    def test_many_int_var_decl(self):
        input = """int main() {
            int a,b,c;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_boolean_var_decl(self):
        input = """int main() {
            boolean flag;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_string_var_decl(self):
        input = """int main() {
            string s;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_float_var_decl(self):
        input = """int main() {
            float x,y,z;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_int_array_decl(self):
        input = """int main() {
            int d[5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_boolean_array_decl(self):
        input = """int main() {
            boolean flag[5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_float_array_decl(self):
        input = """int main() {
            float flag[5];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_string_array_decl(self):
        input = """int main() {
            string s[6];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_multiple_arr_decl(self):
        input = """int main() {
            int a[5],b[6];
            float x[5],y[10];
            string s[10];
            boolean flag[2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_func_decl(self):
        input = """int sum() {
            int a,b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_return_sum(self):
        input = """int sum(int a,int b) {
            return a+b;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_multiple_param_vardecl(self):
        input = """void sum(int i,string s, boolean flag) {
            int a, b, c;
            boolean x;
            string g;
            float q,w;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_array_param(self):
        input = """void sum(int i,float f[], boolean flag) {
            int a, b, c;
            boolean x;
            string g;
            float q, w;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_assign(self):
        """ Test Assign Statement"""
        input = """void sum(int i,string s, boolean flag) {
            int a,b,c;
            a = i;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_many_assign(self):
        input = """void sum(int i,string s, boolean flag) {
            int a,b,c;
            a = i;
            b = c = 5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_assign_arr(self):
        input = """void sum(int i,string s, boolean flag) {
            int a,b,c;
            a = i[10];
            b = c = 5;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_assign_arr_with_sum(self):
        input = """void sum() {
            x = a[10] + 3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_assign_with_sum_subtract(self):
        input = """void sum() {
            x = a + b + c - d;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_assign_string(self):
        input = """void sum() {
            x = "Hello World";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_assign_param_array(self):
        input = """void sum(int arr[]) {
            int m,n;
            x = arr[2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_builtin_func(self):
        input = """void sum() {
            getLn(5);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_wrong_close(self):
        input = """int main(){
            int a,b;
            a = b = 5;    
        )"""
        expect = "Error on line 4 col 8: )"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_many_if_else(self):
        input = """void foo(float x) {
            float t;
            if (a > 1) {
                a = 1;
            } else if (a > b) {
                c = d;
            } else {
                d = c;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_more_if_else(self):
        input = """void foo(float x) {
            float t;
            if (a > 1) {
                a = 1;
            } else {
                sum();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_if_else_with_complex_cond(self):
        input = """void foo(int a, int b) {
            if (a > 1 || b < 10) {
                a = b;
            } else {
                b = sum();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_if_if_else(self):
        input = """void foo(int a, int b) {
            if (a > 1 || b < 10) {
                a = b;
            }
            if (a == b) {
                b = b + 1;
            } else {
                a = a + 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_if_if_else_2(self):
        input = """void foo(int a, int b) {
            if (a > 1 || b < 10) {
                a = b;
            }
            if (1 < 2) {
                b = b + 1;
            } else {
                a = a + 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_nested_if_else(self):
        input = """void foo(int a, int b) {
            if (a > 1 || b < 10) {
                a = b;
                if (1 < 2) {
                    b = b + 1;
                } else {
                    a = a + 1;
                }
            }
            
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_do_while_statement(self):
        input = """void foo(int a, int b) {
            do {
                a = a + 1;
            } while a < 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_do_while_statement_with_many_blocks(self):
        input = """void foo(int a, int b) {
            do {
                {
                    a = a + 1;
                }
            } while a < 1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_do_while_statement_with_paren(self):
        input = """void foo(int a, int b) {
            do {
                a = a + 1;
            } while (a < 1);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_index_expression_with_two_squareB(self):
        input = """void foo(int a, int b) {
            x = foo[12][34];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_simple_for_statement(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        s = s + 1;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_for_if_statement(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        if (a == 1) {
                            s = s - 1;
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_two_for_one_if_statements(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        for (j = 1; j < 100; j=j+1) {
                            s = s + 1;
                            if (s == 1) {
                                s = s -1;
                            }
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_two_for_one_do_while_statements(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        for (j = 1; j < 100; j=j+1) {
                            do {
                                x = x + 10*5/6;
                            }
                            while (x>1);
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_break_statement(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        for (j = 1; j < 100; j=j+1) {
                            break;
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_continue_statement(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        for (j = 1; j < 100; j=j+1) {
                            if (x+6>7) continue;
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_return_statement(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        for (j = 1; j < 100; j=j+1) {
                            if (x+6>7) return;
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_for_statement_if_return_statement(self):
        input = """void foo(int a, int b) {
                    for (i = 1; i < 10; i=i+1) {
                        for (j = 1; j < 100; j=j+1) {
                            if (x+6>7) return sum(1+1);
                        }
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_simple_func_call(self):
        input = """void foo(int a, int b) {
                    sum(3,a+1);
                    sum1();
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_func_call_in_return(self):
        input = """void foo(int a, int b) {
                    sum(3,a+1,a[2]);
                    return sum(111,222);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_nested_function_call(self):
        input = """void foo(int a, int b) {
    a(b(c()));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_nested_if_with_func_call(self):
        input = """void main() {
            if (a==b) {
                b = c;
                if (a!=c+1) {
                    sum(a,c);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_nested_if_else_with_do_while(self):
        input = """void main() {
           if (a==b) {
               if(c==d) {
                   do{

                   } while(d==e);
               }
               else {
                   c = c + 1;
               }
           }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_many_func_declare_with_func_call_and_var_decl(self):
        input = """
            int i;
            int f() {
               return ;
            }
            int main() {
                main = f();
                putIntLn(main);
                do {
                    main = f = i = 100;
                    putIntLn(i);
                    putIntLn(main);
                    putIntLn(f);
                } while (putIntLine(main));
                float g;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_ass_and_func_call(self):
        input = """
            void main() {
                a = b + c;
                putStringLn("Hello, World!");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_get_and_print_float(self):
        input = """
            void main() {
                a = b + c;
                getFloat(x);
                putFloatLn(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_print_full_name(self):
        input = """
            string fname, sname, lname;
            void main() {
                putStringLn("Enter your firstname: ");
                getString(fname);
                putStringLn("Enter your lastname: ");
                getString(lname);
                putStringLn("Enter your sur name: ");
                getString(sname);
                putStringLn("Your full name is: ", fname, sname, lname);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_nested_array_assign(self):
        input = """
            void main() {
                a[b[2]] = 10;
                foo();
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_complex_nested_if_else(self):
        input = """
            void main() {
                if (a==b) {
                    if (c==d) {
                        e = f;
                    } else {
                        i = 1;
                    }
                } else {
                    x = 2;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_swap_function(self):
        input = """
            void main () {
                int a[100];
                int i,j,temp;
                for (i = 0; i < n - 2; i=i+1) {
                    for (j = i + 1; j < n - 1; j=j+1) {
                        if (a[i] > a[j]) {
                            temp = a[i];
                            a[i] = a[j];
                            a[j] = temp;
                        }
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_sum_float_array_function(self):
        input = """
            float sum_float_arr(float a[]) {
                int i;
                float s;
                s = 0;
                for (i = n - 1; i >= 0; i=i-1) {
                    s = s + a[i];
                }
                return s;
            }
            void main() {
                float a[100];
                int n;
                putString("Sum of float array: " + sum_float_arr(a));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_enter_data_to_array_function(self):
        input = """
           void input_data_to_array(int a[]) {
               int i,N;
               putStringLn("Number of elements: ");
               getInt(N);
               for(i= 0 ; i < N; i=i+1) {
                   putStringLn("Enter element ",i," : ");
                   putInt(a[i]);
               }
           }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_number_el_5divisible_function(self):
        input = """
           int numbers_of_element_5divisible(int a[], int N) {
                int i, S;
                s = 0;
                for (i=0; i < N; i=i+1) {
                    if(a[i] % 5 == 0) {
                        s = s + a[i];
                    }
                }
                return s;
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_check_prime_function(self):
        input = """
           int prime_number(int N) {
               int i;
               for (i = 2; i < N-1; i=i+1) {
                   if (N % i == 0) {
                       return 0;
                   } else {
                       return 1;
                   }
               }
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_count_x_el_function(self):
        input = """
           int count_X_element(int a[], int X) {
               int i, count;
               count = 0;
               for (i = 0; i < N; i=i+1) {
                   if (a[i] == X) {
                       count = count + 1;
                   }
               }
               return count;
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_replace_all_function(self):
        input = """
           void replace_all(int a[], int N, int x, int y) {
               int i;
               for (i = 0; i < N; i=i+1) {
                   if (a[i] == x) {
                       a[i] = y;
                   }
               }
               return count;
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_replace_all_array(self):
        input = """
            void replace_with_sum(int a[], int N, int x, int y) {
                int i, k;
                for(i = 0; i < N; i=i+1) {
                    if ((a[i-1] + a[i]) % 10 == 0) {
                        k = a[i-1] + a[i];
                        a[i-1] = k;
                        a[i] = k;
                    }
                }
           }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_check_symmetric_array(self):
        input = """
            boolean check_symmetric(float a[], int N) {
                boolean flag;
                int i;
                flag = true;
                for (i = 0; i < N; i=i+1) {
                    if (a[i] != a[N-i+1]) {
                        flag = false;
                        return flag;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_check_incremental_array_function(self):
        input = """
            boolean check_incremental_array(float a[], int N) {
                boolean flag;
                int i;
                flag = true;
                for (i = 0; i < N-1; i=i+1) {
                    if (a[i] < a[i-1]) {
                        flag =false;
                    }
                }
                return flag;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_arithmetic_sequence_function(self):
        input = """
            boolean arithmetic_sequence(float a[], int N, int k) {
                boolean flag;
                int i;
                flag = true;
                for (i = 1; i < N-1; i=i+1) {
                    if (a[i] != a[i-1] + k) {
                        flag =false;
                        return flag;
                    }
                }
                return flag;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_assert_el_in_position(self):
        input = """
            void assert_el(float a[], int N, int k, int x) {
                int i;
                for (i = N; i < k + 1; i=i-1) {
                    if (a[i] != a[i-1] + k) {
                        a[i] = a[i-1];
                        a[k] = x;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_gt_function(self):
        input = """
            int gt(int x) {
                if (x == 0) {
                    return 1;
                } else {
                    return x*gt(x-1);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_fibonacci_function(self):
        input = """
            int fibo(int x) {
                int f1, f2;
                if (x<=2) 
                    return 1;
                else 
                    return fibo(x-2) + fibo(x-1);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_everything_ok(self):
        input = """
            boolean ok(int x) {
                int k;
                boolean ok;
                ok = true;
                if (copy(s,i-2*k+1,k) == copy(s,i-k+1,k)) {
                    ok = false;
                    exit();
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_reverse_number(self):
        input = """
            int reverse_number(int n) {
                reverse = 0;
                do {
                    reverse = reverse * 10;
                    reverse = reverse + n%10;
                    n = n/10;
                } while n != 0;
                return reverse;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_gcd(self):
        input = """
            int gcd(int m, int n) {
                if (m==n) 
                    return m;
                else {
                    if (m>n)
                        return gcd(m-n,n);
                    else
                        return gcd(m,n-m);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_cal_radius_circumference_function(self):
        input = """
            void main() {
                float r,s,c,pi;
                pi = 3.14;
                putStringLn("Tool for calculating s and p of circle");
                putStringLn("--------------------------------------");
                putStringLn("Enter radius R: ");
                getFloat(r);
                s = pi * r * r;
                c = 2 * pi * r;
                putStringLn("Area: ",s);
                putStringLn("Circumference: ",c);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_error_geq_exp_stmt(self):
        input = """
            void main() {
                a = b > = c;
            }
        """
        expect = "Error on line 3 col 24: ="
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_solve_first_order_eq(self):
        input = """
            void main() {
                float a,b,x;
                putStringLn("Solve first order function: AX + B = 0");
                putStringLn("--------------------------------------");
                putStringLn("Enter a: ");
                getFloat(a);
                putStringLn("Enter b: ");
                getFloat(b);
                if (a==0)
                    if (b==0)
                        putStringLn("Infinity solutions");
                    else
                        putStringLn("No solutions");
                else
                    putStringLn("Solution: x= ",-b/a);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_many_complex_if_else(self):
        input = """
            float a,b,c,s,p;
            void main() {
                if (a) b = c;
                else if (a) b = c;
                else if (a) b = c;
                else b = c;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_error_paren_placement(self):
        input = """
            (
                int i;
            )()
        """
        expect = "Error on line 2 col 12: ("
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_redundant_paren(self):
        input = """
                int i;
            )()
        """
        expect = "Error on line 3 col 12: )"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_no_cond_for(self):
        input = """
                void main() {
                    for(;;)
                }
        """
        expect = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_missing_semi(self):
        input = """
                void main() {
                    do {
                        a = b + 10;
                    } while x<10
                }
        """
        expect = "Error on line 6 col 16: }"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_no_enclosed_function(self):
        input = """
                int a[1][2];
        """
        expect = "Error on line 2 col 24: ["
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_err_nested_function_decl(self):
        input = """
                void main() {
                    int sum() {
                        
                    }
                }
        """
        expect = "Error on line 3 col 27: ("
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_unclosed_string(self):
        input = """
                void main() {
                    string a;
                    a = "dsadsadsaas;
                }
        """
        expect = "dsadsadsaas;"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_illegal_escape(self):
        input = """
                void main() {
                    string a;
                    a = "dsad\\msadsaas";
                }
        """
        expect = "dsad\\m"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_paren_and_square(self):
        input = """
            void main() {
                a = (a+b)[12];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_many_subtracts(self):
        input = """
            void main() {
                a = ---- ---b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_exp_inside_square(self):
        input = """
            void main() {
                a = x[2+3];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_many_squareB_with_expression(self):
        input = """
            void main() {
                x = f[2+3][5];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_many_less_operator(self):
        input = """
            void main() {
                a = a < b < c;
            }
        """
        expect = "Error on line 3 col 26: <"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_error_char(self):
        input = """
            void main() {
                a = "asd" ? ;
            }
        """
        expect = "?"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_empty_program(self):
        input = """
        """
        expect = "Error on line 2 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_index_expression(self):
        input = """
        void main() {
            foo(2)[3+x] = a[b[2]] +3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_complex_index_expression(self):
        input = """
        void main() {
            a = foo(2,c+d,3/5)[1*3];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_complex_LB_RB_index_expression(self):
        input = """
        void main() {
            a = (a+b)[12];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_many_square_brackets(self):
        input = """
            void main() {
                string a;
                a = b[[[[[[[[[[[[[[-----------]]]]]]]]]]]]]];
            }
        }
        """
        expect = "Error on line 4 col 22: ["
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_right_assoc(self):
        input = """
            void main() {
                a = a -+b;
            }
        }
        """
        expect = "Error on line 3 col 23: +"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_compare_exp_stmt(self):
        input = """
            void main() {
                a = c > d && e >= f || q < d && d <= e ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_eq_noteq_exp_stmt_in_function(self):
        input = """
            void main() {
                e = f == g ||  z != k  ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_many_assign_exp_stmt(self):
        input = """
            void main() {
                a = b = c = e = f;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_nested_exp(self):
        input = """
            void main() {
                x = foo[!(1+a=2)];
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_error_assign(self):
        input = """
            void main() {
                x = ;
        }
        """
        expect = "Error on line 3 col 20: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_error_add(self):
        input = """
            void main() {
                x ++;
        }
        """
        expect = "Error on line 3 col 19: +"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_mass_function(self):
        input = """
            int main()
                {
                    int n;
                    printf("Enter a binary number: ");
                    scanf("%lld", n);
                    printf("%lld in binary = %d in decimal", n, convertBinaryToDecimal(n));
                    return 0;
                }
                int convertBinaryToDecimal(int n)
                {
                    int decimalNumber,i, remainder;
                    i = 0;
                    decimalNumber = 0;
                    do 
                    {
                        remainder = n%10;
                        n = n / 10;
                        decimalNumber =decimalNumber+ remainder*pow(2,i);
                        i=i+1;
                    } while (n!=0);
                    return decimalNumber;
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))
