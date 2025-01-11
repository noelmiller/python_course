from math import isclose


print(.1 + .2 == 3) # False

print(f".1 + .2 = {0.1 + 0.2}") # 0.1 + 0.2 = 0.30000000000000004

a: float = .1 + .2
b: float = .3

print(f'{a} == {b}?', isclose(a, b, rel_tol=.001)) # these numbers are less than .1% apart
