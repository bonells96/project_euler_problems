from typing import List

def multiples(multiple: int, bound: int) -> List[int]:
    return ([multiple*n for n in range(int(bound/multiple)+1) if multiple*n<bound])

if __name__ == "__main__":
    print(sum(set(multiples(3,1000) + multiples(5,1000))))