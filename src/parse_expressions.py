# 
# 
# 
# 
# def parse_function_call_expression(token_list: list[Token], first: int):
#     # first pointet to the iden, then (
#     start_line = token_list[first].line()
#     fcn_name = token_list[first]
#     first += 2
# 
#     # comma separated expression list
#     # n_tokens = len(token_list)
#     args = []
#     while True:
#         check_end_of_token_stream(token_list, first, start_line, "a function call argument block")
#         # if first >= n_tokens:
#         #     raise Exception(f"End of token stream reached inside a function call argument block at line: {start_line}")
# 
#         if token_list[first].is_a(TokenKind.RPAREN):
#             break
# 
#         (arg_expr, next_first) = parse_expression(token_list, first)
#         first = next_first
#         args.append(arg_expr)
# 
# 
#     expr = FunctionCallExpression(fcn_name, args)
#     next_first = first + 1
#     return (expr, next_first)
# 
# 
# # TODO
# def parse_term(token_list: list[Token], first: int):
#     act_token = token_list[first]
#     if act_token.is_a(TokenKind.IDENTIFYER):
#         next_token = token_list[first+1]
#         if next_token.is_a(TokenKind.DOT):
#             first += 2
#             (rhs_expr, next_first) = parse_expression(token_list, first)
#             bin_expr = BinaryExpression(act_token, rhs_expr, next_token)
#             return (bin_expr, next_first)
#         else:
#             next_first = first + 1
#             return (LiteralExpression(act_token), next_first)
# 
#     if act_token.is_a(TokenKind.LPAREN):
#         first += 1
#         (expr, next_first) = parse_expression(token_list, first)
#         check_token(token_list, next_first, TokenKind.RPAREN)
#         next_first += 1
#         return (expr, next_first)
# 
#     if act_token.is_a(TokenKind.NUM_INT) or act_token.is_a(TokenKind.NUM_REAL) or act_token.is_a(TokenKind.STRING):
#         next_first = first + 1
#         return (LiteralExpression(act_token), next_first)
#     
#     if is_builtin_variable_kind(act_token):
#         next_first = first + 1
#         return (LiteralExpression(act_token), next_first)
# 
# 
# 
# 
# 
# def parse_expression(token_list: list[Token], first: int):
#     act_token: Token = token_list[first]
#     start_line: int = act_token.line()
# 
#     if is_unary_operator(act_token):
#         # (arg_expr, next_first) = parse_unary_expression(token_list, first)
#         operator_token = act_token
#         (arg_expr, next_first) = parse_expression(token_list, first)
#         return (UnaryExpression(arg_expr, operator_token), next_first)
#     
#     if act_token.is_a(TokenKind.IDENTIFYER):
#         check_end_of_token_stream(token_list, first+1, start_line, "an expression")
# 
#         next_token = token_list[first+1]
#         if next_token.is_a(TokenKind.DOT):
#             (dot_expr, next_first) = parse_expression(token_list, first+2)
#             bin_expr = BinaryExpression(act_token, dot_expr, next_token)
#             return (bin_expr, next_first)
# 
#     if is_function_call(token_list, first):
#         (fcn_call_expr, next_first) = parse_function_call_expression(token_list, first)
#         return (fcn_call_expr, next_first)
#     
# 
#     (term_expr, next_first) = parse_term(token_list, first)
#     first = next_first
#     operator_token = token_list[first]
#     
#     if is_power_binary_operator(operator_token):
#         first += 1
#         (rhs_expr, next_first) = parse_expression(token_list, first)
#         bin_expr = BinaryExpression(term_expr, rhs_expr, operator_token)
#         return (bin_expr, next_first)
#     
#     if is_multdiv_binary_operator(operator_token):
#         first += 1
#         (rhs_expr, next_first) = parse_expression(token_list, first)
#         bin_expr = BinaryExpression(term_expr, rhs_expr, operator_token)
#         return (bin_expr, next_first)
#     
#     if is_addsub_binary_operator(operator_token):
#         first += 1
#         (rhs_expr, next_first) = parse_expression(token_list, first)
#         bin_expr = BinaryExpression(term_expr, rhs_expr, operator_token)
#         return (bin_expr, next_first)
#     
#     if is_comparison_binary_operator(operator_token):
#         first += 1
#         (rhs_expr, next_first) = parse_expression(token_list, first)
#         bin_expr = BinaryExpression(term_expr, rhs_expr, operator_token)
#         return (bin_expr, next_first)
#     
#     if is_logical_binary_operator(operator_token):
#         first += 1
#         (rhs_expr, next_first) = parse_expression(token_list, first)
#         bin_expr = BinaryExpression(term_expr, rhs_expr, operator_token)
#         return (bin_expr, next_first)
#     
#     # else
#     return (term_expr, next_first)





