class GraphTraveller():
    def __init__(self, data, label):
        self.data = data
        self.label = label

    def move(self, state, symbol):
        for x in self.data.transitions:
            start = x[0]
            sym = x[1]
            end = x[2]
            if state == start and symbol == sym:
                return end
        return None
    
    def check_end(self, state):
        if state in self.data.accepting_states:
            return True
        return False
    
    def get_end(self, state):
        if state in self.data.accepting_states:
            return self.label[state]
        return None