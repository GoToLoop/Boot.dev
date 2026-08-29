from collections.abc import Iterable

type Int_Or_Iterable = int | Iterable[Int_Or_Iterable]

def sum_nested_list(sizes: Iterable[ int | Iterable[Int_Or_Iterable] ]) -> int:
    return sum( n if isinstance(n, int) else sum_nested_list(n) for n in sizes ) 
