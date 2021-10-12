from math import sqrt
def k_recurrence_relation(n, k):
    if n < 40: 
        if n == 0 or n == 1:
            return n
        else: 
            return k_recurrence_relation(n - 1, k) + k * k_recurrence_relation(n - 2, k)    # Recursive functional call for Fibonacci calculation
    else:
        return round((1 + sqrt(5))**n - (1 - sqrt(5))**n) / (2**n*sqrt(5))      # Approximates fibonacci sequence result for runtime
def main():
    FILEPATHREAD = "rosalind_fib.txt"
    FILEPATHWRITE = "FIB-output.txt"
    with open(FILEPATHREAD, "r") as fr:
        data = fr.read().split(" ")
    with open(FILEPATHWRITE, "w") as fw:
        fw.write(str(k_recurrence_relation(int(data[0]), int(data[1]))))
    return print("\nThe recurrence relational dataset has been processed and the appropriate output has been saved to {}.\n".format(FILEPATHWRITE))
if __name__ == "__main__":
    main()