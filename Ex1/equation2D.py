def equation2d(a, b, c):
    """(int, int, int)->str
       returns answers of a 2d equation. Ex)
       >>>input:(1, 4, 4)
       output:The only answer is:-2.0
       >>>input:(1,-1,-6)
       output:Answers are:3.0,-2.0
       >>>input:(4,4,4)
       output:No answer found  """
    delta= ((b**2) - (4*a*c))
    if  delta==0:
        x=((-b)-(delta**0.5))/(2*a)
        return "The only answer is:{}".format(x)
    elif delta>0:
        x=(-b+(delta**0.5 ))/(2*a)
        xx=(-b-(delta**0.5))/(2*a)
        return 'Answers are:{},{}'.format(x, xx)
    else:
        return "No answer found"
    
a=input("Enter a:")
b=input("Enter b:")
c=input("Enter c:")
print(equation2d(int(a), int(b), int(c)))
