import pyMetrics
import ast

def test_node_vec():
    tree_a = ast.parse("a=1;b=3;c='asdf';print('123')")
    vec = pyMetrics.to_type_vec(tree_a)
    types = pyMetrics.get_type_axis()
    print([(type_x, count_x) for type_x, count_x in zip(types, vec)])

def test_vec_compare():
    tree_a = ast.parse("a=1;b=3;c='asdf';print('123')")
    tree_b = ast.parse("b=1;ad=3;\n" 
        "def func(x):\n"
        "  input('123')")
    vec_a = pyMetrics.to_type_vec(tree_a)
    vec_b = pyMetrics.to_type_vec(tree_b)

    mdist = pyMetrics.manhattan_distance(vec_a, vec_b)
    edist = pyMetrics.euclidean_distance(vec_a, vec_b)
    print("L2: %.2f, L1: %.2f" % (edist, mdist))