from vc_token import VCTokenSet
from constructor.AutomataGraphContrustor import automata_graph_contructor
from constructor.ThompsonConstruction import combine
from constructor.NFAToDFA import nfa_to_dfa
from constructor.DFAToMinimiseDFA import dfa_to_minimise_dfa

def build_automata_graph_from_vc_regex():
    graph = []
    label = {}
    list_token = []
    for token in VCTokenSet.__dict__:
        if '__' not in token:
            subgraph = automata_graph_contructor(VCTokenSet.__dict__[token])
            graph.append(subgraph)
            list_token.append(token)

    final_graph = graph[0]
    
    for state in graph[0].accepting_states:
        label[state] = list_token[0]

    for i in range(1, len(graph)):
        final_graph = combine(final_graph, graph[i])
        for state in final_graph.accepting_states:
            if state not in label:
                label[state] = list_token[i]

    final_graph, label = nfa_to_dfa(final_graph, label=label)
    return final_graph, label