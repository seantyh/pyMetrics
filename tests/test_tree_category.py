
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

def test_import_nodes():
    tree = ast.parse(
        "from os.path import join\n"
        "import re"
    )

    print(pyMetrics.get_import_modules(tree))

def test_def_names():
    tree = ast.parse(
        "def funcA(argName):\n"
        "  pass\n"
        "class ClsDummy:\n"
        "  def methodA(method_argX):\n"
        "    pass\n"
        "async def funcAsync(asyncArg):\n"
        "  pass\n"
        "a = 3\n"
    )

    print(pyMetrics.get_definition_names(tree))
    