def find_next_state(traveller, token, state, char):
    for tk in token.keys():
        if char in token[tk]:
            return traveller.move(state, tk)
    return traveller.move(state, "other")


def output_vctok(traveller, vc_tok, vc_tok_verbose,state, current_word, scanner, type):
    print(current_word, file=vc_tok)
    current_word = current_word.replace("\"", "")
    if type == 'forward':
        print(f'Kind = {state} [{traveller.get_end(state)}], spelling = \"{current_word}\"'
            f', position = {scanner.count_line}({scanner.count_col})..{scanner.count_line}({scanner.count_col+len(current_word)-1})',
            file=vc_tok_verbose)
    elif type == 'backward':
        print(f'Kind = {state} [{traveller.get_end(state)}], spelling = \"{current_word}\"'
            f', position = {scanner.count_line}({scanner.count_col-len(current_word)})..{scanner.count_line}({scanner.count_col-1})',
            file=vc_tok_verbose)

def scan(traveller, scanner, token, vctok_path, vctok_verbose_path):
    vc_tok = open(vctok_path, 'w')
    vc_tok_verbose = open(vctok_verbose_path, 'w')
    state = "0"
    current_word = ""
    char = None
    while True:
        if state == None:
            raise Exception(f'Invalid token for "{current_word}" at line {scanner.count_line}, col {scanner.count_col}')

        # look word ahead
        word = scanner.peek_word()
        next_state = find_next_state(traveller, token, state, word)
        if traveller.check_end(next_state):
            if traveller.get_end(next_state) != "SPACE":
                output_vctok(traveller, vc_tok, vc_tok_verbose, next_state, current_word + word, scanner, type='forward')
            current_word = ""
            state = "0"
            if not scanner.seek_word():
                break
            continue

        # look 2 chars ahead
        char_2 = scanner.peek_char(2)
        next_state = find_next_state(traveller, token, state, char_2)
        if traveller.check_end(next_state):
            if traveller.get_end(next_state) != "SPACE":
                output_vctok(traveller, vc_tok, vc_tok_verbose, next_state, current_word + char_2, scanner, type='forward')
            current_word = ""
            state = "0"
            if not scanner.seek_char(2):
                break
            continue

        # look 1 char ahead
        char = scanner.peek_char()
        next_state = find_next_state(traveller, token, state, char)
        
        if next_state == None and traveller.check_end(state):
            if traveller.get_end(state) != "SPACE":
                output_vctok(traveller, vc_tok, vc_tok_verbose, state, current_word, scanner, type='backward')
            current_word = ""
            state = "0"

        else:
            current_word += char
            state = next_state 
            if not scanner.seek_char():
                break
    if char:
        next_state = find_next_state(traveller, token, state, char)
        if next_state == None and traveller.check_end(state):
            if traveller.get_end(state) != "SPACE":
                output_vctok(traveller, vc_tok, vc_tok_verbose, state, current_word, scanner, type='backward')
            state = "0"
    if state == None: state = "0"
    next_state = find_next_state(traveller, token, state, "__eof__")
    if traveller.check_end(next_state):
        output_vctok(traveller, vc_tok, vc_tok_verbose, next_state, "$", scanner, type='forward')
    else:
        raise Exception(f'Invalid token for "{current_word}" at line {scanner.count_line}, col {scanner.count_col}')