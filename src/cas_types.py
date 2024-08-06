
from __future__ import annotations
from enum import Enum, auto, IntEnum
from common_utils import *
from lexer import TokenKind, Token


class TypeKind(Enum):
    NIL      = auto()
    BOOL     = auto()
    INT      = auto()
    REAL     = auto()
    STRING   = auto()
    FUNCTION = auto()
    STRUCT   = auto()




class AbstractType:
    def __init__(self, name: str, is_builtin: bool, type_kind: TypeKind):
        self.m_name = name
        self.m_is_builtin = is_builtin
        self.m_type_kind = type_kind

    def name(self) -> str:
        return self.m_name
    
    def kind(self) -> TypeKind:
        return self.m_type_kind
    
    def is_a(self, kind: TypeKind) -> bool:
        return self.kind() == kind
    
    def is_builtin(self) -> bool:
        return self.m_is_builtin



class NilType(AbstractType):
    def __init__(self):
        super().__init__("Nil", True, TypeKind.NIL)

class BoolType(AbstractType):
    def __init__(self):
        super().__init__("Bool", True, TypeKind.BOOL)

class IntType(AbstractType):
    def __init__(self):
        super().__init__("Int", True, TypeKind.INT)

class RealType(AbstractType):
    def __init__(self):
        super().__init__("Real", True, TypeKind.REAL)

class StringType(AbstractType):
    def __init__(self):
        super().__init__("String", True, TypeKind.STRING)

class FunctionType(AbstractType):
    def __init__(self, arg_type_ptrs: list[AbstractType], return_type_ptr: AbstractType):
        super().__init__("<function>", False, TypeKind.FUNCTION)
        self.m_argument_type_ptrs = arg_type_ptrs
        self.m_return_type_ptr    = return_type_ptr

    def argument_types(self) -> list[AbstractType]:
        return self.m_argument_type_ptrs
    
    def return_type(self) -> AbstractType:
        return self.m_return_type_ptr
    

class StructType(AbstractType):
    def __init__(self, name: str):
        super().__init__(name, False, TypeKind.STRUCT)





class TypeTable:
    # these indices needs to be in the same order as in the ctor defined
    NIL_INDEX    = 0
    BOOL_INDEX   = 1
    INT_INDEX    = 2
    REAL_INDEX   = 3
    STRING_INDEX = 4

    def __init__(self):
        self.m_names     = list() # list[str]
        self.m_tokens    = list() # list[Token]
        self.m_type_ptrs = list() # list[AbstractType]

        self.add("Nil",    Token(TokenKind.TYPE_NIL,    0, -1), NilType())
        self.add("Bool",   Token(TokenKind.TYPE_BOOL,   0, -1), BoolType())
        self.add("Int",    Token(TokenKind.TYPE_INT,    0, -1), IntType())
        self.add("Real",   Token(TokenKind.TYPE_REAL,   0, -1), RealType())
        self.add("String", Token(TokenKind.TYPE_STRING, 0, -1), StringType())

    
    def contains(self, name: str) -> bool:
        idx = linear_search(self.m_names, name)
        return is_valid_index(idx)  

    def add(self, name: str, token: Token, type_ptr: AbstractType) -> None:
        if not self.contains(name):
            self.m_names.append(name)
            self.m_tokens.append(token)
            self.m_type_ptrs.append(type_ptr)

    def lookup_by_name(self, name: str) -> AbstractType:
        idx = linear_search(self.m_names, name)
        if not is_valid_index(idx):
            return None
        else:
            return self.m_type_ptrs[idx]

    def lookup_by_tokenkind(self, token_kind: TokenKind) -> AbstractType:
        idx = find_if(self.m_tokens, lambda token: token.kind() == token_kind )
        if not is_valid_index(idx):
            return None
        else:
            return self.m_type_ptrs[idx]
    
    def get_nil_ptr(self) -> NilType:
        return self.m_type_ptrs[TypeTable.NIL_INDEX]

    def get_bool_ptr(self) -> BoolType:
        return self.m_type_ptrs[TypeTable.BOOL_INDEX]

    def get_int_ptr(self) -> IntType:
        return self.m_type_ptrs[TypeTable.INT_INDEX]

    def get_real_ptr(self) -> RealType:
        return self.m_type_ptrs[TypeTable.REAL_INDEX]

    def get_string_ptr(self) -> StringType:
        return self.m_type_ptrs[TypeTable.STRING_INDEX]
    



# =================================================================================================
# define one global TypeTable object
# =================================================================================================

type_table = TypeTable()



