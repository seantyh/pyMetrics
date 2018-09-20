import ast
import _ast
import logging
import pdb

logger = logging.getLogger("node_ast")
logger.setLevel("INFO")

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
    is_equal = tree_equals(tree_x, tree_ref)
    if not is_equal:
        # step one level down
        ret_buf = []
        children = ast.iter_child_nodes(tree_ref)
        for node_ch in children:
            equal_tree = find_in_trees(tree_x, node_ch)
            pdb.set_trace()
            ret_buf += equal_tree
    else:
        ret_buf = [tree_ref]
    return ret_buf


def tree_equals(tree_a, tree_b, structure_only=False):
    if type(tree_a) is not type(tree_b):
        return False

    fields_a = list(ast.iter_fields(tree_a))
    fields_b = list(ast.iter_fields(tree_b))

    if len(fields_a) != len(fields_b):
        return False

    are_fields_equal = True
    for fd_a, fd_b in zip(fields_a, fields_b):
        name_a = fd_a[0];  name_b = fd_b[0]
        value_a = fd_a[1]; value_b = fd_b[1]

        if name_a != name_b or \
            type(value_a) is not type(value_b):
            logger.debug("name or type mismatch")
            are_fields_equal = False
            break

        if isinstance(value_a, list):
            value_equal = True
            for ch_a, ch_b in zip(value_a, value_b):
                value_equal &= tree_equals(ch_a, ch_b)
                if not value_equal:
                    logger.debug("children mismatch")
                    break
        elif isinstance(value_a, ast.AST):
            value_equal = tree_equals(value_a, value_b)
        else:
            value_equal = value_a == value_b
            if not value_equal:
                logger.debug("simple value mismatch")
        are_fields_equal &= (value_equal or structure_only)

    logger.debug("are_children_equal: %s", are_fields_equal)
    return are_fields_equal



