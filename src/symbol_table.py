
from __future__ import annotations
from typing import *

from common_utils import *
from cas_types import *
from lexer import TokenKind, Token


class SymbolTableEntry:
    def __init__(
            self,
            token: Token,
            name: str,
            type_ptr: AbstractType = None,
            depth: int = -1,
            local_index: int = -1,
            is_used: bool = False,
            ):
        self.m_token        = token
        self.m_name         = name
        self.m_type_ptr     = type_ptr
        self.m_depth        = depth
        self.m_local_index  = local_index
        self.m_is_used      = is_used
        

    def has_name(self, name: str) -> bool:
        return self.m_name == name

    def token(self) -> Token:
        return self.m_token
    
    def name(self) -> str:
        return self.m_name
    
    def type_ptr(self) -> AbstractType:
        return self.m_type_ptr
    
    def depth(self) -> int:
        return self.m_depth
    
    def local_index(self) -> int:
        return self.m_local_index
    
    def is_used(self) -> bool:
        return self.m_is_used



class SymbolLookupResult:
    def __init__(self, entry: SymbolTableEntry, found: bool, is_in_same_table: bool):
        self.entry            = entry
        self.found            = found
        self.is_in_same_table = is_in_same_table
        


def lookup_recursive(symbol_table: Union[SymbolTable, None], name: str) -> SymbolLookupResult:
    found            = False
    is_in_same_table = False
    is_first         = True

    while symbol_table is not None:
        entry = symbol_table.lookup(name)
        if entry is not None:
            found = True
            if is_first:
                is_in_same_table = True
            
            return SymbolLookupResult(entry, found, is_in_same_table)
        else:
            is_first = False
            symbol_table = symbol_table.enclosing()

    return SymbolLookupResult(entry, found, is_in_same_table)



class SymbolTable:
    def __init__(self, enclosing_symbol_table: SymbolTable = None):
        self.m_entries = list() # list[SymbolTableEntry]
        self.m_enclosing_symbol_table = enclosing_symbol_table

    def enclosing(self) -> SymbolTable:
        return self.m_enclosing_symbol_table

    def add(self, next_entry: SymbolTableEntry) -> None:
        self.m_entries.append(next_entry)

    def lookup(self, name: str) -> SymbolTableEntry: # ptr
        idx = find_if(self.m_entries, lambda elem: elem.has_name(name))
        if not is_valid_index(idx):
            return None
        else:
            return self.m_entries[idx]











