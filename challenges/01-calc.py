# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operators = {
    "add": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}


while True:
    print("What calculation would you like to do? (add, sub, mult, div) ['exit' to exit]")
    calc = input()
    if calc == 'exit':
        print("Goodbye")
        break
    if not calc in operators:
        print("Not a valid operator")

    else:
        op = operators[calc]
        num_one = int(input("What is number 1?"))
        num_two = int(input("What is number 2?"))

        print(f"Your result is {op(num_one, num_two)}")
