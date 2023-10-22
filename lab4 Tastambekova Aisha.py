user_input = input("Enter a string without spaces: ")
user_input = user_input.replace(" ", "")  # Remove any spaces from the input
input_tuple = tuple(user_input)
print("Tuple created from the input:", input_tuple)
