from itertools import combinations
superset_a = {1, 2, 3, 4, 5, 6}
m = 3
n = 3
list_of_sets = []
for _ in range(m):
    unique_combinations = set(combinations(superset_a, n))
    list_of_sets.append(unique_combinations)
for i, set_of_combinations in enumerate(list_of_sets, 1):
    print(f"Set {i}: {set_of_combinations}")
