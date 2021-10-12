def hamming_distance(s, t):
    dh = 0

    for i, c in enumerate(s):
        if c != t[i]:
            dh += 1
 
    return dh


if __name__ == "__main__":

    small_dataset = """
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    """

    large_dataset = open('rosalind_hamm.txt').read()

    s, t = large_dataset.split()
    dist = hamming_distance(s, t)

    print (dist)