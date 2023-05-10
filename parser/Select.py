import json
from collections import defaultdict
from .First import get_first_from_production
from .Follow import get_follow

with open("./parser/vc_grammar/VCGrammar.json", 'r') as f:
    data = f.read()
    data = json.loads(data)
    NON_TERMINATE_SYMBOLS = [key for key, value in data.items()]

with open("./parser/vc_grammar/VCGrammarDefinition.json", 'r') as f:
    data = f.read()
    data = json.loads(data)
    TERMINATE_SYMBOLS = [key for key, value in data["decode"].items()] + [key for key in data["token"]]


def build_parsing_table(grammar):
    parsing_table = defaultdict(dict)
    for non_terminal_symbol in NON_TERMINATE_SYMBOLS:
        for production in grammar[non_terminal_symbol]:

            first_set = get_first_from_production(production, grammar)

            if "EPSILON" in first_set:
                first_set.remove("EPSILON")
                follow_set = get_follow(non_terminal_symbol, grammar)
                for terminal_symbol in follow_set:
                    if terminal_symbol in parsing_table[non_terminal_symbol]:
                        raise Exception(f"Grammar is not LL(1). Found duplicate syntax in {non_terminal_symbol} {terminal_symbol}\n"
                                        f"Previous production: {parsing_table[non_terminal_symbol][terminal_symbol]}\n"
                                        f"Current production: {production}")
                    else:
                        parsing_table[non_terminal_symbol][terminal_symbol] = production
                
            for terminal_symbol in first_set:
                if terminal_symbol in parsing_table[non_terminal_symbol]:
                    raise Exception(f"Grammar is not LL(1). Found duplicate syntax in {non_terminal_symbol} {terminal_symbol}\n"
                                    f"Previous production: {parsing_table[non_terminal_symbol][terminal_symbol]}\n"
                                    f"Current production: {production}")
                parsing_table[non_terminal_symbol][terminal_symbol] = production
    return parsing_table