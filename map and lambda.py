# List comprehension

list10 = [a for a in 'niteesh']
print(list)

list1 = [a for a in [32,2,5,4]]
print(list1)

list2 = [b for b in (1,2,3,4,5,6,7) if b%2==0]
print(list2)
list3 = [b for b in 'i am good'.split(' ')]
print(list3)

list4 = [i*i for i in range(1,11)]
print(list4)

list5 = [[j for j in range(3)]for i in range(5)]
print(list5)

# lambda , map, list comprehension at a time

l = list(map(lambda x:x*2,[i for i in range(1,6)]))
print(l)

#### reverse each string in tuple
t = ('niteesh','rupali')
revt = list((a[::-1] for a in t))
print(revt)

### sum of odd element in list
numr = 0
odd = [1,23,4,56,7,9,8,26,9,7,8]
sodd = [x for x in odd if x%2!=0]
print(sodd)
def sum(list):
    sum = 0
    for i in list:
        sum = sum+i
    return sum
print(sum(sodd))

### sum of element in list

def sumlist(i):
    s = 0
    for c in str(i):
        s = s+int(c)
    return s
l5 = [sumlist(i) for i in sodd]
print(l5)

### word from letter of list
def letter(i):
    nb = ''
    for chr in i:
      nb = nb+chr
    return nb

l6 = ['n','i','t','i','s','h']
print(letter(l6))

## MAP & Lambda
# addition
def addition(n):
    return n+n

number = (1,2,3,4,5)
result = map(addition,number)
print(list(result))

result2 = map(lambda n: n+n,number)
print(list(result2))

## addtion of two list
l7 = [1,2,3,4,5]
l8 = [11,12,13,14,15]

result3 = map(lambda a,b:a+b,l7,l8)
print('addition of list l7 & l8:\n',list(result3))


l = ['sat', 'bat', 'cat', 'mat']
result4 = list(map(list,l))
print(result4)