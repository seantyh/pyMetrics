
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
    tree = ast.parse("a=a+1;b=b+1;c=c+2;d=d+3")    
    print("nnode: " + str(pyMetrics.node_count(tree)))
    print("depth: " + str(pyMetrics.tree_depth(tree)))

def test_tree_deep():
    tree = ast.parse("[y for y in range(x) for x in range(5) if x % 2]")    
    print("nnode: " + str(pyMetrics.node_count(tree)))
    print("depth: " + str(pyMetrics.tree_depth(tree)))