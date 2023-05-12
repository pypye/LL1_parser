from .PaserReader import parserReader
from .Select import build_parsing_table
from .ScannerReader import read
import treelib
import os
import copy

class AST:
    def __init__(self):
        self.tree = treelib.Tree(deep=True)
        self.tree.create_node("<program>", 0)

    def add_node(self, token, id, parent_id):
        self.tree.create_node(token, id+1, parent=parent_id)
        return id+1

def ll1_parser(input, parsing_table, type, init_ptr, ast, id):
    ast = copy.deepcopy(ast)
    stack = [{"production": type, "parent": 0}]
    pointer = init_ptr
    while len(stack) > 0:
        u = stack[-1]
        stack.pop()
        if u["production"] == input[pointer]["type"]:
            id = ast.add_node(input[pointer]["token"], id, u["parent"])
            pointer += 1
            continue

        if u["production"] == "EPSILON":
            id = ast.add_node("EPSILON", id, u["parent"])
            continue

        try:
            production = parsing_table[u["production"]][input[pointer]["type"]]
        except:
            return True, pointer, ast, id
        
        id = ast.add_node("<" + u["production"] + ">", id, u["parent"])
        for x in production[::-1]:
            stack.append({ "production": x, "parent": id})

    return False, pointer, ast, id

def parse(file, vc_token, parsing_table):
    ast = AST()
    pointer = 0
    id = 1
    while pointer < len(vc_token)-1:
        err1, pt1, ast1, id1 = ll1_parser(vc_token, parsing_table, "var-decl", pointer, ast, id)
        err2, pt2, ast2, id2 = ll1_parser(vc_token, parsing_table, "func-decl", pointer, ast, id)
        if err1 and err2:
            raise Exception(f'[var-decl] Syntax error at line {vc_token[pt1]["position"]}\n'
                            f'[func-decl] Syntax error at line", {vc_token[pt2]["position"]}')
        elif err1 == False:
            pointer = pt1
            id = id1
            ast = ast1
        elif err2 == False:
            pointer = pt2
            id = id2
            ast = ast2

    os.makedirs(f"./output/{file}", exist_ok=True)
    if os.path.exists(f"./output/{file}/out_ast_full.vcps"):
        os.remove(f"./output/{file}/out_ast_full.vcps")
    ast.tree.save2file(f"./output/{file}/out_ast_full.vcps", key=lambda x: x.identifier)

    print("[+] Syntax is correct")
    return ast.tree


def LL1_parser(file):
    grammar = parserReader('./parser/vc_grammar/VCGrammar.json')
    parsing_table = build_parsing_table(grammar)
    vc_token = read(f'./lexical_scanner/output/{file}/{file}.verbose.vctok')
    ast = parse(file, vc_token, parsing_table)

    print("[+] LL1 Parse done")
    return ast
