# Author RTS 3/16/22
# defines function
def factorial(num): 
    # If Else Statment
    if num != 0: 
        total = 1 
        counter = 1
        while counter <= num: 
            total *= counter 
            counter += 1 
        return total
    else:
        print("Zero cannot be an input") 

# Test 
print(factorial(0)) 
print(factorial(5))
