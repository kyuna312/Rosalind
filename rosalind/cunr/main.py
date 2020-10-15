
if __name__ == '__main__':
    # A quick function to calculate the double factorial of a given number
    doublefactorial = lambda n: n * doublefactorial(n-2) if n > 1 else 1    
    
    # Read the number of leaves, n.
    n = int(open('./rosalind_cunr.txt', 'r').read())
    
    # The number of trees on n leaves is the double factorial, (2n-5)!!
    print(doublefactorial(2*n-5) % 1000000)
