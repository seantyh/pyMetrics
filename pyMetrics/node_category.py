
import ast

def get_node_in_category(tree, type_list):
    nodes = list(ast.walk(tree))
    cat_nodes = []
    for node_x in nodes:
        if type(node_x).__name__ in type_list:
            cat_nodes.append(node_x)        
    return cat_nodes

def get_advance_nodes(tree):
    ADVANCE_NODE_TYPES = [
        "Assert", "AsyncFor", "AsyncFunctionDef",
        "AsyncWith", "Await", "GeneratorExp", "Suite", 
        "Yield", "YieldFrom"
    ]

    return get_node_in_category(tree, ADVANCE_NODE_TYPES)

def get_import_nodes(tree):
    IMPORT_NODE_TYPES = [
        "Import", "ImportFrom"
    ]

    return get_node_in_category(tree, IMPORT_NODE_TYPES)

def get_function_nodes(tree):
    FUNC_NODE_TYPES = ["FunctionDef", "AsyncFunctionDef"]

    return get_node_in_category(tree, FUNC_NODE_TYPES)

def get_class_nodes(tree):
    CLASS_NODE_TYPES = ["ClassDef"]

    return get_node_in_category(tree, CLASS_NODE_TYPES)

def get_string(tree):
    STRING_NODE_TYPES = ["Str"]
    str_nodes = get_node_in_category(tree, STRING_NODE_TYPES)
    str_list = [x.s for x in str_nodes]
    return str_list

def get_called_func_names(tree):
    STRING_NODE_TYPES = ["Call"]
    call_nodes = get_node_in_category(tree, STRING_NODE_TYPES)        
    func_list = [x.func.id for x in call_nodes]
    return func_list

    