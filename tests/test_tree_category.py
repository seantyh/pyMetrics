
import pyMetrics
import ast

def test_tree_category():
    tree = ast.parse("'asdf';a='32434';func()")
    print(pyMetrics.get_string(tree))
    print(pyMetrics.get_called_func_names(tree))

def test_adv_nodes():
    tree = ast.parse(
        "async def funcA():\n"
        "  yield aaa"
    )
    print(pyMetrics.get_advance_nodes(tree))
    