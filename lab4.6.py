user_input = input("Enter a string without spaces: ")
user_input = user_input.replace(" ", "")
input_set = {char for char in user_input}
print("Set created from the input:", input_set)
