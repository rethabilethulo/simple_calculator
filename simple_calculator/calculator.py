def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

def multiply(*numbers):
    #Multiply elements one by one
    product = 1
    for number in numbers:
        product = product * number
    return product 