

# from Lox: https://craftinginterpreters.com/appendix-i.html


# expression     	:= assignment
# assignment     	:=  logic_orand
#                   |   ( call "." )? IDENTIFIER "=" assignment				 	
# logic_orand       := comparison ( ("|" | "&") comparison )*
# comparison       	:= term_addsub ( ( "!=" | "==" | ">" | ">=" | "<" | "<=" ) term_addsub )*
# term_addsub      	:= term_multdiv ( ( "-" | "+" ) term_multdiv )*
# term_multdiv      := term_pow ( ( "/" | "*" ) term_pow )*
# term_pow          := unary ("^" unary)*
# unary          	:= ( "!" | "-" | "+" ) unary | call
# call           	:= primary ( "(" arguments? ")" | "." IDENTIFIER | "[" array_indexing "]" )*
# primary        	:= 	"true"
# 					| 	"false" 
# 					| 	"nil" 
# 					| 	NUMBER 
# 					| 	STRING
# 					| 	IDENTIFIER
# 					| 	"(" expression ")"
#                   |   "[" array_indexing? "]"
# 
# array_indexing := array_element ("," array_element)*
# array_element := logic_orand
#
# 
# ? zero or one
# + one or more
# * zero or more
#
# program := declaration* 
# 
# declaration :=    variable_decl
#               |   function_decl
#               |   struct_decl
#               |   expr_stmt # e.g. print(15);
#
#
#
# variable_decl := "var" iden ":" type = expr_stmt
# function_decl := "function" iden "(" fcn_args* ")" "->" return_type stmt* "end"
# struct_decl   := "struct" iden struct_members? "end"
#
# iden          := first_char rem_char*
# first_char    := "_" | a-z | A-Z
# rem_char      := first_char | 0-9
#
# type          := iden | builtin_type | fcn_type
# builtin_type  := Nil | Bool | Int | Real | String
# fcn_type      := "Function" "{" "(" arg_types? ")" "->" return_type "}"
# return_type   := type
# arg_types     := arg_type ("," arg_type)
# arg_type      := type
#
# fcn_args      := fcn_arg ("," fcn_arg)*
# fcn_arg       := iden ":" type
#
# struct_members := struct_member (";" struct_member)*
# struct_member  := variable_decl
#
# stmt          := if_stmt | while_stmt | break_stmt | continue_stmt | return_stmt | expr_stmt TODO: add for_stmt
# 
# if_stmt       := "if" "(" expr ")" true_branch ("else" false_branch)* "end"
# true_branch   := stmt*
# false_branch  := stmt*
#
# while_stmt    := "while" "(" expr ")" while_body "end"
# while_body    := stmt*
# 
# break_stmt    := "break" ";"
# continue_stmt := "continue" ";"
# return_stmt   := "return" expr ";"
# expr_stmt     := expr ";"
#
# int_number   := digit digit*
# float_number := (int_number "." ( int_number | ("e" ("+" | "-")* int_number))
# digit        := 0-9
# 
# string := " <characters> "
#
#
#
#



