set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8}
set_c = {3, 4, 9, 10}
for element in set_a.copy():
    if element in set_c:
        set_a.remove(element)
        set_b.add(element)   
print("Set A after removal:", set_a)
print("Set B after addition:", set_b)
