"""Tests two clients."""
import pytest
from utils import contains_predecessor, contains_successor


def test_contains_predecessor():
    #identification, predecessor, node
    assert contains_predecessor(100, 200, 300)
    assert not contains_predecessor(300, 400, 100)

def test_contains_successor():
    #identification, successor, node
    assert contains_successor(100, 300, 200)
    assert contains_successor(300, 200, 100)
    assert not contains_successor(300, 100, 100)
