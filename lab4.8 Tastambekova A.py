set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
set_a = {x for x in set_a if x not in set_b}
print("Set A after removing common elements:", set_a)
