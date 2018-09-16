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

def compare_trees(tree_x, tree_ref):
    children = tree_x.iter_child_nodes()
    for node_ch in children:
        compare_trees(node_ch, tree_ref)
    print(tree_x)
    find_in_trees(tree_x, tree_ref)

def find_in_trees(tree_x, tree_ref):
    children = tree_ref.iter_child_nodes()
    for node_ch in children:
        node_ref = find_in_trees(tree_x, node_ch)
        if not node_ref:
            return None

def tree_equals(tree_a, tree_b):
    pass


