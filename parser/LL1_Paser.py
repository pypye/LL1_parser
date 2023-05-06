from PaserReader import parserReader
from Select import build_parsing_table
from ScannerReader import read

grammar = parserReader('./parser/vc_grammar/VCGrammar.json')
parsing_table = build_parsing_table(grammar)

class AST:
    def __init__(self):
        self.tab = 0
        self.count_tab = {0: 2}
        self.ast = []

    def add_node(self, token):
        self.ast.append((self.tab, token))
        
    def remove_tab(self):
        self.count_tab[self.tab] -= 1
        if self.count_tab[self.tab] == 0:
            self.tab -= 1
        
    def add_tab(self):
        self.tab += 1
        self.count_tab[self.tab] = 0
    
    def increase_count(self):
        self.count_tab[self.tab] += 1

    def decrease_count(self):
        self.count_tab[self.tab] -= 1

    def print(self, mode="w"):
        out = open("out_ast.txt", mode)
        for tab, token in self.ast:
            # if token[0] == "<":
            #     out.write(" "*tab + "(" + "\n")
            # else:
            out.write(" "*tab + token + "\n")

def ll1_parser(input, parsing_table, type, init_ptr):
    ast = AST()
    stack = [type]
    pointer = init_ptr
    while len(stack) > 0:

        if stack[-1] == input[pointer]["type"]:
            stack.pop()
            # print(" "*ast.tab + input[pointer]["token"])
            ast.add_node(input[pointer]["token"])
            ast.remove_tab()
            pointer += 1
            continue

        ast.add_node("<" + stack[-1] + ">")
        # print(" "*ast.tab + "<" + stack[-1] + ">")

        try:
            production = parsing_table[stack[-1]][input[pointer]["type"]]
        except:
            return True, init_ptr, ast

        # print(input[pointer]["token"], stack[-1], production)

        if production == ['EPSILON']:
            stack.pop()
            ast.remove_tab()
            continue
        
        stack.pop()
        ast.remove_tab()
        ast.add_tab()
        for x in production[::-1]:
            ast.increase_count()
            stack.append(x)

    return False, pointer, ast

def parse(vc_token, parsing_table):
    ast_list = []
    pointer = 0
    while pointer < len(vc_token)-1:
        err1, pt1, ast1 = ll1_parser(vc_token, parsing_table, "var-decl", pointer)
        err2, pt2, ast2 = ll1_parser(vc_token, parsing_table, "func-decl", pointer)
        if err1 and err2:
            print("Syntax error at line", vc_token[pointer]["position"])
            return
        elif err1 == False:
            pointer = pt1
            ast_list.append(ast1)
        elif err2 == False:
            pointer = pt2
            ast_list.append(ast2)
    

    ast_list[0].print("w")
    for ast in ast_list[1:]:
        ast.print("a")
    print("Syntax is correct")


vc_token = read('./lexical_scanner/output/example_gcd/example_gcd.verbose.vctok')
parse(vc_token, parsing_table)
