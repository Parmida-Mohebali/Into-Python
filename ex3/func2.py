def func2(str):
    """(str)-> float
    returns the floating point value of the string.
    ex) input: '12.45'
    output:12.45
    if you enter a floating point number, instead
    of a string, it will give you back your own number.
    ex)input:12.45
    output:12.45"""
    numlist=[]
    if type(str) is '':
        for i in range(1,len(str)-1):
            numlist.append(str[i])
        return (''.join(numlist))
    else:
        return (str)
        
    

print(func2(input("Enter the value:")))
