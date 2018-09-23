import ast
import _ast
from collections import OrderedDict
import math
import logging
logger = logging.getLogger("NodeVec")
logger.setLevel("INFO")

def get_type_axis():
    node_types = [x for x in dir(_ast) if x[0]!="_"]
    exclude_types = ['AST', 'PyCF_ONLY_AST', 'Interactive']    
    for x in exclude_types:
        node_types.remove(x)
    return node_types

def to_type_vec(tree):    
    nodes = list(ast.walk(tree))
    type_names = [type(x).__name__ for x in nodes]
    type_axis = get_type_axis()
    type_count = [0] * len(type_axis)
    for name_x in type_names:
        try:
            type_idx = type_axis.index(name_x)
            type_count[type_idx] += 1
        except ValueError as ex:            
            logger.warning(ex)
    return type_count

def euclidean_distance(vec_a, vec_b):
    distx = 0
    for a, b in zip(vec_a, vec_b):
        distx += abs(a-b) ** 2
    return math.sqrt(distx)

def manhattan_distance(vec_a, vec_b):
    distx = 0
    for a, b in zip(vec_a, vec_b):
        distx += abs(a-b)
    return distx
