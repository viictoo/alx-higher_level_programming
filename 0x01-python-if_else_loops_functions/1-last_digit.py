#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = number
if dig >= 0:
    print('Last digit of {} is {}'.format(number, dig % 10), end=" ")
    if (dig % 10) > 5:
        print("and is greater than 5")
    elif (dig % 10) > 0 and (dig % 10) < 6:
        print("and is less than 6 and not 0")
    else:
        print("and is 0")
elif dig < 0:
    dig = dig * -1
    print('Last digit of {} is -{} and is less than 6 and not 0'
          .format(number, dig % 10))
