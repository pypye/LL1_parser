import os
def remove_eps(tree, node):

    for child in tree.children(node.identifier):
        if child.tag == "EPSILON":
            tree.remove_node(node.identifier)
            return tree
        
        tree = remove_eps(tree, child)
    
    return tree

def remove_parent(tree, node):
    for child in tree.children(node.identifier):
        tree = remove_parent(tree, child)
    
    if len(tree.children(node.identifier)) == 1:
        if tree.parent(node.identifier) != None:
            tree.move_node(tree.children(node.identifier)[0].identifier, tree.parent(node.identifier).identifier)
            tree.remove_node(node.identifier)
    
    return tree

def pretty_print_ast(file, ast):
    ast2 = remove_eps(ast, ast.get_node(ast.root))
    ast3 = remove_parent(ast2, ast2.get_node(ast2.root))
    if os.path.exists(f"./output/{file}/out_ast_reduced.txt"):
        os.remove(f"./output/{file}/out_ast_reduced.txt")
    ast3.save2file(f"./output/{file}/out_ast_reduced.txt", key=lambda x: x.identifier)
    return ast3


def gen_bracket(tree, node):
    strs = "( "
    for child in sorted(tree.children(node.identifier), key=lambda x: x.identifier):
        if not child.tag.startswith("<"):  
            if child.tag == "(":
                strs += "\\( "
            elif child.tag == ")":
                strs += "\\) "
            else:
                strs += child.tag + " "
        strs += gen_bracket(tree, child)
    strs += ") "
    return strs

def bracket_print(file, ast):
    strs = gen_bracket(ast, ast.get_node(ast.root))
    strs = strs.replace("( )", "")
    strs = strs.replace("  ", " ")
    out = open(f"./output/{file}/out_ast_bracket.txt", "w")
    out.write(strs)