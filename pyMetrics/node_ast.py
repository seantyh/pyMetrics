import ast
import _ast

def get_node_types():
    node_types = [x for x in dir(_ast) if x[0].isupper()]
    exclue_types = ['AST', 'PyCF_ONLY_AST', 'Interactive']
    for x in exclude_types:
        node_types.remove(x)
    return node_types

def to_nodetype_vec(codes):
    tree = ast.parse(codes)
    nodes = list(ast.walk(tree))
    node_types = [type(x).__name__ for x in nodes]
    


