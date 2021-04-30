def prog4(a):
    """(int)-> list
    Return all divisors of number "a" in a 
    sorted list.
    Ex)
    input= 50
    output=
    Divisors of a are: [1, 2, 5, 10, 25]
    """
    dlist=[1]
    for i in range(2, a):
        if(a%i)==0:
            dlist.append(i)
            dlist.sort()
    return 'Divisors of a are:', dlist

print(prog4(int(input("Enter a:"))))
