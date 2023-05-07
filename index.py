"""Create a function that checks to see if two numbers sum are
less than 100"""

def less_than100(num1, num2):
    total = num1 + num2

    if total < 100:
        return f"{total} is less than 100"
    else:
        return f"{total} is greater than 100"

print(less_than100(22, 95))