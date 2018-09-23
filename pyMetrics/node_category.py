
import ast
import _ast

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
    str_nodes.sort(key=lambda x: x.lineno)
    str_list = [x.s for x in str_nodes]
    return str_list

def get_called_func_names(tree):
    STRING_NODE_TYPES = ["Call"]
    call_nodes = get_node_in_category(tree, STRING_NODE_TYPES)    
    func_list = []
    for node_x in call_nodes:
        func_node = node_x.func
        if isinstance(func_node, _ast.Name):           
            func_list.append(func_node.id)
    return func_list

def get_import_modules(tree):
    imp_nodes = get_import_nodes(tree)
    module_list = []
    
    for node_x in imp_nodes:
        if isinstance(node_x, _ast.Import):
            module_list += [x.name for x in node_x.names]
        else:
            module_list.append(node_x.module)        
    return module_list

def get_definition_names(tree):
    DEF_NODE_TYPES = ["Assign", "AsyncFunctionDef", 
        "FunctionDef", "ClassDef"]
    def_nodes = get_node_in_category(tree, DEF_NODE_TYPES)
    def_names = []
    for node_x in def_nodes:        
        if isinstance(node_x, _ast.Assign):
            for targ_x in node_x.targets:
                if not isinstance(targ_x, _ast.Name):
                    continue
                def_names.append(targ_x.id)            
        elif isinstance(node_x, _ast.FunctionDef):
            def_names.append(node_x.name)
            def_names += [arg_x.arg for arg_x in node_x.args.args]
        elif isinstance(node_x, _ast.AsyncFunctionDef):
            def_names.append(node_x.name)
            def_names += [arg_x.arg for arg_x in node_x.args.args]
        elif isinstance(node_x, _ast.ClassDef):
            def_names.append(node_x.name)
        else:
            print("WARNING: unrecognized node types: %s", 
                type(node_x).__name__)
    return def_names

    