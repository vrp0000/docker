import calendar

print('Welcome to the Calendar application!')

import calendar as cal
yr = int(input ("Please enter any year: "))
mon = int(input ("Please enter any month: "))
while 1 == 1:
    if (mon >=1 and mon <=12 ):
        print(cal.month(yr,mon))
        print ("Have a nice day!")
        break
    else:
        print("Incorrect value of month entered. TRY Again")
        mon = int(input ("Please enter any month: "))