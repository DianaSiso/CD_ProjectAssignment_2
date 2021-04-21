"""Test dynamic nodes involving a running DHT."""
import pytest
import time
from DHTClient import DHTClient
from DHTNode import DHTNode


@pytest.fixture(scope="session", autouse=True)
def node():
    node = DHTNode(("localhost", 4000), ("localhost", 5000))
    node.start()
    time.sleep(3)
    yield node
    node.done = True
    node.join()


@pytest.fixture(scope="session", autouse=True)
def node1():
    node = DHTNode(("localhost", 6000), ("localhost", 5000))
    node.start()
    time.sleep(3)
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


def test_put_keystore(node, client):
    assert client.put("10", "Aveiro")

    assert node.identification == 581
    assert node.successor_id == 654

    assert node.keystore == {"10": "Aveiro"}


def test_actual_node_finger_table(node1, node2):
    assert node1.identification == 895
    assert node1.successor_id == 959

    assert node2.identification == 752
    assert node2.successor_id == 770

    assert isinstance(node1.finger_table.as_list, list)

    assert node1.finger_table.as_list == [
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
