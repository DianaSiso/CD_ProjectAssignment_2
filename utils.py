def dht_hash(text, seed=0, maximum=2**10):
    """ FNV-1a Hash Function. """
    fnv_prime = 16777619
    offset_basis = 2166136261
    h = offset_basis + seed
    for char in text:
        h = h ^ ord(char)
        h = h * fnv_prime
    return h % maximum


def contains_predecessor(identification, predecessor, node):
    """ Check node (id) is contained between predecessor and identification."""
    #TODO
    return False


def contains_successor(identification, successor, node):
    """ Check node (id) is contained between identification and successor."""
    #TODO
    return False
