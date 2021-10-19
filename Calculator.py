#addition
def add(x,y):
    return x + y
#sutraction
def sub(x,y):
    return x - y
#multiplication
def mul(x,y):
    return x * y
#division
def div(x,y):
    return x / y
#main calculator programe
print('calculator to calculate addition, subtraction,multiplication,division')
print('Choose operation to perform on two numbers')
print('1.add\n2.sub\n3.mul\n4.div')
num = int(input('enter opration number'))
a = int(input('enter 1st number'))
b = int(input('enter 2nd number'))
if num==1:
    print('addition of numbers',add(a,b))
elif num==2:
    print('subtraction of numbers=',sub(a,b))
elif num==3:
    print('multiplication of numbers=',mul(a,b))
elif num==4:
    print('Division of numbers=',div(a,b))
else:
    print('requested operation is not in calculator')

