def func1(str):
    """(str)->list
    returns the words in a string as a 
    list that includes strings.
    ex)input: It's an example.
    output:["It's", 'an', 'example.']"""
    return str.split()

print(func1(input("Enter the string:")))
