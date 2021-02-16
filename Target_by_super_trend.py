def intraday(entry_val,previous_val):
    if position == 'long':
        return (((entry_val-previous_val)/2)+entry_val)
    else:
        return (entry_val-((entry_val-previous_val)/2))
    





print('target approch using the supertrend techniqcal study')
target='yes'
while target=='yes':
    position = input('enter long or short: ')
    entry_val= float(input('enter the entry price: '))
    previous_val= float(input('enter the privious val: '))
    tar_price= intraday(entry_val,previous_val)
    print(tar_price)
    target=input('do u wnt to continue: ')
