def locations(s_and_t):
    results = []

    s, t = s_and_t.split()
    l = len(t)

    for i in range(len(s) - l):
        if s[i:i+l] == t:
            results.append(i + 1)

    return results


if __name__ == "__main__":

    small_dataset = "ACGTACGTACGTACGT\nGTA"
    large_dataset = open('rosalind_subs.txt').read()

    results = locations(large_dataset)

    print (' '.join(map(str, results)))