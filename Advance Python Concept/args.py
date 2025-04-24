#all arguments are stored in tuple 
def sum(*sid):
    total =0
    for item in sid:
        total += item
    
    return total

print(sum(1, 2, 3, 4))