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
    if (predecessor == node):
        return True

    if (identification - predecessor > 0):
        if (node > predecessor) and (node < identification):
            return True
    else:                                           #here we have 2 options, node is after 0 or node is before 0
        if (node > predecessor) or (node < identification):
            return True
    return False

def contains_successor(identification, successor, node):
    """ Check node (id) is contained between identification and successor."""
    #TODO

    if ((identification - successor) < 0): #458 - 123
        if (node < successor and node > identification):    #123 - 867
            return True
    else:
         if (node < successor) or (node > identification):
             return True
    return False
