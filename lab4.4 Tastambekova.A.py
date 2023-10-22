def count_element_occurrences(input_tuple):
    element_count = {}
    for item in input_tuple:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1

    element_frequency_pairs = tuple(element_count.items())
   return element_frequency_pairs
example_tuple = (1, 2, 2, 'apple', 'banana', 'apple', [1, 2], [1, 2], (1, 2))
element_frequency_pairs = count_element_occurrences(example_tuple)
print("Element-Frequency Pairs:")
for pair in element_frequency_pairs:
    print(pair)
