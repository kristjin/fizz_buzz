import sys

def getFoo():
    return raw_input("Please enter the number of foo:  ")

def validFoo(foo):
    try:
        int(foo)
    except ValueError:
        print "I'm so sorry, you must enter a number.  Please try your call again."
        return False
    return True

if len(sys.argv) > 1:
    n = sys.argv[1]
    while not validFoo(n):
        n = getFoo()
else:
    n = getFoo()
    while not validFoo(n):
        n = getFoo()

for i in range(1, int(n)+1):
    if not (i % 5) and not (i % 3):
        print "FizzBuzz!"
    elif not (i % 5):
        print "Buzz!"
    elif not (i % 3):
        print "Fizz!"
    else:
        print i

