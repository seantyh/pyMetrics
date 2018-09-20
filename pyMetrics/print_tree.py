import ast
import _ast
from io import StringIO

def print_tree(tree, depth=0):    
    type_name = type(tree).__name__    
    if isinstance(tree, _ast.Name):
        name = tree.id
        node_repr = "{} ({})".format(type_name, name)    
    elif isinstance(tree, _ast.Num):        
        value = tree.n
        node_repr = "{} ({})".format(type_name, value)
    else:
        node_repr = type_name
    print("-"*depth + node_repr)
    children = ast.iter_child_nodes(tree)
    for ch_x in children:
        print_tree(ch_x, depth+1)    