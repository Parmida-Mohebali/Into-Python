def prog3(a):
    """ (int)-> bool
    Firstly checks wether the given number, a,
    is a prime number or not, then returns True and False.
    Ex)if a is less than 2, the answer is "False".
    input: 1
    output: False
    Ex) if a==2 the answer is "True". 
    input:2
    output:True
    Ex)for more than 2, it uses the Trial division
    to findout wether a is a prime number or not.
    input: 5
    output:True
    Ex) 
    input:50
    output:False
    """ 
    if a<2:
        return False
    if a==2:
        return True
    sqa = a**0.5
    i = 2
    while i <= sqa:
        if a % i == 0:
            return False
        i += 1
    return True

print(prog3(int(input("Enter number a:"))))
