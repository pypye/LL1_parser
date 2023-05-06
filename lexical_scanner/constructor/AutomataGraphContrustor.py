from .RegexToNFA import regex_to_nfa
from .NFAToDFA import nfa_to_dfa
from .DFAToMinimiseDFA import dfa_to_minimise_dfa

def automata_graph_contructor(regex):
    data = regex_to_nfa(regex)
    data = nfa_to_dfa(data)
    data = dfa_to_minimise_dfa(data)
    return data

