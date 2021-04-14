def swap(A, B):
    """(int, int)->int
       returns A swaped with B. Ex)
       input:(A, B)
       output:(B, A) """
    C=A
    A=B
    B=C
    return A, B

a=input("Enter a:")
b=input("Enter b:")
print("a swaped with b:", swap(int(a), int(b)))
