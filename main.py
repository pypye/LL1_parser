from lexical_scanner.gen_tok import generate_token
from parser.Select import build_parsing_table
from parser.PaserReader import parserReader
from parser.ScannerReader import read
from parser.LL1_Paser import parse
import json

generate_token("test")
vc_token = read('./lexical_scanner/output/test/test.verbose.vctok')
grammar = parserReader('./parser/vc_grammar/VCGrammar.json')
parsing_table = build_parsing_table(grammar)
parse(vc_token, parsing_table)