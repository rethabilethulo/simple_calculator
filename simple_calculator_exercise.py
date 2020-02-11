def multiply(*numbers):
     total = 0
    for number in numbers:
        product = product * number
    return product 

print(multiply(1,2,3,4,5))
print(multiply(1,3))    
print(multiply(-1,3))