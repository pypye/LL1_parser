from graph.GraphFromVCRegex import build_automata_graph_from_vc_regex
from graph.GraphTraveller import GraphTraveller
from scanner.Scanner import Scanner
from scanner.ScannerFromFile import scan
import json
import os

def generate_token(file):
    os.makedirs(f"output/{file}", exist_ok=True)
    graph = build_automata_graph_from_vc_regex()
    graph[0].export_graph(f"output/{file}/graph.dat", graph[1])
    print("[+] Export graph done")
    graph[0].export_table(f"output/{file}/table.dat")
    print("[+] Export table done")
    traveller = GraphTraveller(graph[0], graph[1])
    scanner = Scanner(f"input/{file}.vc")
    token = json.load(open('vc_token/VCTokenDefinition.json'))
    scan(traveller, scanner, token, vctok_path=f"output/{file}/{file}.vctok", vctok_verbose_path=f"output/{file}/{file}.verbose.vctok")
    print("[+] Generate token done")

generate_token("in")