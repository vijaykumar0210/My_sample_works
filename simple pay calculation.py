name = input("enter name of the employee: ")
#enter details of the employees details
hrs = float(input("enter hours "))
#if the hours worked by the employee is more than 40 the rate will increase for remaining hours above 40
rate = float(input("enter rate "))
print("total hours worked by"+name,hrs)
print("total rate availed to "+name,rate)
if hrs<40:
    p=(hrs*rate)
if hrs>40:
    p=((hrs-40)*(rate*1.5))+(40*rate)
print("total gross pay :",p)
if p >1000:
    print('grade according to total hrs worked: A')
elif p<=500:
    print('grade according to total hrs worked: B')
elif p<500:
    print('grade according to total hrs worked: C')
