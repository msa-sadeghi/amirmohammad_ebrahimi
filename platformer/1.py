def myfunction(numbers):
    s = 0
    for n in numbers:
        if n % 2 == 0:
            s += n
    return s
        
        
print(myfunction([1,2,3,4,5,6,7,8,9]))
            