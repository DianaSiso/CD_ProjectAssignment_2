"""Tests two clients."""
import pytest
import time
from DHTClient import DHTClient
from DHTNode import DHTNode, FingerTable


@pytest.fixture(scope="session", autouse=True)
def node():
    node = DHTNode(("localhost", 6000), ("localhost", 5000))
    node.start()
    time.sleep(10)
    yield node
    node.done = True
    node.join()


@pytest.fixture(scope="session", autouse=True)
def node2():
    node = DHTNode(("localhost", 3000), ("localhost", 5000))
    node.start()
    time.sleep(10)
    yield node
    node.done = True
    node.join()


@pytest.fixture()
def client():
    return DHTClient(("localhost", 5000))


def test_finger_table():
    f = FingerTable(10, ("localhost", 5000), 4)

    assert f.getIdxFromId(11) == 1
    assert f.getIdxFromId(12) == 2
    assert f.getIdxFromId(14) == 3
    assert f.getIdxFromId(18) == 4

    f.fill(11, ("localhost", 5001))

    assert f.find(11) == ("localhost", 5001)
    assert f.find(12) == ("localhost", 5001)

    f.update(2, 12, ("localhost", 5002))
    f.update(3, 15, ("localhost", 5003))
    f.update(4, 20, ("localhost", 5004))

    assert f.as_list == [
        (11, ("localhost", 5001)),
        (12, ("localhost", 5002)),
        (15, ("localhost", 5003)),
        (20, ("localhost", 5004)),
    ]

    assert f.find(13) == ("localhost", 5002)

    assert f.refresh() == [
        (1, 11, ("localhost", 5001)),
        (2, 12, ("localhost", 5002)),
        (3, 14, ("localhost", 5002)),
        (4, 18, ("localhost", 5003)),
    ]


def test_actual_node_finger_table(node, node2):
    assert node.identification == 895
    assert node.successor_id == 959

    assert node2.identification == 752
    assert node2.successor_id == 770

    assert isinstance(node.finger_table.as_list, list)

    assert node.finger_table.as_list == [
        (959, ("localhost", 5001)),
        (959, ("localhost", 5001)),
        (959, ("localhost", 5001)),
        (959, ("localhost", 5001)),
        (959, ("localhost", 5001)),
        (959, ("localhost", 5001)),
        (959, ("localhost", 5001)),
        (257, ("localhost", 5003)),
        (257, ("localhost", 5003)),
        (581, ("localhost", 4000)),
    ]

    assert node2.finger_table.as_list == [
        (770, ("localhost", 5000)),
        (770, ("localhost", 5000)),
        (770, ("localhost", 5000)),
        (770, ("localhost", 5000)),
        (770, ("localhost", 5000)),
        (895, ("localhost", 6000)),
        (895, ("localhost", 6000)),
        (895, ("localhost", 6000)),
        (257, ("localhost", 5003)),
        (257, ("localhost", 5003)),
    ]
