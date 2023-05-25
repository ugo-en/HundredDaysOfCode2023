# A simple python code that prints from 1 to 100, with a twist
# If a number is a multiple of 3, it prints fizz
# if it's a number of 5, it prints buzz. If it's a multple of both 3 and 5, 
# it prints fizz buzz

import time


# show welcome message
print(
    '''
Welcome to FizzBuzz!
It is a simple python app that prints from 1 to 100 with a twist.

If a number is a multiple of 3, it prints fizz.
If it's a number of 5, it prints buzz. 
If it's a multple of both 3 and 5, it prints fizz buzz
    '''
)

# start the loop
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
    
    # add a little pause so users can follow easily
    time.sleep(0.5)

