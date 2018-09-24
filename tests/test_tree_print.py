
import pyMetrics
import ast

def test_tree_print():
    tree = ast.parse("a=1;print(a+3)")
    pyMetrics.print_tree(tree)

def test_tree_print_func():
    tree = ast.parse(""
    "def funcA():"
    "  a = 1;"
    "  b = 2;"
    "  c = a+b;"
    "  return c"
    )
    pyMetrics.print_tree(tree)
    print("depth: " + str(pyMetrics.tree_depth(tree)))

def test_depth_simple():
    tree = ast.parse("a=a+1")
    pyMetrics.print_tree(tree)
    print("depth: " + str(pyMetrics.tree_depth(tree)))