from lexical_scanner.graph.GraphFromVCRegex import build_automata_graph_from_vc_regex
from lexical_scanner.graph.GraphTraveller import GraphTraveller
from lexical_scanner.scanner.Scanner import Scanner
from lexical_scanner.scanner.ScannerFromFile import scan
import json
import os

def generate_token(file):
    os.makedirs(f"lexical_scanner/output/{file}", exist_ok=True)
    graph = build_automata_graph_from_vc_regex()
    graph[0].export_graph(f"lexical_scanner/output/{file}/graph.dat", graph[1])
    print("[+] Export graph done")
    graph[0].export_table(f"lexical_scanner/output/{file}/table.dat")
    print("[+] Export table done")
    traveller = GraphTraveller(graph[0], graph[1])
    scanner = Scanner(f"lexical_scanner/input/{file}.vc")
    token = json.load(open('lexical_scanner/vc_token/VCTokenDefinition.json'))
    scan(traveller, scanner, token, vctok_path=f"lexical_scanner/output/{file}/{file}.vctok", vctok_verbose_path=f"lexical_scanner/output/{file}/{file}.verbose.vctok")
    print("[+] Generate token done")

# generate_token("test")