#for squre type sq ,for rectangle type re 
def computearea(l,b):
    if x==('sq'):
        return (l**2)
    elif x==('re'):
        return (l*b)
x=input("enter shape:")
if x==('sq'):
    l=float(input("enter lenth:"))
    b=float(0)

elif x == ('re'):
    l=float(input('enter lenth:'))

    b=float(input('enter breadth:'))

area=  computearea(l,b)
print("Area:", area)
