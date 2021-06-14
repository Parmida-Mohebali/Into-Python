from math import gcd
final=[]
def func4(list):
   """تابع اشکال دارد و کار نمی کند"""
    list2=[]
    m=list.split()
    for j in range(1,len(m)-1):
        list2+=m[j]
        for i in range(len(list)):    
            a=list2[i][0]
            b=list2[i][1]
            c=gcd(a, b)
            a, b= (a // c), (b // c)
            final=final.append((x, y))
        return(final)



print(func4(input()))
