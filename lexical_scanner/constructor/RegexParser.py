
non_symbols = ['+', '*', '.', '|', '?', '(', ')']

def precedence_comparator(a, b):
    p = ["|", "+", ".", "*",  "?"]
    return p.index(a) > p.index(b)

def add_concationate(regex):
    res = []
    char = ""
    for i in range(len(regex)-1):
        if regex[i] not in non_symbols:
            char += regex[i]
            if regex[i + 1] == '(':
                res.append(char)
                char = ""
                res += '.'
        else:
            if char: res.append(char)
            res.append(regex[i])
            char = ""
        if regex[i] in [')', '*', '+', '?'] and regex[i + 1] == '(':
            res += '.'
        if regex[i] in [')', '*', '+', '?'] and regex[i + 1] not in non_symbols:
            res += '.'

    if regex[-1] not in non_symbols: 
        char += regex[-1]
        res.append(char)
    else:
        if char: res.append(char)
        res += regex[-1]
    return res

def make_polish_postfix(regex):
    s = []
    res = []
    for c in regex:
        if c not in non_symbols or c in ["*", "+", "?"]:
            res.append(c)
        elif c == ")":
            while len(s) > 0 and s[-1] != "(": res += s.pop()
            s.pop()
        elif c == "(":
            s.append(c)
        elif len(s) == 0 or s[-1] == "(" or precedence_comparator(c, s[-1]):
            s.append(c)
        else:
            while len(s) > 0 and s[-1] != "(" and not precedence_comparator(c, s[-1]): res += s.pop()
            s.append(c)
    while len(s) > 0: res.append(s.pop())
    return res

def regex_parser(data):
    data = add_concationate(data)
    data = make_polish_postfix(data)
    return data
