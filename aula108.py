#count é um iterador sem fim
from itertools import count

c1 = count(start=8, step=8)
r1 = range(10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(c1, '__iter__'))
print('r1', hasattr(c1, '__next__'))