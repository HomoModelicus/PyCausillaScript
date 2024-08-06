from __future__ import annotations
from enum import Enum, IntEnum, auto

class TokenKind (Enum):
    # numbers
    NUM_INT     = auto() # 10
    NUM_REAL    = auto()  # 3.14
    
    # string
    STRING      = auto()  # ""

    # identifyer
    IDENTIFYER  = auto() # e.g. name
    
    # operators
    PLUS        = auto() # +
    MINUS       = auto() # -
    PROD        = auto() # *
    DIVIDE      = auto() # /
    POWER       = auto() # ^
    COLON       = auto() # :
    ARROW       = auto() # ->
    SEMICOLON   = auto() # ;
    COMMA       = auto() # ,
    EQUAL       = auto() # =
    DOT         = auto() # .

    AND         = auto() # &
    OR          = auto() # |
    NOT         = auto() # !

    EQUALEQUAL  = auto() # ==
    NOTEQUAL    = auto() # != 
    LESS        = auto() # <
    GREATER     = auto() # >
    LESSTHAN    = auto() # <=
    GREATERTHAN = auto() # >=

    LPAREN      = auto() # (
    RPAREN      = auto() # )
    LBRACKET    = auto() # [
    RBRACKET    = auto() # ]
    LBRACE      = auto() # {
    RBRACE      = auto() # }

    # keywords
    VAR         = auto() # var
    FUNCTION    = auto() # function
    STRUCT      = auto() # struct

    # MAIN        = auto() # main
    
    RETURN      = auto() # return

    IF          = auto() # if
    ELSE        = auto() # else
    FOR         = auto() # for
    WHILE       = auto() # while
    END         = auto() # end
    BREAK       = auto() # break
    CONTINUE    = auto() # continue

    NIL         = auto() # nil   
    TRUE        = auto() # true
    FALSE       = auto() # false
    PI          = auto() # pi

    
    
    # builtins
    TYPE_NIL        = auto()  # Nil
    TYPE_BOOL       = auto()  # Bool
    TYPE_INT        = auto()  # Int
    TYPE_REAL       = auto()  # Real
    TYPE_STRING     = auto()  # String
    TYPE_FUNCTION   = auto()  # Function
    
    FCN_PRINT   = auto() # print
    FCN_ABS     = auto() # abs
    FCN_SQRT    = auto() # sqrt
    FCN_SIN     = auto() # sin
    FCN_COS     = auto() # cos
    FCN_TAN     = auto() # tan
    FCN_ASIN    = auto() # asin
    FCN_ACOS    = auto() # acos
    FCN_ATAN    = auto() # atan
    FCN_LOG     = auto() # log
    FCN_LOG10   = auto() # log10
    FCN_LOG2    = auto() # log2
    FCN_EXP     = auto() # exp
    FCN_MOD     = auto() # mod







class Token:

    def __init__(self: Token, kind: TokenKind, value, line: int):
        self.m_kind  = kind
        self.m_value = value
        self.m_line  = line

    def kind(self: Token) -> TokenKind: 
        return self.m_kind
    
    def is_a(self: Token, kind: TokenKind) -> bool:
        return self.kind() == kind

    def line(self) -> int:
        return self.m_line
    
    def value(self):
        return self.m_value

    def __repr__(self) -> str:
        s = f"Token({self.m_kind.name}, {self.m_value}, {self.m_line})"
        return s





class Lexer:

    @staticmethod
    def create_kw_builtin_dict() -> dict:
        d = dict()

        # keywords
        d["var"]      = TokenKind.VAR
        d["function"] = TokenKind.FUNCTION
        d["struct"]   = TokenKind.STRUCT
        d["return"]   = TokenKind.RETURN   
        # d["main"]     = TokenKind.MAIN     
        d["nil"]      = TokenKind.NIL      
          
        d["if"]       = TokenKind.IF
        d["else"]     = TokenKind.ELSE
        
        d["for"]      = TokenKind.FOR
        d["while"]    = TokenKind.WHILE
        d["break"]    = TokenKind.BREAK
        d["continue"] = TokenKind.CONTINUE
        d["end"]      = TokenKind.END
        d["true"]     = TokenKind.TRUE
        d["false"]    = TokenKind.FALSE
        d["pi"]       = TokenKind.PI
        
        # builtins
        d["Nil"]    = TokenKind.TYPE_NIL
        d["Bool"]   = TokenKind.TYPE_BOOL
        d["Int"]    = TokenKind.TYPE_INT
        d["Real"]   = TokenKind.TYPE_REAL
        d["String"] = TokenKind.TYPE_STRING
        d["Function"] = TokenKind.TYPE_FUNCTION

        d["print"]  = TokenKind.FCN_PRINT

        return d

    def __init__(self: Lexer, text: str) -> None:
        self.m_text = text
        self.m_token_list: list[Token] = list()
        self.m_kw_dict = Lexer.create_kw_builtin_dict()

    def token_list(self) -> list[Token]:
        return self.m_token_list

    def handle_number(self: Lexer, start_idx: int, linenr: int) -> int:
        idx = start_idx
        while (self.m_text[idx].isdigit() 
               or self.m_text[idx] == "+"
               or self.m_text[idx] == "-"
               or self.m_text[idx] == "e"
               or self.m_text[idx] == "."
               ): # probably a number
            idx += 1
        num_str = self.m_text[start_idx:idx]
        num     = float(num_str) # this fails if the number is not a number
        num_int = int(num)

        if num == num_int:
            idx = num_str.find(".")
            if idx < 0:
                tok = Token(TokenKind.NUM_INT, num_int, linenr)
            else:
                tok = Token(TokenKind.NUM_REAL, num, linenr)
        else:
            tok = Token(TokenKind.NUM_REAL, num, linenr)
        self.m_token_list.append(tok)
        return idx
    
    def handle_string(self: Lexer, start_idx: int, linenr: int) -> int:
        n_words = len(self.m_text)
        idx = start_idx+1
        while idx < n_words and not (self.m_text[idx] == '"' and self.m_text[idx-1] != "\\"):
            idx += 1
        if idx >= n_words:
            raise Exception(f"not closed string encountered at line: {linenr}")
        
        s = self.m_text[start_idx:idx]
        tok = Token(TokenKind.STRING, s, linenr)
        self.m_token_list.append(tok)
        return idx+1

    def handle_identifyer_keywords_builtins(self: Lexer, start_idx: int, linenr: int) -> int:
        idx = start_idx

        # firstchar
        if (self.m_text[idx] == "_" or self.m_text[idx].isalpha()):
            idx += 1
        
        # remchar
        while (self.m_text[idx] == "_" or self.m_text[idx].isalnum()):
            idx += 1
    
        possible_iden = self.m_text[start_idx:idx]

        if possible_iden in self.m_kw_dict:
            kind = self.m_kw_dict[possible_iden]
            value = 0
        else:
            kind = TokenKind.IDENTIFYER
            value = possible_iden
        
        tok = Token(kind, value, linenr)
        self.m_token_list.append(tok)
        return idx
    

    def process(self: Lexer) -> list[Token]:
        n_chars: int = len(self.m_text)
        idx: int     = 0
        linenr: int  = 0

        while idx < n_chars:
            
            match self.m_text[idx]:
                case " ":
                    idx += 1
                    continue

                case "\t":
                    idx += 1
                    continue

                case "\n":
                    linenr += 1
                    idx += 1
                    continue

                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    next_idx = self.handle_number(idx, linenr)
                    idx = next_idx
                    continue

                case '"':
                    next_idx = self.handle_string(idx, linenr)
                    idx = next_idx
                    continue
                
                # operators:
                case "+":
                    next_token = Token(TokenKind.PLUS, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "-":
                    if self.m_text[idx+1] == ">":
                        next_token = Token(TokenKind.ARROW, 0, linenr)
                        idx += 2
                    else:
                        next_token = Token(TokenKind.MINUS, 0, linenr)
                        idx += 1
                    self.m_token_list.append(next_token)
                    continue

                case "*":
                    next_token = Token(TokenKind.PROD, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "/":
                    # handle comments
                    if self.m_text[idx+1] == "/":
                        # handle line comment, go to the end of the line
                        idx += 2 # eat //
                        while idx < n_chars and self.m_text[idx] != '\n':
                            idx += 1
                        idx += 1 # eat newline too
                        continue

                    elif self.m_text[idx+1] == "*":
                        # handle block comment
                        start_idx = idx
                        start_linenr = linenr
                        idx += 2 # eat /*
                        while self.m_text[idx] != '*' and self.m_text[idx+1] != '/':
                            if self.m_text[idx] == '\n':
                                linenr += 1
                            idx += 1
                        idx += 2 # eat */
                        if idx > n_chars:
                            raise Exception(f"block comment was not closed at line: {start_linenr}")
                        continue

                    else:
                        next_token = Token(TokenKind.DIVIDE, 0, linenr)
                        self.m_token_list.append(next_token)
                        idx += 1
                        continue

                case "^":
                    next_token = Token(TokenKind.POWER, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case ":":
                    next_token = Token(TokenKind.COLON, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case ";":
                    next_token = Token(TokenKind.SEMICOLON, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case ",":
                    next_token = Token(TokenKind.COMMA, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "=":
                    if self.m_text[idx+1] == "=":
                        next_token = Token(TokenKind.EQUALEQUAL, 0, linenr)
                        idx += 2
                    else:
                        next_token = Token(TokenKind.EQUAL, 0, linenr)
                        idx += 1
                    self.m_token_list.append(next_token)
                    continue

                case '.':
                    next_token = Token(TokenKind.DOT, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "&":
                    next_token = Token(TokenKind.AND, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "|":
                    next_token = Token(TokenKind.OR, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "!":
                    if self.m_text[idx+1] == "=":
                        next_token = Token(TokenKind.NOTEQUAL, 0, linenr)
                        idx += 2
                    else:
                        next_token = Token(TokenKind.NOT, 0, linenr)
                        idx += 1
                    self.m_token_list.append(next_token)
                    continue
                

                case "<":
                    if self.m_text[idx+1] == "=":
                        next_token = Token(TokenKind.LESSTHAN, 0, linenr)
                        idx += 2
                    else:
                        next_token = Token(TokenKind.LESS, 0, linenr)
                        idx += 1
                    self.m_token_list.append(next_token)
                    continue

                case ">":
                    if self.m_text[idx+1] == "=":
                        next_token = Token(TokenKind.GREATERTHAN, 0, linenr)
                        idx += 2
                    else:
                        next_token = Token(TokenKind.GREATER, 0, linenr)
                        idx += 1
                    self.m_token_list.append(next_token)
                    continue
                
                case "(":
                    next_token = Token(TokenKind.LPAREN, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case ")":
                    next_token = Token(TokenKind.RPAREN, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "[":
                    next_token = Token(TokenKind.LBRACKET, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "]":
                    next_token = Token(TokenKind.RBRACKET, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "{":
                    next_token = Token(TokenKind.LBRACE, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case "}":
                    next_token = Token(TokenKind.RBRACE, 0, linenr)
                    self.m_token_list.append(next_token)
                    idx += 1
                    continue

                case _:
                    next_idx = self.handle_identifyer_keywords_builtins(idx, linenr)
                    if next_idx <= idx:
                        raise Exception(f"invalid token encountered: {self.m_text[idx]}")
                    idx = next_idx
                    continue
            # end match
        # end while
        return self.token_list()


