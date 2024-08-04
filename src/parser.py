
from __future__ import annotations
from enum import Enum, IntEnum, auto
from lexer import *


# =================================================================================================
# Utilities
# =================================================================================================


def str_whitespace(depth: int, ws: str = "    "):
    return ws * depth




def is_builtin_type_kind(token: Token) -> bool:
    k = token.kind()
    return (   k == TokenKind.TYPE_NIL 
            or k == TokenKind.TYPE_BOOL 
            or k == TokenKind.TYPE_INT 
            or k == TokenKind.TYPE_REAL 
            or k == TokenKind.TYPE_STRING
        )

def is_builtin_variable_kind(token: Token) -> bool:
    k = token.kind()
    return (   k == TokenKind.NIL 
            or k == TokenKind.TRUE
            or k == TokenKind.FALSE 
            or k == TokenKind.PI
            or is_builtin_type_kind(token)
        )

def is_builtin_function_kind(token: Token) -> bool:
    k = token.kind()
    return (   k == TokenKind.FCN_PRINT 
            or k == TokenKind.FCN_ABS 
            or k == TokenKind.FCN_SQRT 
            or k == TokenKind.FCN_SIN 
            or k == TokenKind.FCN_COS
            or k == TokenKind.FCN_TAN 
            or k == TokenKind.FCN_ASIN 
            or k == TokenKind.FCN_ACOS
            or k == TokenKind.FCN_ATAN 
            or k == TokenKind.FCN_LOG 
            or k == TokenKind.FCN_LOG10
            or k == TokenKind.FCN_LOG2 
            or k == TokenKind.FCN_EXP 
            or k == TokenKind.FCN_MOD
        )

def list_builtin_types() -> list[TokenKind]:
    return [    TokenKind.TYPE_NIL,
                TokenKind.TYPE_BOOL,
                TokenKind.TYPE_INT,
                TokenKind.TYPE_REAL,
                TokenKind.TYPE_STRING,
                TokenKind.TYPE_FUNCTION]




def is_unary_operator(token: Token) -> bool:
    k = token.kind()
    return (
            k == TokenKind.NOT
        or  k == TokenKind.MINUS
        or  k == TokenKind.PLUS
    )

def is_logical_binary_operator(token: Token) -> bool:
    k = token.kind()
    return (
            k == TokenKind.AND
        or  k == TokenKind.OR
    )

def is_comparison_binary_operator(token: Token) -> bool:
    k = token.kind()
    return (
            k == TokenKind.LESS
        or  k == TokenKind.LESSTHAN
        or  k == TokenKind.GREATER
        or  k == TokenKind.GREATERTHAN
        or  k == TokenKind.EQUALEQUAL
        or  k == TokenKind.NOTEQUAL
    )

def is_power_binary_operator(token: Token) -> bool:
    k = token.kind()
    return (
            k == TokenKind.POWER
    )

def is_multdiv_binary_operator(token: Token) -> bool:
    k = token.kind()
    return (
            k == TokenKind.PROD
        or  k == TokenKind.DIVIDE
    )

def is_addsub_binary_operator(token: Token) -> bool:
    k = token.kind()
    return (
            k == TokenKind.PLUS
        or  k == TokenKind.MINUS
    )


def is_function_name(token: Token) -> bool:
    return (
        token.is_a(TokenKind.IDENTIFYER) 
        or is_builtin_function_kind(token)
        )

def is_function_call(token_list: list[Token], first: int) -> bool:
     return (
        is_function_name(token_list[first]) 
        and token_list[first+1].is_a(TokenKind.LPAREN)
        )




def print_ast(decl) -> None:
    pass


# =================================================================================================
# types
# =================================================================================================


# TODO: 
# - DeclarationKind and StatementKind need to be merged together
# - upload the code into github
# - the decl and stmt-s classes need be merged into one class-hierarchy as well
# - ? concrete class for ExpressionParseResult and StatementParseResult ?



class AbstractTypeDeclaration:
    pass

class BuiltinTypeDeclaration(AbstractTypeDeclaration):
    def __init__(self, token: Token):
        self.m_token = token

    def print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}{self.m_token.value()}")

    def str(self) -> str:
        return self.m_token.kind().name

class UserDefTypeDeclaration(AbstractTypeDeclaration):
    def __init__(self, token: Token):
        self.m_token = token

    def print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}{self.m_token.value()}")
    
    def str(self) -> str:
        return self.m_token.value()
    

class FunctionTypeDeclaration(AbstractTypeDeclaration):
    def __init__(self, fcn_arg_types: list[AbstractTypeDeclaration], return_type: AbstractTypeDeclaration):
        self.m_argument_types = fcn_arg_types
        self.m_return_type    = return_type

    def print(self, depth: int) -> None:
        raise Exception("unimplemented in FunctionTypeDeclaration context")
    
    def str(self) -> str:
        raise Exception("unimplemented in FunctionTypeDeclaration context")
        

class FunctionArgumentDeclaration:
    def __init__(self, iden: Token, arg_type: AbstractTypeDeclaration):
        self.m_iden = iden
        self.m_type = arg_type

    def identifyer(self) -> str:
        return self.m_iden.value()
    
    def argument_type(self) -> AbstractTypeDeclaration:
        return self.m_type
    




class StatementKind(Enum):
    VARIABLE_DECL = auto()
    FUNCTION_DECL = auto()
    STRUCT_DECL = auto()

    EXPRESSION_STATEMENT = auto()
    IF_STATEMENT         = auto()
    WHILE_STATEMENT      = auto()
    BREAK_STATEMENT      = auto()
    CONTINUE_STATEMENT   = auto()
    RETURN_STATEMENT     = auto()



class AbstractStatement:
    def __init__(self, kind: StatementKind):
        self.m_kind = kind


    def statement_kind(self) -> StatementKind:
        return self.m_kind
    
    def is_a(self, kind: StatementKind) -> bool:
        return self.statement_kind() == kind
    
    def is_variable_decl(self) -> bool:
        return self.decl_kind() == StatementKind.VARIABLE_DECL
    
    def is_function_decl(self) -> bool:
        return self.decl_kind() == StatementKind.FUNCTION_DECL
    
    def is_struct_decl(self) -> bool:
        return self.decl_kind() == StatementKind.STRUCT_DECL
    

    def print(self, depth: int = 1) -> None:
        self.do_print(depth)

    def do_print(self, depth: int) -> None:
        raise Exception("unimplemented in a Statement")


class ExpressionStatement(AbstractStatement):
    def __init__(self, expr: AbstractExpression):
        super().__init__(StatementKind.EXPRESSION_STATEMENT)
        self.m_expr = expr

    def do_print(self, depth: int = 1) -> None:
        print(f"{str_whitespace(depth)}expression statement:")
        self.m_expr.print(depth + 1)


class IfStatement(AbstractStatement):
    def __init__(self, cond: AbstractExpression, true_branch: list[AbstractStatement], false_branch: list[AbstractStatement]):
        super().__init__(StatementKind.IF_STATEMENT)
        self.m_cond = cond
        self.m_true_branch = true_branch
        self.m_false_branch = false_branch

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}if statement:")

        print(f"{str_whitespace(depth+1)}condition:")
        self.m_cond.print(depth + 2)

        inner_depth = depth + 2

        print(f"{str_whitespace(depth+1)}true branch:")
        for elem in self.m_true_branch:
            elem.print(inner_depth)
        
        print(f"{str_whitespace(depth+1)}false branch:")
        for elem in self.m_false_branch:
            elem.print(inner_depth)



class WhileStatement(AbstractStatement):
    def __init__(self, cond: AbstractExpression, body: list[AbstractStatement]):
        super().__init__(StatementKind.WHILE_STATEMENT)
        self.m_cond = cond
        self.m_body = body

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}while statement:")

        print(f"{str_whitespace(depth+1)}condition:")
        self.m_cond.print(depth + 2)

        inner_depth = depth + 2

        print(f"{str_whitespace(depth+1)}body:")
        for elem in self.m_body:
            elem.print(inner_depth)
        

class BreakStatement(AbstractStatement):
    def __init__(self, token: Token):
        super().__init__(StatementKind.BREAK_STATEMENT)
        self.m_token = token

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}break statement")

class ContinueStatement(AbstractStatement):
    def __init__(self, token: Token):
        super().__init__(StatementKind.CONTINUE_STATEMENT)
        self.m_token = token
    
    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}continue statement")

class ReturnStatement(AbstractStatement):
    def __init__(self, expr_stmt: ExpressionStatement):
        super().__init__(StatementKind.RETURN_STATEMENT)
        self.m_expr_stmt = expr_stmt

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}return statement")
        self.m_expr_stmt.print(depth + 1)




class VariableDeclaration(AbstractStatement):
    def __init__(
            self: VariableDeclaration,
            iden: Token,
            type: AbstractTypeDeclaration,
            expr_stmt: ExpressionStatement
            ):
        super().__init__(StatementKind.VARIABLE_DECL)
        self.m_iden      = iden
        self.m_type      = type
        self.m_expr_stmt = expr_stmt

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}identifyer: {self.m_iden.value()}")
        print(f"{str_whitespace(depth)}type: {self.m_type.str()}")
        # print(f"{str_whitespace(depth)} expression:")
        self.m_expr_stmt.print(depth)
        print("") # newline
        


class FunctionDeclaration(AbstractStatement):
    def __init__(
            self: FunctionDeclaration, 
            iden: Token, 
            fcn_args: list[FunctionArgumentDeclaration], 
            return_type: AbstractTypeDeclaration, 
            stmt_list: list[AbstractExpression]
            ):
        super().__init__(StatementKind.FUNCTION_DECL)
        self.m_iden         = iden
        self.m_fcn_args     = fcn_args
        self.m_return_type  = return_type
        self.m_stmt_list    = stmt_list

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)} identifyer: {self.m_iden.value()}")
        print(f"{str_whitespace(depth)} type: function decl with n_args: {len(self.m_fcn_args)}")
        
        for [idx, fcn_arg] in enumerate(self.m_fcn_args):
            print(f"{str_whitespace(depth+1)}at {idx}: {fcn_arg.identifyer()} of type {fcn_arg.argument_type().str()}")
        
        print(f"{str_whitespace(depth)}-> with return type: {self.m_return_type.str()}")
        
        depth += 1
        for [idx, stmt] in enumerate(self.m_stmt_list):
            stmt.print(depth)
        
        print("") # newline


        
class StructDeclaration(AbstractStatement):
    def __init__(
            self: StructDeclaration,
            iden: Token,
            struct_members: list[VariableDeclaration]
            ):
        super().__init__(StatementKind.STRUCT_DECL)
        self.m_iden = iden
        self.m_struct_members = struct_members

    def do_print(self, depth: int) -> None:
        raise Exception("unimplemeted in struct decl context")


class PrintExpression(AbstractStatement):
    def __init__(self, expr: AbstractExpression):
        super().__init__(ExpressionKind.PRINT)
        self.m_expr = expr

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}print statement:")
        self.m_expr.print(depth + 1)




class ExpressionKind(Enum):
    UNARY         = auto()
    BINARY        = auto()
    LITERAL       = auto()
    ARRAY_LITERAL = auto()
    VARIABLE      = auto()
    FUNCTIONCALL  = auto()
    PRINT         = auto()



class AbstractExpression:
    def __init__(self, kind: ExpressionKind):
        self.m_kind = kind

    def kind(self) -> ExpressionKind:
        return self.m_kind
    
    def is_a(self, kind: ExpressionKind) -> bool:
        return self.m_kind == kind

    def print(self, depth: int = 1) -> None:
        self.do_print(depth)
        return None
    
    def do_print(self, depth: int) -> None:
        raise Exception("not implemented for some Expression")
    


class UnaryExpression(AbstractExpression):
    def __init__(self, operator_token: Token, arg: AbstractExpression):
        super().__init__(ExpressionKind.UNARY)
        self.m_operator_token = operator_token
        self.m_argument = arg
        
    def argument(self) -> AbstractExpression:
        return self.m_argument
    
    def is_not(self) -> bool:
        return self.m_operator_token.kind() == TokenKind.NOT
    
    def is_plus(self) -> bool:
        return self.m_operator_token.kind() == TokenKind.PLUS
    
    def is_minus(self) -> bool:
        return self.m_operator_token.kind() == TokenKind.MINUS
    
    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}unary expression: {self.m_operator_token.kind()}")
        self.m_argument.do_print(depth + 1)



class BinaryExpression(AbstractExpression):
    def __init__(self, operator_token: Token, lhs_expr: AbstractExpression, rhs_expr: AbstractExpression):
        super().__init__(ExpressionKind.BINARY)
        self.m_operator_token = operator_token
        self.m_lhs = lhs_expr
        self.m_rhs = rhs_expr

    def lhs(self) -> AbstractExpression:
        return self.m_lhs
    
    def rhs(self) -> AbstractExpression:
        return self.m_rhs
    
    def is_assignment(self) -> bool:
        return self.m_operator_token.kind() == TokenKind.EQUAL
    
    def is_and(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.AND
    
    def is_or(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.OR
    
    def is_less(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.LESS
    
    def is_lessthan(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.LESSTHAN
    
    def is_greater(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.GREATER
    
    def is_greaterthan(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.GREATERTHAN
    
    def is_equalequal(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.EQUALEQUAL
    
    def is_notequal(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.NOTEQUAL
    
    def is_minus(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.MINUS
    
    def is_plus(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.PLUS
    
    def is_product(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.PROD
    
    def is_divide(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.DIVIDE
    
    def is_power(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.POWER
    
    def is_dot(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.DOT
    
    def is_indexing(self) -> bool:
            return self.m_operator_token.kind() == TokenKind.LBRACKET
    
    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}binary expression: {self.m_operator_token.kind()}")
        self.m_lhs.do_print(depth + 1)
        self.m_rhs.do_print(depth + 1)


class FunctionCallExpression(AbstractExpression):
    def __init__(self, fcn_name: AbstractExpression, args: list[AbstractExpression]):
        super().__init__(ExpressionKind.FUNCTIONCALL)
        self.m_name = fcn_name
        self.m_arguments = args 

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}function call expression: with n_args: {len(self.m_arguments)}")
        self.m_name.print(depth + 1)
        for arg in self.m_arguments:
            arg.do_print(depth + 1)
        

class LiteralExpression(AbstractExpression):
    def __init__(self, token: Token):
        super().__init__(ExpressionKind.LITERAL)
        self.m_token = token

    def is_true(self) -> bool:
        return self.m_token.kind() == TokenKind.TRUE

    def is_false(self) -> bool:
        return self.m_token.kind() == TokenKind.FALSE

    def is_nil(self) -> bool:
        return self.m_token.kind() == TokenKind.NIL 

    def is_int_number(self) -> bool:
        return self.m_token.kind() == TokenKind.NUM_INT

    def is_real_number(self) -> bool:
        return self.m_token.kind() == TokenKind.NUM_REAL

    def is_string(self) -> bool:
        return self.m_token.kind() == TokenKind.STRING

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}literal expression: {self.m_token.value()}")
    


class VariableExpression(AbstractExpression):
    def __init__(self, varname: Token):
        super().__init__(ExpressionKind.VARIABLE)
        self.m_name = varname

    def do_print(self, depth: int) -> None:
        print(f"{str_whitespace(depth)}variable expression: {self.m_name.value()}")
    

class ArrayLiteralExpression(AbstractExpression):
    def __init__(self, elements: list[AbstractExpression]):
        super().__init__(ExpressionKind.ARRAY_LITERAL)
        self.m_elements = elements

    def do_print(self, depth: int) -> None:
        print(f"ArrayLiteralExpression with n_elements: {len(self.m_elements)}")
        for elem in self.m_elements:
            elem.print(depth + 1)







# =================================================================================================
# parser utilities
# =================================================================================================

def is_any_equal(haystack, test_hay):
    b = False
    ii = 0
    while not b:
        if haystack[ii] == test_hay:
            b = True
            break
    return b


def check_token(token_list: list[Token], first: int, expected_kind: TokenKind) -> None:
    act_token = token_list[first]
    act_kind = act_token.kind()
    linenr = act_token.line()
    if act_kind != expected_kind:
        raise Exception(f"expected token of {expected_kind}, but found: {act_kind} at line: {linenr}")
    return None


def check_any_of_token(token_list: list[Token], first: int, expected_kinds: list[TokenKind]) -> None:
    act_token = token_list[first]
    act_kind = act_token.kind()
    linenr = act_token.line()
    if not is_any_equal(expected_kinds, act_kind):
        str_expected_kinds = list(map( lambda e: e.name, expected_kinds))
        raise Exception(f"expected token of {str_expected_kinds}, but found: {act_kind} at line: {linenr}")
    return None

def check_end_of_token_stream(token_list, first, start_line, context_msg) -> None:
    n_tokens = len(token_list)
    if first >= n_tokens:
            raise Exception(f"End of token stream reached inside {context_msg} at line: {start_line}")
    return None

# def parse_separeted_list(
#         token_list: list[Token],
#         first: int,
#         separator_kind: TokenKind,
#         expected_kinds: list[TokenKind],
#         semantic_op) -> int:
#     
#     start_line = token_list[first].line()
#     # n_tokens = len(token_list)
#     while True:
#         # if first >= n_tokens:
#         #     raise Exception(f"End of token stream reached inside a separated list at line: {token_list[n_tokens-1].line()}")
#         check_end_of_token_stream(token_list, first, start_line, "a separated list")
# 
#         check_any_of_token(token_list, first, expected_kinds)
#         act_token = token_list[first]
#         first     = semantic_op(token_list, first)
#         if token_list[first].is_a(separator_kind):
#             first += 1
#         else:
#             break
#     return first
#         

# =================================================================================================
# parse declarations
# =================================================================================================


# TODO: function type inside the function type is not parsed correctly
def parse_function_type_decl(token_list: list[Token], first: int):
    check_token(token_list, first + 0, TokenKind.TYPE_FUNCTION)
    check_token(token_list, first + 1, TokenKind.LBRACE)
    check_token(token_list, first + 2, TokenKind.LPAREN)
    start_line          = token_list[first].line()
    first              += 3
    builtin_type_list   = list_builtin_types()
    expected_kinds      = [TokenKind.IDENTIFYER].extend(builtin_type_list)
    argument_type_list  = [] # list[AbstractTypeDeclaration]

    while True:
        check_end_of_token_stream(token_list, first, start_line, "a function type decl block")

        if token_list[first].is_a(TokenKind.RPAREN):
            first += 1
            break

        if token_list[first].is_a(TokenKind.COMMA):
            first += 1
        
        check_any_of_token(token_list, first, expected_kinds)
        argument_type_list.append(token_list[first])


    
    check_token(token_list, first, TokenKind.ARROW)
    first += 1
    (return_type_decl, next_first) = parse_type_decl(token_list, first)
    check_token(token_list, next_first + 0, TokenKind.RBRACE)
    first = next_first + 1

    type_decl = FunctionTypeDeclaration(argument_type_list, return_type_decl)

    return (type_decl, first)



def parse_function_arguments_in_decl(token_list: list[Token], first):
    # after the LPAREN
    # shall stop at the RPAREN, thats the next token

    start_line = token_list[first].line()
    # n_tokens = len(token_list)

    fcn_args = []
    while True:

        check_end_of_token_stream(token_list, first, start_line, "a function argument block")

        if token_list[first].is_a(TokenKind.RPAREN):
            first += 1
            break
        
        # iden : type
        check_token(token_list, first + 0, TokenKind.IDENTIFYER)
        check_token(token_list, first + 1, TokenKind.COLON)
        iden = token_list[first]
        first += 2
        (parsed_type, next_first) = parse_type_decl(token_list, first)
        first = next_first
        fcn_arg = FunctionArgumentDeclaration(iden, parsed_type)
        fcn_args.append(fcn_arg)

        if token_list[first].is_a(TokenKind.COMMA):
            first += 1

    next_first = first
    return (fcn_args, next_first)


def parse_type_decl(token_list: list[Token], first: int):
    act_token = token_list[first]
    if is_builtin_type_kind(act_token):
        return (BuiltinTypeDeclaration(act_token), first+1)
    elif act_token.is_a(TokenKind.IDENTIFYER):
        return (UserDefTypeDeclaration(act_token), first+1)
    elif act_token.is_a(TokenKind.TYPE_FUNCTION):
        return parse_function_type_decl(token_list, first)
    else:
        raise Exception(f"expected a valid type expression but got: {act_token.value()} at line: {act_token.line()}")












def parse_variable_declaration(token_list: list[Token], first: int):
    check_token(token_list, first + 0, TokenKind.VAR)
    check_token(token_list, first + 1, TokenKind.IDENTIFYER)
    check_token(token_list, first + 2, TokenKind.COLON)
    
    first                   += 1
    iden_token              = token_list[first]
    first                   += 2
    (type_decl, next_first) = parse_type_decl(token_list, first)
    first                   = next_first
    check_token(token_list, first + 0, TokenKind.EQUAL)
    first += 1
    (expr_stmt, next_first) = parse_expression_statement(token_list, first)
    # check_token(token_list, next_first, TokenKind.SEMICOLON) # already checked in parse_expression_statement 
    # next_first = next_first + 1
    vardecl                 = VariableDeclaration(iden_token, type_decl, expr_stmt)

    return (vardecl, next_first)


def parse_function_declaration(token_list: list[Token], first: int):
    check_token(token_list, first + 0, TokenKind.FUNCTION)
    check_token(token_list, first + 1, TokenKind.IDENTIFYER)
    check_token(token_list, first + 2, TokenKind.LPAREN)

    start_line = token_list[first].line()
    iden: Token = token_list[first+1]
    first += 3

    # : list[FunctionArgumentDeclaration], : int
    (fcn_args, next_first) = parse_function_arguments_in_decl(token_list, first)
    first = next_first
    
    check_token(token_list, first + 0, TokenKind.ARROW)
    first += 1
    (return_type_decl, next_first) = parse_type_decl(token_list, first)
    first = next_first

    stmt_list = [] # :list[AbstractStatement]
    while True:
        check_end_of_token_stream(token_list, first, start_line, "a function declaration")

        (stmt, next_first) = parse_statement(token_list, first)
        first              = next_first
        stmt_list.append(stmt)
       
        if token_list[first].is_a(TokenKind.END):
            first += 1
            break
    
    fcn_decl = FunctionDeclaration(iden, fcn_args, return_type_decl, stmt_list)

    return (fcn_decl, first)




def parse_struct_declaration(token_list: list[Token], first: int):
    start_line = token_list[first].line()
    check_token(token_list, first + 0, TokenKind.STRUCT)
    check_token(token_list, first + 1, TokenKind.IDENTIFYER)
    iden     = token_list[first+1]
    first   += 2
    vardecls = []

    while True:
        check_end_of_token_stream(token_list, first, start_line, "a struct declaration")
 
        if token_list[first].is_a(TokenKind.END):
            first += 1
            break

        (vardecl, next_first) = parse_variable_declaration(token_list, first)
        vardecls.append(vardecl)
        first = next_first

    struct_decl = StructDeclaration(iden, vardecls)
    next_first  = first
    return (struct_decl, next_first)



# =================================================================================================
# parse statements
# =================================================================================================


def parse_if_statement(token_list: list[Token], first: int):
    start_line = token_list[first].line()
    check_token(token_list, first + 0, TokenKind.IF)
    check_token(token_list, first + 1, TokenKind.LPAREN)
    first += 2
    (cond_expr, next_first) = parse_expression(token_list, first)
    check_token(token_list, next_first + 0, TokenKind.RPAREN)
    first = next_first + 1
    
    # parse true branch util either else or end is found
    true_branch       = []
    false_branch      = []
    is_in_true_branch = True

    # n_tokens = len(token_list)
    while True:
        check_end_of_token_stream(token_list, first, start_line, "an if statement")

        act_token = token_list[first]

        if act_token.is_a(TokenKind.END):
            first += 1
            break

        if act_token.is_a(TokenKind.ELSE):
            first += 1
            is_in_true_branch = False
        
        (stmt, next_first) = parse_statement(token_list, first)
        first = next_first

        if is_in_true_branch:
            true_branch.append(stmt)
        else:
            false_branch.append(stmt)

    if_stmt = IfStatement(cond_expr, true_branch, false_branch)
    next_first = first
    return (if_stmt, next_first)



def parse_while_statement(token_list: list[Token], first: int):
    start_line = token_list[first].line()
    check_token(token_list, first + 0, TokenKind.WHILE)
    check_token(token_list, first + 1, TokenKind.LPAREN)
    first += 2
    (cond_expr, next_first) = parse_expression(token_list, first)
    first = next_first
    check_token(token_list, first + 0, TokenKind.RPAREN)
    first += 1

    while_body = [] # list[AbstractStatement]
    while True:
        check_end_of_token_stream(token_list, first, start_line, "a while statement")

        act_token = token_list[first]
        if act_token.is_a(TokenKind.END):
            first += 1
            break

        (stmt, next_first) = parse_statement(token_list, first)
        first              = next_first
        while_body.append(stmt)
        

    while_stmt = WhileStatement(cond_expr, while_body)
    next_first = first
    return (while_stmt, next_first)


def parse_break_statement(token_list: list[Token], first: int):
    check_token(token_list, first + 0, TokenKind.BREAK)
    check_token(token_list, first + 1, TokenKind.SEMICOLON)
    return (BreakStatement(token_list[first], first + 2))


def parse_continue_statement(token_list: list[Token], first: int):
    check_token(token_list, first + 0, TokenKind.CONTINUE)
    check_token(token_list, first + 1, TokenKind.SEMICOLON)
    return (ContinueStatement(token_list[first], first + 2))


def parse_return_statement(token_list: list[Token], first: int):
    check_token(token_list, first, TokenKind.RETURN)
    (expr_stmt, next_first) = parse_expression_statement(token_list, first + 1)
    return (ReturnStatement(expr_stmt), next_first)


def parse_expression_statement(token_list: list[Token], first: int):
    (expr, next_first) = parse_expression(token_list, first)
    check_token(token_list, next_first, TokenKind.SEMICOLON)
    expr_stmt = ExpressionStatement(expr)
    return (expr_stmt, next_first + 1)



def parse_print_statement(token_list, first):
    check_token(token_list, first + 0, TokenKind.FCN_PRINT)
    check_token(token_list, first + 1, TokenKind.LPAREN)
    first += 2
    (expr, next_first) = parse_expression(token_list, first)
    first = next_first
    check_token(token_list, first + 0, TokenKind.RPAREN)
    check_token(token_list, first + 1, TokenKind.SEMICOLON)
    first += 2
    return (PrintExpression(expr), first)


def parse_statement(token_list: list[Token], first: int):

    act_token = token_list[first]
    match act_token.kind():
        case TokenKind.IF:
            return parse_if_statement(token_list, first)
        
        case TokenKind.WHILE:
            return parse_while_statement(token_list, first)
        
        case TokenKind.BREAK:
            return parse_break_statement(token_list, first)
        
        case TokenKind.CONTINUE:
            return parse_continue_statement(token_list, first)
        
        case TokenKind.RETURN:
            return parse_return_statement(token_list, first)
        
        case TokenKind.VAR:
            return parse_variable_declaration(token_list, first)
        
        case TokenKind.FCN_PRINT:
            return parse_print_statement(token_list, first)

        case _:
            return parse_expression_statement(token_list, first)


# =================================================================================================
# parse expressions
# =================================================================================================


def parse_expression(token_list: list[Token], first: int):
    (expr, next_first) = parse_assignment(token_list, first)
    return (expr, next_first)


def parse_assignment(token_list: list[Token], first: int):
    (lhs_expr, next_first) = parse_logic_andor(token_list, first)
    first                  = next_first
    op_token               = token_list[first]
    if op_token.is_a(TokenKind.EQUAL):
        first += 1
        (rhs_expr, next_first) = parse_logic_andor(token_list, first)
        first                  = next_first
        assign_expr            = BinaryExpression(op_token, lhs_expr, rhs_expr)
        return (assign_expr, first)
    else:
        return (lhs_expr, first)


def parse_logic_andor(token_list: list[Token], first: int):
    start_line             = token_list[first].line()
    (lhs_expr, next_first) = parse_comparison(token_list, first)
    first                  = next_first
    
    while True:
        check_end_of_token_stream(token_list, first, start_line, "a math expression")

        op_token = token_list[first]
        if (
                op_token.is_a(TokenKind.AND)
            or  op_token.is_a(TokenKind.OR)
            ):
            first                 += 1
            (rhs_expr, next_first) = parse_comparison(token_list, first)
            first                  = next_first
            expr                   = BinaryExpression(op_token, lhs_expr, rhs_expr)
            lhs_expr               = expr
            
        else:
            return (lhs_expr, first)



def parse_comparison(token_list: list[Token], first: int):
    start_line             = token_list[first].line()
    (lhs_expr, next_first) = parse_term_addsub(token_list, first)
    first                  = next_first
    
    while True:
        check_end_of_token_stream(token_list, first, start_line, "a math expression")

        op_token = token_list[first]
        if (
            # "!=" | "==" | ">" | ">=" | "<" | "<="
                op_token.is_a(TokenKind.NOTEQUAL)
            or  op_token.is_a(TokenKind.EQUALEQUAL)
            or  op_token.is_a(TokenKind.LESS)
            or  op_token.is_a(TokenKind.LESSTHAN)
            or  op_token.is_a(TokenKind.GREATER)
            or  op_token.is_a(TokenKind.GREATERTHAN)
            ):
            first                 += 1
            (rhs_expr, next_first) = parse_term_addsub(token_list, first)
            first                  = next_first
            expr                   = BinaryExpression(op_token, lhs_expr, rhs_expr)
            lhs_expr               = expr
            
        else:
            return (lhs_expr, first)



def parse_term_addsub(token_list: list[Token], first: int):
    start_line             = token_list[first].line()
    (lhs_expr, next_first) = parse_term_multdiv(token_list, first)
    first                  = next_first
    
    while True:
        check_end_of_token_stream(token_list, first, start_line, "a math expression")

        op_token = token_list[first]
        if (
                op_token.is_a(TokenKind.PLUS)
            or  op_token.is_a(TokenKind.MINUS)
            ):
            first                 += 1
            (rhs_expr, next_first) = parse_term_multdiv(token_list, first)
            first                  = next_first
            expr                   = BinaryExpression(op_token, lhs_expr, rhs_expr)
            lhs_expr               = expr
            
        else:
            return (lhs_expr, first)


def parse_term_multdiv(token_list: list[Token], first: int):
    start_line             = token_list[first].line()
    (lhs_expr, next_first) = parse_term_power(token_list, first)
    first                  = next_first
    
    while True:
        check_end_of_token_stream(token_list, first, start_line, "a math expression")

        op_token = token_list[first]
        if (
                op_token.is_a(TokenKind.PROD)
            or  op_token.is_a(TokenKind.DIVIDE)
            ):
            first                 += 1
            (rhs_expr, next_first) = parse_term_power(token_list, first)
            first                  = next_first
            expr                   = BinaryExpression(op_token, lhs_expr, rhs_expr)
            lhs_expr               = expr
            
        else:
            return (lhs_expr, first)


def parse_term_power(token_list: list[Token], first: int):
    (lhs_expr, next_first) = parse_unary(token_list, first)
    first                  = next_first
    op_token               = token_list[first]
    if op_token.is_a(TokenKind.POWER):
        first += 1
        (rhs_expr, next_first) = parse_unary(token_list, first)
        first                  = next_first
        expr                   = BinaryExpression(op_token, lhs_expr, rhs_expr)
        return (expr, first)
    else:
        return (lhs_expr, first)


def parse_unary(token_list: list[Token], first: int):
    act_token: Token = token_list[first]
    if (   act_token.is_a(TokenKind.NOT) 
        or act_token.is_a(TokenKind.MINUS)
        or act_token.is_a(TokenKind.PLUS)
        ):
        op_token           = act_token
        first             += 1
        (expr, next_first) = parse_unary(token_list, first)
        first              = next_first
        unary_expr         = UnaryExpression(op_token, expr)
        return (unary_expr, first)
    
    return parse_call(token_list, first)


def parse_call(token_list: list[Token], first: int):
    act_token     = token_list[first]
    start_line    = act_token.line()
    (expr, first) = parse_primary(token_list, first)

    while True:
        # this cannot be the end of the token stream
        check_end_of_token_stream(token_list, first, start_line, "a function call expression")
        act_token: Token = token_list[first]

        if act_token.is_a(TokenKind.LPAREN):
            first                     += 1
            (fcn_arg_expr, next_first) = parse_function_call_arguments(token_list, first)
            first                      = next_first
            fcn_call_expr              = FunctionCallExpression(expr, fcn_arg_expr)
            expr                       = fcn_call_expr
            continue

        if act_token.is_a(TokenKind.DOT):
            first   += 1
            op_token = act_token
            lhs_expr = expr
            
            check_token(token_list, first, TokenKind.IDENTIFYER)
            act_token = token_list[first]
            rhs_expr  = VariableExpression(act_token)
            expr      = BinaryExpression(op_token, lhs_expr, rhs_expr)
            first    += 1
            continue

        if act_token.is_a(TokenKind.LBRACKET):
            first                            += 1
            op_token                          = act_token
            (array_indexing_expr, next_first) = parse_array_indexing(token_list, first)
            lhs_expr                          = expr
            array_indexing_expr               = BinaryExpression(op_token, lhs_expr, array_indexing_expr)
            expr                              = array_indexing_expr
            continue

        # else
        break

    return (expr, first)


def parse_function_call_arguments(token_list: list[Token], first: int):
    # this eats the closing ) as well and points to the next token at return
    # prev token was (
    start_line = token_list[first].line()
    expr = [] # list[AbstractExpression]
    while True:
        # this cannot be the end of the token stream
        check_end_of_token_stream(token_list, first, start_line, "a function call expression")
        act_token: Token = token_list[first]
        
        if act_token.is_a(TokenKind.RPAREN):
            first += 1
            break

        (args_expr, first) = parse_expression(token_list, first)
        expr.append(args_expr)

        # this would also eat a trailing comma
        # TODO: how to avoid the trailing comma
        # it is not that bad, trailing comma can be really helpful
        act_token = token_list[first]
        if act_token.is_a(TokenKind.COMMA):
            first += 1

    return (expr, first)


def parse_array_indexing(token_list: list[Token], first: int):
    # this eats the closing ] as well and points to the next token at return
    start_line = token_list[first].line()
    expr = [] # list[AbstractExpression]
    while True:
        # this cannot be the end of the token stream
        check_end_of_token_stream(token_list, first, start_line, "an array literal or indexing expression")
        act_token: Token = token_list[first]
        
        if act_token.is_a(TokenKind.RBRACKET):
            first += 1
            break

        (args_expr, first) = parse_expression(token_list, first)
        expr.append(args_expr)

        # this would also eat a trailing comma
        # TODO: how to avoid the trailing comma
        # it is not that bad, trailing comma can be really helpful
        act_token = token_list[first]
        if act_token.is_a(TokenKind.COMMA):
            first += 1

    return (expr, first)



def parse_primary(token_list: list[Token], first: int):
    act_token = token_list[first]
    kind = act_token.kind()

    match kind:
        case TokenKind.TRUE:
            return (LiteralExpression(act_token), first+1)
        
        case TokenKind.FALSE:
            return (LiteralExpression(act_token), first+1)
        
        case TokenKind.NIL:
            return (LiteralExpression(act_token), first+1)
        
        case TokenKind.NUM_INT:
            return (LiteralExpression(act_token), first+1)
        
        case TokenKind.NUM_REAL:
            return (LiteralExpression(act_token), first+1)
        
        case TokenKind.STRING:
            return (LiteralExpression(act_token), first+1)
        
        case TokenKind.IDENTIFYER:
            return (VariableExpression(act_token), first+1)
        
        # case TokenKind.FCN_PRINT:
        #     first             += 1
        #     (expr, next_first) = parse_expression(token_list, first)
        #     first              = next_first
        #     return (PrintExpression(expr), first)
        
        case TokenKind.LPAREN:
            (expr, next_first) = parse_expression(token_list, first)
            return (expr, next_first)




# =================================================================================================
# parse whole program
# =================================================================================================



def parse_program(token_list: list[Token]):
    n_tokens = len(token_list)
    first = 0
    trees = [] # list[AbstractDeclaration]
    while first < n_tokens:
        act_token = token_list[first]

        match act_token.kind():
            case TokenKind.VAR:
                (parse_tree, next_first) = parse_variable_declaration(token_list, first)
                trees.append(parse_tree)
                first = next_first
                continue
            
            case TokenKind.FUNCTION:
                (parse_tree, next_first) = parse_function_declaration(token_list, first)
                trees.append(parse_tree)
                first = next_first
                continue
            
            case TokenKind.STRUCT:
                (parse_tree, next_first) = parse_struct_declaration(token_list, first)
                trees.append(parse_tree)
                first = next_first
                continue
            
            case TokenKind.FCN_PRINT:
                (parse_tree, next_first) = parse_print_statement(token_list, first)
                trees.append(parse_tree)
                first = next_first
                continue

            case _:
                (parse_tree, next_first) = parse_expression_statement(token_list, first)
                trees.append(parse_tree)
                first = next_first
                continue
    
    return trees




