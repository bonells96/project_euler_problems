from typing import List
import math

golden_section = (1 + math.sqrt(5)/2)


def fibonacci_list(bound:int) -> List[int]:
    f_0 = 1
    f_1 = 2

    fibonacci_series = {0:f_0, 1:f_1}

    f = 2
    k=2
    while f < bound:
        f = (fibonacci_series[k-1] + fibonacci_series[k-2])
        if f > bound:
            break
        fibonacci_series[k] = f
        k+=1
    return fibonacci_series

if __name__ == "__main__":

    list_fibonacci = fibonacci_list(4000000)
    print(sum([n for _,n in list_fibonacci.items() if n%2==0]))