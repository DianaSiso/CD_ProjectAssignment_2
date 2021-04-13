"""Tests two clients."""
import pytest
from utils import contains_predecessor, contains_successor

def test_contains_predecessor():
    assert contains_predecessor(300, 100, 200)
    assert contains_predecessor(100, 200, 300)
    assert not contains_predecessor(300, 400, 100)

def test_contains_successor():
    assert contains_successor(100, 300, 200)
    assert contains_successor(300, 200, 100)
    assert not contains_successor(300, 100, 100)
