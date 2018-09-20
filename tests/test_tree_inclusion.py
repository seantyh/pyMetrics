import pyMetrics
import ast
from os.path import dirname, abspath, join
import logging
import pytest
import pdb


BASE_PATH = dirname(abspath(__file__))
logging.basicConfig(level="DEBUG")
logger = logging.getLogger()


def test_simple_inclusion():
    tree_a = ast.parse("a=1")
    tree_b = ast.parse("b=2;a=1")
    found = pyMetrics.find_in_trees(tree_a, tree_b)
    assert len(found) > 0
    logger.info("found: %s", found)