from __future__ import annotations
from opcodes import *
from cas_types import *


class Nil:
    pass


class Value:
    def __init__(self, type_ptr: AbstractType, value_part):
        self.m_type_ptr = type_ptr
        self.m_value = value_part

    def type_ptr(self) -> AbstractType:
        return self.m_type_ptr
    
    def type_kind(self) -> TypeKind:
        return self.type_ptr().kind()
    
    def is_nil(self) -> bool:
        return self.type_ptr().is_a(TypeKind.NIL)

    def is_bool(self) -> bool:
        return self.type_ptr().is_a(TypeKind.BOOL)
    
    def is_int(self) -> bool:
        return self.type_ptr().is_a(TypeKind.INT)
    
    def is_real(self) -> bool:
        return self.type_ptr().is_a(TypeKind.REAL)
    
    def is_function(self) -> bool:
        return self.type_ptr().is_a(TypeKind.FUNCTION)
    
    def is_string(self) -> bool:
        return self.type_ptr().is_a(TypeKind.STRING)
    
    def is_struct(self) -> bool:
        return self.type_ptr().is_a(TypeKind.STRUCT)


def as_nil(value: Value) -> int:
    return Nil()

def as_bool(value: Value) -> int:
    return bool(value.m_value)

def as_int(value: Value) -> int:
    return int(value.m_value)

def as_real(value: Value) -> float:
    return float(value.m_value)

def as_object(value: Value) -> GCObject:
    return value.m_value





# TODO: 
# as_string
# as_function
# as_struct

def as_string(value: Value) -> str:
    return value.m_value

# as GCObject?
def as_function(value: Value) -> CompiledFunction:
    return value.m_value





def make_nil_value() -> Value:
    global type_table
    type_ptr = type_table.get_nil_ptr()
    return Value(type_ptr, Nil())

def make_bool_value(val: bool) -> Value:
    global type_table
    type_ptr = type_table.get_bool_ptr()
    return Value(type_ptr, val)

def make_int_value(val: int) -> Value:
    global type_table
    type_ptr = type_table.get_int_ptr()
    return Value(type_ptr, val)

def make_real_value(val: float) -> Value:
    global type_table
    type_ptr = type_table.get_real_ptr()
    return Value(type_ptr, val)


# TODO: does this even make sense?
# how to track string objects in the gc?
def make_string_value(val: str) -> Value:
    global type_table
    type_ptr = type_table.get_string_ptr()
    return Value(type_ptr, val)

def make_function_value(fcn: CompiledFunction) -> Value:
    type_ptr = fcn.function_type()
    v        = Value(type_ptr, fcn)
    return v

# TODO: make_struct_value







def print_value(value: Value) -> None:
    match value.type_kind():
        case TypeKind.NIL:
            print("nil")

        case TypeKind.BOOL:
            b = as_bool(value)
            print(f"{b}")

        case TypeKind.INT:
            b = as_int(value)
            print(f"{b}")

        case TypeKind.REAL:
            b = as_real(value)
            print(f"{b}")

        case TypeKind.STRING:
            # TODO: 
            b = as_object(value)
            print(f"{b}")

        case TypeKind.FUNCTION:
            # TODO: 
            b = as_object(value)
            print(f"{b}")

        case TypeKind.STRUCT:
            # TODO: 
            b = as_object(value)
            print(f"{b}")

        case _:
            raise Exception("implementation error")




class GCObject:
    def __init__(self):
        self.m_next_obj: GCObject = None
        self.m_is_marked = False


class CompiledFunction(GCObject):
    def __init__(self, name: str, n_arguments: int, function_type: FunctionType):
        self.m_name        = name
        self.m_opcodes     = list() # list[OpCode]
        self.m_n_arguments = n_arguments
        self.m_function_type = function_type
        self.m_contants = list() # list[Value]
    
    def function_type(self) -> FunctionType:
        return self.m_function_type

    def opcode_at(self, idx: int) -> OpCode:
        return self.m_opcodes[idx]

    def opcodes(self) -> list[OpCode]:
        return self.m_opcodes
    
    def append_opcode(self, opcode: OpCode) -> None:
        return self.m_opcodes.append(opcode)

    def n_arguments(self) -> int:
        return self.m_n_arguments

    def constant_at(self, idx: int) -> Value:
        return self.m_contants[idx]

    def append_constant(self, value: Value) -> None:
        self.m_contants.append(value)
    




# TODO implement it correctly

class GarbageCollector:
    def __init__(self):
        self.m_next_object: GCObject = None

    # def allocate(self, ?)






