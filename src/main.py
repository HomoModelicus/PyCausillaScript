


# Missing pieces according to reddit:
# https://www.reddit.com/r/ProgrammingLanguages/comments/1arhgie/what_needs_to_be_added_to_loxfrom_crafting/
# The biggest missing piece is support for arrays/lists.
# statically typed lox: https://github.com/DavidTimms/loxdown/tree/master
# 
#
# 
# There are a few things coming in mind:
# 
# The essentials:
# - Collection types such as Array/List(as u/munificent already mentioned), Dictionary/Map, etc.
# - More standard libraries for handling basic types, strings, collections, io, 
# 	and anything that cannot be implemented directly in userland.
# - Module/Namespace support as well as a mechanism to load/include other source files in a lox script.
# 
# Nice to have:
# - A framework for writing standard libraries.
# - Class methods and metaclasses.
# - Anonymous functions/lambdas.
# - For each loop for collection types.
# - Error and/or Exception Handling.
# - String interpolation and UTF-8 string support.
# - Concurrency and parallelism.
# - Optional/gradual types similar to Mypy and RBS.
# 
# These are for the use cases of user land, 
# though as compiler writers there may be a few more things to consider 
# such as VM as non-global variable, 
# adding AST between parser and bytecode generation/emission and further optimizations.




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




from __future__ import annotations

from parser import *
from symbol_table import *
from objects import *
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
        var f0: Int = 1;
        var f1: Int = 1;
        var f:  Int = 1;
        var i:  Int = 1;
        while (i <= n)
            f  = f0 + f1;
            f0 = f1;
            f1 = f;
        end

        return f;
    end

    
    function main() -> Nil
        var n: Int = 10;
        var res: Int = fib(n);
        print(res);

        return nil;
    end
    

"""






def print_tokens(token_list: list[Token]) -> None:
    for token in token_list:
        print(token)
        # print("\n")
    return None

def print_ast_trees(parse_trees: list[AbstractExpression]) -> None:
    for [idx, pt] in enumerate(parse_trees):
        print("=========================================================")
        print(f"the {idx}-th parse tree:")
        pt.print()




class Compiler:
    def __init__(self, enclosing_symbol_table: SymbolTable = None):
        self.m_enclosing_symbol_table = enclosing_symbol_table
        self.m_this_symbol_table = SymbolTable()
    
    def this_symbol_table(self) -> SymbolTable:
        return self.m_this_symbol_table
    
    def compile(self, fcn_ast: FunctionDeclaration) -> CompiledFunction:
        fcn_name: str
        n_arguments: int
        function_type: FunctionType
        compiled_fcn = CompiledFunction(fcn_name, n_arguments, function_type)
        return compiled_fcn




def populate_builtin_symbol_table(symbol_table: SymbolTable) -> None:

    global type_table
    bool_ptr   = type_table.get_bool_ptr()
    int_ptr    = type_table.get_int_ptr()
    real_ptr   = type_table.get_real_ptr()
    string_ptr = type_table.get_string_ptr()

    # there are probably too many such tables?
    # most likely better idea would be to extend the parser + lexer + compiler
    # with such things like inline assembly functions
    # 
    # 
    # or allow implicit upcasting to reduce the number of cases?


    #          Nil | Bool | Int | Real | String
    #        -----------------------------------
    # Nil    |      |
    # Bool   |
    # Int    |
    # Real   |
    # String | 


    # define every builtin here
    # operator+(Int, Int) -> Int
    # operator+(Real, Real) -> Real
    # operator+(Int, Real) -> Real
    # operator+(Real, Int) -> Real
    


    symbol_table.add(
        SymbolTableEntry(
                Token(TokenKind.PLUS, 0, -1),
                "operator+",
                FunctionType([int_ptr, int_ptr], int_ptr),
                depth = -1,
                local_index = -1,
                is_used = True)
    )
    symbol_table.add(
        SymbolTableEntry(
                Token(TokenKind.PLUS, 0, -1),
                "operator+",
                FunctionType([real_ptr, real_ptr], real_ptr),
                depth = -1,
                local_index = -1,
                is_used = True)
    )

    return None




def populate_symbol_table_vardecl(symbol_table: SymbolTable, parse_tree: AbstractStatement) -> None:
    pass

def populate_symbol_table_functiondecl(symbol_table: SymbolTable, parse_tree: AbstractStatement) -> None:
    pass

def populate_symbol_table_structdecl(symbol_table: SymbolTable, parse_tree: AbstractStatement) -> None:
    pass



def populate_symbol_table_all(symbol_table: SymbolTable, parse_trees: list[AbstractStatement]) -> None:
    for [idx, parse_tree] in enumerate(parse_trees):
        if parse_tree.is_variable_decl():
            populate_symbol_table_vardecl(symbol_table, parse_tree)
            continue

        if parse_tree.is_function_decl():
            populate_symbol_table_functiondecl(symbol_table, parse_tree)
            continue

        if parse_tree.is_struct_decl():
            populate_symbol_table_structdecl(symbol_table, parse_tree)
            continue



def compile_all(parse_trees: list[AbstractStatement], builtin_symbol_table):

    # step 1: populate the symbol table with the visible entries
    global_symbol_table = SymbolTable(builtin_symbol_table)
    populate_symbol_table_all(global_symbol_table, parse_trees)
    
    # step 2: type check each vardecl

    # step 3: type check every functiondecl

    # 


        






if __name__ == "__main__":

    lexer       = Lexer(sample_text)
    token_list  = lexer.process()
    parse_trees = parse_program(token_list)
    print_ast_trees(parse_trees)


    builtin_symbol_table = SymbolTable()
    populate_builtin_symbol_table(builtin_symbol_table)

    # no implicit conversion:
    # Real + Int ? shall this be allowed?
    # sin(10) as Int?
    # only upward conversion is allowed?
    # downcasting? Real -> Int? e.g. f(a: Int, b: Real) but is called with f(10.3, 5)

    # define the global builtin symbol table:
    # - contains function declarations, but not the definitions, those are only used for type checking
    # - defines the builtin variables

    # compilation pipeline:
    # for each outer level declarations:
    #   - create an entry in the program global symbol table, but it doesnt start compiling those ast-s
    #   - if every decl-s are done, we shall start with the struct decl-s
    #   - then with the function decl-s
    #   - then the var decls
    # 
    # what to do with a var decl?
    #   - every rhs side symbol and operator shall be known (== there is an entry in the symbol table)
    #       if some of this search fails, it is a compilation error
    #   - each of these rhs expression can be typechecked == evaluated for each subexpression what the resulting type is
    #   - it can be checked, whether the rhs and lhs are compatible with each other
    #       at this stage, type conversion operators could be applied to the ast inside the compiler
    #   - ? no implicit conversion: if the lhs and rhs types are not exactly the same, that's an error
    #
    # what to do with struct decl? TODO: this point is not understood well enough
    #   - struct decl contains only var decls inside
    #       struct Point
    #           var x : Real = 0.0;
    #           var y : Real = 0.0;
    #       end
    #   - such a decl is taken into the symbol table and each sub vardecl is checked as normal vardecl 
    #
    # what to do with function decl?
    #   - 






    # this is already global
    # global type_table
    # type_table = TypeTable()

    
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

    
    # print("vm gets started")
    # print("\n\n")
    # 
    # vm = VirtualMachine()
    # vm.run()
    # 
    # print("vm returned")






