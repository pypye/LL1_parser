from lexical_scanner.lexical_scanner import generate_token
from parser.LL1_Paser import LL1_parser
from ast_print import pretty_print_ast, bracket_print

if __name__ == "__main__":
    file = "in"
    generate_token(file)
    ast = LL1_parser(file)
    ast = pretty_print_ast(file, ast)
    ast = bracket_print(file, ast)
