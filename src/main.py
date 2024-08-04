
from __future__ import annotations


# from lexer import *
# from cas_types import *

from parser import *
from virtual_machine import *



sample_text2 = """
    
    function factorial_rec(n: Int) -> Int
        if (n <= 1)
            return 1;
        else
            return n * factorial_rec(n - 1);
        end
    end

    /*
    function factorial_iter(n: Int) -> Int
        var f: Int = 1;
        for (var ii: Int in range(2, n))
            f = f * ii;
        end
        return f;
    end
    */
    
    function factorial_iter(n: Int) -> Int
        var f: Int = 1;
        var ii: Int = 2;
        while (ii <= n)
            f = f * ii;
        end
        return f;
    end

"""


sample_text3 = """

    function add(a: Real, b: Real) -> Real
        var c: Real = a + b; // add the arguments
        return c;
    end



    function main() -> Nil

        var first: Real = 11;
        var second: Real = -5;
        var res: Real = add(first, second);

        if (res >= 15)
            print(res);
        end

        var s : String = "this is a string to be printed";

        print(s);

        return nil;
    end
"""


sample_text = """
    // var a: Real = 10;
    // var b: Real = 10 + 20;
    // var c: Real = 10 - 20;
    // var d: Real = 10 * 20;
    // var e: Real = 10 / 20;
    // var f: Real = 10 ^ 2;
    // var a: Real = 10 + 30 * 20 - 15;
    // 10 + 30 * 20 - 15;

    /*
    function add(a: Int, b: Int) -> Int
        var c: Int = a + b;
        return c;
    end
    */
    
    /*
    function add(a: Real, b: Int) -> Real
        var c: Real = a + b;
        return c;
    end
    */

    /*
    function fib(n: Int) -> Int
        if (n <= 1)
            return 1;
        else
            return fib(n-1) + fib(n-2);
        end
    end
    */

    function fib_iter(n: Int) -> Int
        var f : Int = 1;
        var i : Int = 1;
        while (i <= n)
            f = f * i;
        end

        return f;
    end

    /*
    function main() -> Nil
        var n: Int = 10;
        var res: Int = fib(n);

        print(res);

        return nil;
    end
    */

"""



# TODO:
# - implement array literals, parse + classes
# - implement array indexing, parse + classes
# - implement struct-s
# 
# - compiling steps:
#       o type checking on the ast
#       o from ast nodes to CompiledFunction
#
# - virtual machine:
#       o implement if jumping fw_if_false
#       o implement while backwards jumping
#       o implement lamda captures
#
# - implement the starter function, which can handle every errors, not handled in the main()
#



if __name__ == "__main__":

    # this is already global
    # global type_table
    # type_table = TypeTable()

    print("vm gets started")
    print("\n\n")

    vm = VirtualMachine()
    vm.run()

    print("vm returned")


    # lexer = Lexer(sample_text)
    # lexer.process()
    # token_list = lexer.token_list()
    #
    # # print("\r\n")
    # print("\r\n")
    # print("Token list:")
    # for token in token_list:
    #     print(token)
    #     # print("\n")
    #
    # parse_trees = parse_program(token_list)
    # for [idx, pt] in enumerate(parse_trees):
    #     print("=========================================================")
    #     print(f"the {idx}-th parse tree:")
    #     pt.print()


    



    # semantic check
    # type check
    # ?ir with only goto-s and blocks?
    # compiling
    #   - break and continue: probably the stack ptr needs to be moved as well, not only the instr_ptr
    # 
    # vm:
    # - Value representation
    # - CallFrame
    #   o Exception Handling
    # 


    # def split(self: Lexer) -> None:
    #     self.m_words = self.m_text.split(" ")
    # 
    # def remove_comments(self: Lexer) -> None:
    #     # comment_indices = list()
    #     # number_indices = list()
    #     # string_indices = list()
    # 
    #     n_words = len(self.m_words)
    #     idx = 0
    #     n_line = 0
    #     while idx < n_words: # [idx, word] in enumerate(self.m_words):
    #         word = self.m_words[idx]
    #         
    #         while word.startswith("\n"):
    #             word.
    # 
    #         if word.startswith('"'):
    #             first_idx = idx
    #             while idx < n_words and (self.m_words[idx].endswith('"') and not self.m_words[idx].endswith('\"')):
    #                 idx += 1
    #             if idx == n_words:
    #                 raise Exception(f"not closed string encountered at ")
    #             
    #         
    # 
    #         if word.startswith("//") and not in_string:
