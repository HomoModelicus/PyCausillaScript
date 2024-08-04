
from __future__ import annotations
from enum import Enum, IntEnum, auto




class OpCode(IntEnum):
    PLUS_F64        = auto()
    MINUS_F64       = auto()
    PROD_F64        = auto()
    DIVIDE_F64      = auto()
    POWER_F64       = auto()

    LESS_F64        = auto()
    LESSTHEN_F64    = auto()
    GREATER_F64     = auto()
    GREATERTHEN_F64 = auto()
    EQUALEQUAL_F64  = auto()
    NOTEQUAL_F64    = auto()
    
    PLUS_I64        = auto()
    MINUS_I64       = auto()
    PROD_I64        = auto()
    DIVIDE_I64      = auto()
    POWER_I64       = auto()

    LESS_I64        = auto()
    LESSTHEN_I64    = auto()
    GREATER_I64     = auto()
    GREATERTHEN_I64 = auto()
    EQUALEQUAL_I64  = auto()
    NOTEQUAL_I64    = auto()
    
    JUMP_FW          = auto()
    JUMP_BW          = auto()
    JUMP_FW_IF_FALSE = auto()

    CALL            = auto()
    RETURN          = auto()

    # constant values start at index 0
    GET_CONSTANT    = auto()

    # local variables start at index 1
    # at index 0 is the function object
    GET_LOCAL       = auto()
    SET_LOCAL       = auto()
    
    PUSH_NIL        = auto()
    PUSH_TRUE       = auto()
    PUSH_FALSE      = auto()

    POP             = auto()
    # POPN            = auto()
    
    PRINT           = auto()

    # try, catch










