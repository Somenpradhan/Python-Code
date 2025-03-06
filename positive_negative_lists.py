# Program to take 10 integer inputs and separate them into positive and negative lists

# Initialize lists
positive_numbers = []
negative_numbers = []

# Take 10 integer inputs from the user
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    if num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)

# Determine which list has more elements and print accordingly
if len(positive_numbers) > len(negative_numbers):
    print("\nPositive Numbers List:", positive_numbers)
    print("Negative Numbers List:", negative_numbers)
else:
    print("\nNegative Numbers List:", negative_numbers)
    print("Positive Numbers List:", positive_numbers)
