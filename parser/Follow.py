from parser.PaserReader import parserReader
from parser.First import get_first

object_set = set()
def __get_follow__(object_name, grammar):
    follow_set = set()
    follow_set.add("$")

    if object_name in object_set:
        return follow_set
    object_set.add(object_name)

    for obj, production_list in grammar.items():
        for production in production_list:
            if object_name in production:
                index = production.index(object_name)
                if index + 1 < len(production):
                    first_set = get_first(production[index + 1], grammar)
                    if "EPSILON" in first_set:
                        first_set.remove("EPSILON")
                        follow_set = follow_set.union(first_set)
                        follow_set = follow_set.union(__get_follow__(obj, grammar))
                    else:
                        follow_set = follow_set.union(first_set)
                else:
                    follow_set = follow_set.union(__get_follow__(obj, grammar))

    return follow_set

def get_follow(object_name, grammar):
    global object_set
    object_set = set()
    return __get_follow__(object_name, grammar)

# grammar = parserReader('./parser/vc_grammar/VCGrammar.json')
# print(get_follow("declarator-tail", grammar))