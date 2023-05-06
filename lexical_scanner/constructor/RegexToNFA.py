from .RegexParser import regex_parser
from .AutomataGraph import AutomataGraph
from .ThompsonConstruction import and_rule, or_rule, multiplier_rule, plus_rule, question_rule

non_symbols = ['+', '*', '.', '|', '?', '(', ')']

def regex_to_nfa(data):
    postfix_data = regex_parser(data)
    s = []
    for x in postfix_data:
        if x not in non_symbols:
            ag = AutomataGraph({
                "alphabet": [x],
                "state": [0, 1],
                "initial_state": 0,
                "accepting_states": [1],
                "transitions": [[0, x, 1]]
            })
            s.append(ag)
        else:
            ag = None
            if x == "|":
                ag = or_rule(s[-2], s[-1])
                s = s[:-2]
            elif x == ".":
                ag = and_rule(s[-2], s[-1])
                s = s[:-2]
            elif x == "*":
                ag = multiplier_rule(s[-1])
                s = s[:-1]
            elif x == "+":
                ag = plus_rule(s[-1])
                s = s[:-1]
            elif x == "?":
                ag = question_rule(s[-1])
                s = s[:-1]
            s.append(ag)

    return s[0]