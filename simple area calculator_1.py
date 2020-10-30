#for squre type sq ,for rectangle type re,for triangle type tr,for circle type ci

def __computearea(l,b,h,ba,r):
    if x==('squre'):
        return (l**2)
    elif x==('rectangle'):
        return (l*b)
    elif x==('triangle'):
        return ((h*ba)/2)
    elif x==('circle'):
        return (3.142*(r**2))
area_calculate ='yes'
while area_calculate =='yes':
    x=input("enter shape:")
    if x==('squre'):
        l=float(input("enter lenth:"))
        b= h = ba = r = 0
    elif x == ('rectangle'):
        l=float(input('enter lenth:'))
        b=float(input('enter breadth:'))
        h=ba=r=0
    elif x==('triangle'):
        h =float(input('enter hieght'))
        ba=float(input('enter base'))
        l=b=r=0
    elif x==('circle'):
        r =float(input('enter radius'))
        l=b=h=ba=0
    area=  __computearea(l,b,h,ba,r)
    print("Area is:", area)
    area_calculate = input('do you want to calculate more(type yes to continue):')
    
