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
    if (predecessor == node):
        return True

    if (identification - predecessor > 0):
        if (node > predecessor) and (node < identification):
            return True
    else:                                           
        if (node > predecessor) or (node < identification):
            return True
    return False

def contains_successor(identification, successor, node):
    if (successor == node):
        return True
    
    if ((identification - successor) < 0): 
        if (node < successor and node > identification):    
            return True
    else:
        if (node < successor) or (node > identification):
             return True
    return False
