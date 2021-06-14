def func3(x):
    """(float)-> int
    This function removes the numbers after 
    floating point and returns the integer befor dot.
    ex) input: 123.456
    output:123 """
    intlist=[]
    s=0
    for i in range(len(x)):
        if x[i]!='.' and s==0:
            intlist+=x[i]
        if x[i]=='.':
            s+=1
            return ("".join(intlist))

print(func3(input("Enter your number:")))
