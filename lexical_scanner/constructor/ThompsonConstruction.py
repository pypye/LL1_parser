from .AutomataGraph import AutomataGraph

def and_rule(r: AutomataGraph, s: AutomataGraph):
    clone_r = AutomataGraph(r.__dict__)
    clone_s = AutomataGraph(s.__dict__)
    clone_r.normalize_index(start_index=0)
    clone_s.normalize_index(start_index=len(r.state)-1)
    for transition in clone_s.transitions:
        if transition[0] == clone_s.initial_state:
            transition[0] = clone_r.accepting_states[0]

    data = {
        "alphabet": list(set(clone_r.alphabet + clone_s.alphabet)),
        "state": sorted(list(set(clone_r.state + clone_s.state))),
        "initial_state": clone_r.initial_state,
        "accepting_states": clone_s.accepting_states,
        "transitions": clone_r.transitions + clone_s.transitions
    }
    return AutomataGraph(data)


def or_rule(r: AutomataGraph, s: AutomataGraph):
    clone_r = AutomataGraph(r.__dict__)
    clone_s = AutomataGraph(s.__dict__)
    clone_r.normalize_index(start_index=1)
    clone_s.normalize_index(start_index=len(r.state)+1)
    accepting_state = str(len(clone_r.state) + len(clone_s.state) + 1)
    data = {
        "alphabet": list(set(clone_r.alphabet + clone_s.alphabet)),
        "state": sorted(list(set(["0"] + clone_r.state + clone_s.state + [accepting_state]))),
        "initial_state": "0",
        "accepting_states": [accepting_state],
        "transitions": [
            ["0", "epsilon", clone_r.initial_state],
            ["0", "epsilon", clone_s.initial_state], 
        ] + clone_r.transitions + clone_s.transitions + [
            [clone_r.accepting_states[0], "epsilon", accepting_state],
            [clone_s.accepting_states[0], "epsilon", accepting_state]
        ]
    }
    return AutomataGraph(data)

def multiplier_rule(r: AutomataGraph):
    clone_r = AutomataGraph(r.__dict__)
    clone_r.normalize_index(start_index=1)
    accepting_state = str(len(clone_r.state) + 1)
    data = {
        "alphabet": clone_r.alphabet,
        "state": sorted(list(set(["0"] + clone_r.state + [accepting_state]))),
        "initial_state": "0",
        "accepting_states": [accepting_state],
        "transitions": clone_r.transitions + [
            ["0", "epsilon", clone_r.initial_state],
            [clone_r.accepting_states[0], "epsilon", clone_r.initial_state],
            [clone_r.accepting_states[0], "epsilon", accepting_state],
            ["0", "epsilon", accepting_state],
        ]
    }
    return AutomataGraph(data)


def plus_rule(r: AutomataGraph):
    clone_r = AutomataGraph(r.__dict__)
    clone_r.normalize_index(start_index=1)
    accepting_state = str(len(clone_r.state) + 1)
    data = {
        "alphabet": clone_r.alphabet,
        "state": sorted(list(set(["0"] + clone_r.state + [accepting_state]))),
        "initial_state": "0",
        "accepting_states": [accepting_state],
        "transitions": clone_r.transitions + [
            ["0", "epsilon", clone_r.initial_state],
            [clone_r.accepting_states[0], "epsilon", clone_r.initial_state],
            [clone_r.accepting_states[0], "epsilon", accepting_state],
        ]
    }
    return AutomataGraph(data)


def question_rule(r: AutomataGraph):
    clone_r = AutomataGraph(r.__dict__)
    clone_r.normalize_index(start_index=1)
    accepting_state = str(len(clone_r.state) + 1)
    data = {
        "alphabet": clone_r.alphabet,
        "state": sorted(list(set(["0"] + clone_r.state + [accepting_state]))),
        "initial_state": "0",
        "accepting_states": [accepting_state],
        "transitions": clone_r.transitions + [
            ["0", "epsilon", clone_r.initial_state],
            ["0", "epsilon", accepting_state],
            [clone_r.accepting_states[0], "epsilon", accepting_state],
        ]
    }
    return AutomataGraph(data)


def combine(r: AutomataGraph, s: AutomataGraph):
    clone_r = AutomataGraph(r.__dict__)
    clone_s = AutomataGraph(s.__dict__)
    clone_r.normalize_index(start_index=0)
    clone_s.normalize_index(start_index=len(r.state)-1)
    for transition in clone_s.transitions:
        if transition[0] == clone_s.initial_state:
            transition[0] = clone_r.initial_state

    clone_s.state.remove(clone_s.initial_state)

    data = {
        "alphabet": list(set(clone_r.alphabet + clone_s.alphabet)),
        "state": clone_r.state + clone_s.state,
        "initial_state": clone_r.initial_state,
        "accepting_states": clone_r.accepting_states + clone_s.accepting_states,
        "transitions": clone_r.transitions + clone_s.transitions
    }
    return AutomataGraph(data, normalize=False)