
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