import pyMetrics
import ast
from os.path import dirname, abspath, join
import logging
logging.basicConfig(level="DEBUG")
logger = logging.getLogger()
logger.setLevel("INFO")
import pytest
import pdb


BASE_PATH = dirname(abspath(__file__))

def test_simple_inclusion():
    tree_a = ast.parse("a=1")
    tree_b = ast.parse("b=2;a=1")
    tree_a_assig = tree_a.body[0]
    found = pyMetrics.find_in_trees(tree_a_assig, tree_b)
    assert len(found) > 0    
    logger.info("found: %s", found)

def test_cross_inclusion(caplog):    
    tree_a = ast.parse("a=1+2")
    tree_b = ast.parse("b=1+(1+2)")    
    found = pyMetrics.compare_trees(tree_a, tree_b)    
    # breakpoint()
    logger.info("found: %s", found)
    found = pyMetrics.compare_trees(tree_b, tree_a)
    logger.info("TreeB against TreeA found: %s", found)