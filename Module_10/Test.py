from itertools import zip_longest
l1 = [1,2,3,4]
l2 = [11,12,13,14,15]
l3 = list(zip_longest(l1, l2, fillvalue=None))
print(l3)