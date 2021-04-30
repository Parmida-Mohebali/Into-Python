evenlist=[]
def prog1(a, b):
    """(int, int)-> list
    Return list of even numbers between a and b.
    Ex)
    input: 5, 10
    output:[6, 8]
    Ex)
    input:32, 43
    output:[34, 36, 38, 40, 42]
    """
    if a%2==0:
        for i in range(a+2, b, 2):
            evenlist.append(i)
        return evenlist
    else:
        for i in range(a+1, b, 2):
            evenlist.append(i)
        return evenlist
print(prog1(int(input("Enter your first number:" )), int(input("Enter your second number:"))))

        
