# Initialize an empty list
my_list = []

# Define a condition to stop taking input (for example, when the user enters 'stop')
stop_condition = 'stop'

while True:
    # Take input from the user
    user_input = input("Enter an element to add to the list (or 'stop' to exit): ")

    # Check if the user wants to stop
    if user_input == stop_condition:
        break

    # Add the input to the list
    my_list += [user_input]

# Print the final list
print("Final list:", my_list)
