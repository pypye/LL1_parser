from PaserReader import parserReader
from Select import build_parsing_table
from ScannerReader import read
import json

grammar = parserReader('./parser/vc_grammar/VCGrammar.json')
parsing_table = build_parsing_table(grammar)

def ll1_parser(input, parsing_table, type, init_ptr):
    stack = [type]
    pointer = init_ptr
    while len(stack) > 0:

        if stack[-1] == input[pointer]["type"]:
            print(input[pointer]["token"], stack[-1], production)
            stack.pop()
            pointer += 1
            continue

        # production = parsing_table[stack[-1]][input[pointer]["type"]]
        try:
            production = parsing_table[stack[-1]][input[pointer]["type"]]
        except:
            return True, init_ptr
    
        # print(input[pointer]["token"], stack[-1], production)

        if production == ['EPSILON']:
            stack.pop()
            continue

        stack.pop()
        for x in production[::-1]:
            stack.append(x)

    return False, pointer

def parse(vc_token, parsing_table):
    pointer = 0
    while pointer < len(vc_token)-1:
        err1, pt1 = ll1_parser(vc_token, parsing_table, "var-decl", pointer)
        err2, pt2 = ll1_parser(vc_token, parsing_table, "func-decl", pointer)
        if err1 and err2:
            print("Syntax error at line", vc_token[pointer]["position"])
            return
        elif err1 == False:
            pointer = pt1
        elif err2 == False:
            pointer = pt2
    
    print("Syntax is correct")


vc_token = read('./lexical_scanner/output/test/test.verbose.vctok')
# for x in vc_token:
#     print(x)
parse(vc_token, parsing_table)
