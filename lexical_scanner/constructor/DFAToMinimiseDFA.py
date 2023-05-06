from .RegexToNFA import regex_to_nfa
from .NFAToDFA import nfa_to_dfa
from .AutomataGraph import AutomataGraph

def move(data, state, symbol):
    for x in data.transitions:
        start = x[0]
        sym = x[1]
        end = x[2]
        if state == start and symbol == sym:
            return end
    return None

def dfa_to_minimise_dfa(data):
    final_state = data.accepting_states
    non_final_state = [x for x in data.state if x not in final_state]

    moves = {}
    for state in data.state:
        for symbol in data.alphabet:
            if state not in moves:
                moves[state] = {}
            moves[state][symbol] = move(data, state, symbol)
            
    state_map = {}
    for state in data.state:
        state_map[state] = state


    for i in range(len(non_final_state)):
        for j in range(i+1, len(non_final_state)):
            if moves[non_final_state[i]] == moves[non_final_state[j]]:
                state_map[non_final_state[j]] = non_final_state[i]

    for i in range(len(final_state)):
        for j in range(i+1, len(final_state)):
            if moves[final_state[i]] == moves[final_state[j]]:
                state_map[final_state[j]] = state_map[final_state[i]]

    new_transition = []
    for x in data.transitions:
        start = x[0]
        sym = x[1]
        end = x[2]
        new_transition.append([state_map[start], sym, state_map[end]])

    new_transition = list(set([tuple(x) for x in new_transition]))

    new_graph = AutomataGraph({
        "alphabet": data.alphabet,
        "state": sorted(list(set(state_map.values()))),
        "initial_state": state_map[data.initial_state],
        "accepting_states": [state_map[x] for x in data.accepting_states],
        "transitions": new_transition
    })
    return new_graph