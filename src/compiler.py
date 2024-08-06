
from __future__ import annotations

from parser import *
from symbol_table import *
from objects import *






class FunctionCompiler:
    def __init__(self, enclosing_symbol_table: SymbolTable):
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







