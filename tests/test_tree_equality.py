import pyMetrics
import ast
from os.path import dirname, abspath, join
import logging
import pytest
import pdb

BASE_PATH = dirname(abspath(__file__))
logging.basicConfig(level="DEBUG")

def test_tree():
    tree_a = ast.parse("a=1")
    tree_b = ast.parse("a=1")
    tree_c = ast.parse("b=1")    

    assert pyMetrics.tree_equals(tree_a, tree_b)
    assert pyMetrics.tree_equals(tree_a, tree_c, structure_only=True)
    assert not pyMetrics.tree_equals(tree_a, tree_c)

def test_complex_tree():
    tree_a = ast.parse("a = 3; a = a + 1")
    tree_b = ast.parse("a = 3; a = a + 1")
    tree_c = ast.parse("b = 3; b = b + 1")

    assert pyMetrics.tree_equals(tree_a, tree_b)
    assert not pyMetrics.tree_equals(tree_a, tree_c)
    assert pyMetrics.tree_equals(tree_a, tree_c, structure_only=True)

def test_code_file():    
    with open(join(BASE_PATH, "data/code_a.py"), "r") as fin:
        code_a = fin.read()
    with open(join(BASE_PATH, "data/code_b.py"), "r") as fin:
        code_b = fin.read()
    tree_a = ast.parse(code_a)
    tree_b = ast.parse(code_b)
    assert not pyMetrics.tree_equals(tree_a, tree_b)
    assert pyMetrics.tree_equals(tree_a, tree_b, structure_only=True)