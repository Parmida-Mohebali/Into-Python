#gives you your age in days

print("enter your age please.")
age=int(input())
a=age//4
d=(age-a)*365 + a*366
print("you are", d, "days old.")
#example output for 50 age: you are 18262 days old
