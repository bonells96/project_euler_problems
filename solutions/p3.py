import numpy as np

def smallestPrimeDivisor(n:int) -> int:
    
    "Returns the smallest divisor of n > than 1"

    # if divisible by 2
    if (n % 2 == 0):
        return 2
 
    # iterate from 3 to sqrt(n)
    i = 3
    while(i * i <= n):
        if (n % i == 0):
            return i
        i += 2
 
    return n


def primeDecomposition(n:int) -> int:
    """
    Returns the decomposition of n in prime factors 
    """
    k = n
    smallestPrime = smallestPrimeDivisor(k)
    decomposition = [smallestPrime]
    while(smallestPrime!=k):
        k = int(k/smallestPrime)
        smallestPrime = smallestPrimeDivisor(k)
        decomposition.append(smallestPrime)
    return decomposition

if __name__ == "__main__":

    decomposition = primeDecomposition(600851475143)
    print(decomposition[-1])