from PaserReader import parserReader

def is_terminal_symbol(string):
    return isinstance(string, str) and string == string.upper()

object_set = set()

def __get_first__(object_name, grammar):
    first_set = set()

    if is_terminal_symbol(object_name):
        first_set.add(object_name)
        return first_set

    if object_name in object_set:
        return first_set
    object_set.add(object_name)

    for x in grammar[object_name]:
        if is_terminal_symbol(x[0]):
            first_set.add(x[0])
        else:
            first_set = first_set.union(__get_first__(x[0], grammar))
    return first_set

def get_first(object_name, grammar):
    global object_set
    object_set = set()
    return __get_first__(object_name, grammar)

def get_first_from_production(production, grammar):
    return get_first(production[0], grammar)
