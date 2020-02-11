def add(*numbers) :
    total = 0
    for number in numbers:
        total = total + number
    return total 
    
    
print(add(1,2,3,4,5))   
print(add(1,2))
print(add(-1 ,-1))
print(add(1,2,3,4))

