# from graphviz import Digraph
# from markdownTable import markdownTable

class AutomataGraph():
    def __init__(self, data, normalize=True):
        self.alphabet = data["alphabet"]
        self.state = data["state"]
        self.initial_state = data["initial_state"]
        self.accepting_states = data["accepting_states"]
        self.transitions = data["transitions"]
        if normalize:
            self.normalize_index()

        
    def normalize_index(self, start_index=0):
        normalized_dict = {}
        for i, state in enumerate(self.state):
            normalized_dict[state] = i + start_index

        self.state = [str(normalized_dict[state]) for state in self.state]
        self.initial_state = str(normalized_dict[self.initial_state])
        self.accepting_states = [str(normalized_dict[state]) for state in self.accepting_states]
        self.transitions = [[str(normalized_dict[transition[0]]), str(transition[1]), str(normalized_dict[transition[2]])] for transition in self.transitions]

    def __str__(self):
        ans = "Alphabet: " + str(self.alphabet) + "\n"
        ans += "State: " + str(self.state) + "\n"
        ans += "Initial State: " + str(self.initial_state) + "\n"
        ans += "Accepting States: " + str(self.accepting_states) + "\n"
        ans += "Transitions: " + str(self.transitions) + "\n"
        return ans
    
    # def draw(self):
    #     self.graph = Digraph()
    #     for x in self.state:
    #         if (x not in self.accepting_states):
    #             self.graph.attr('node', shape='circle')
    #             self.graph.node(x)
    #         else:
    #             self.graph.attr('node', shape='doublecircle')
    #             self.graph.node(x)

    #     self.graph.attr('node', shape='none')
    #     self.graph.node('')
    #     self.graph.edge('', self.initial_state)
    #     for x in self.transitions:
    #         self.graph.edge(x[0], x[2], label=('ε', x[1])[x[1] != 'epsilon'])
        
    #     self.graph.render('nfa', view=True)


    def export_graph(self, path, end_state_name):
        f = open(path, 'w')
        for key in self.__dict__.keys():
            print(key.upper(), file=f)
            if key == 'transitions':
                for x in self.transitions:
                    print(f"{x[0]} {x[1]} {x[2]}", file=f)
            elif key == 'accepting_states':
                for x in self.accepting_states:
                    print(x, end_state_name[x], file=f)
            else:
                for x in self.__dict__[key]:
                    print(x, file=f)
            print("", file=f)

    def export_table(self, path):
        f = open(path, 'w')
        map = {}
        for x in self.transitions:
            if x[0] not in map:
                map[x[0]] = {}
            map[x[0]][x[1]] = x[2]

        data = []
        for x in self.state:
            if x in map:
                row = {}
                row['state'] = x
                for y in self.alphabet:
                    if y in map[x]:
                        row[y] = map[x][y]
                    else:
                        row[y] = ''
                data.append(row)
        # print(markdownTable(data).getMarkdown(), file=f)