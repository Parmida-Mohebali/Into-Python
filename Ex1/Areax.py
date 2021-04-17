def areax(a, b, c, d, e):
    """(int, int, int, int, int)-> str
    checks out if the inputs are whether sides and
    the diagonal of a quadrilateral or are the sides of
    a triangle. then returns the area of our shape. Ex)
    >>>input:3,4,4,3,5
    output:The Area is:12.0
    >>>input: 3,4,0,4,5
    output:There can be two triangles and their Areas are:6.0,6.0
    """
    if e==0:
        return "An error accured.value of diagonal can't be 0."
    elif a==0:
        s=(b+c+e)/2
        A=(s*(s-b)*(s-c)*(s-e))**0.5
        ss=(c+d+e)/2
        AA=(ss*(ss-c)*(ss-d)*(ss-e))**0.5
        return "There can be two triangles and their Areas are:{},{}".format(A, AA)
    elif b==0:
        s=(a+d+e)/2
        A=(s*(s-a)*(s-d)*(s-e))**0.5
        ss=(c+d+e)/2
        AA=(ss*(ss-c)*(ss-d)*(ss-e))**0.5
        return "There can be two triangles and their Areas are:{},{}".format(A, AA)
    elif c==0:
        s=(a+b+e)/2
        A=(s*(s-a)*(s-b)*(s-e))**0.5
        ss=(a+d+e)/2
        AA=(ss*(ss-a)*(ss-d)*(ss-e))**0.5
        return "There can be two triangles and their Areas are:{},{}".format(A, AA)
    elif d==0:
        s=(a+b+e)/2
        A=(s*(s-a)*(s-b)*(s-e))**0.5
        ss=(b+c+e)/2
        AA=(ss*(ss-b)*(ss-c)*(ss-e))**0.5
        return "There can be two triangles and their Areas are:{},{}".format(A, AA)
    else:
        s=(a+b+e)/2
        A=(s*(s-a)*(s-b)*(s-e))**0.5
        ss=(d+c+e)/2
        AA=(ss*(ss-d)*(ss-c)*(ss-e))**0.5
        return "The Area is:{}".format(A+ AA)
        
        
        
a=int(input("Enter the firt side:"))
b=int(input("Enter the second side:"))
c=int(input("Enter the third side:"))
d=int(input("Enter the forth side:"))
e=int(input("Enter diagonal:"))
print(areax(a, b, c, d, e))
