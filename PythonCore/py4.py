#py4.py
print((2332+34343j)*(32332-353453j)*(32332-353453j)*(32332-353453j))
'kunal'
'''hey bro'''
"""hellloo"""


print("""\
   kdskkkkkkkkkkkkkkkkkkkslkkirjer
      ldfkjlfdnsnsmjewjk
      dslfnsfnsekjfnwef m 
      nsjlnfsjnfs
      sdfsndflsdfdkldkkdkekr   
      

      'py'   'thon'
      """)
print('py'  'thon')
something='hey '
print(something+'kunal')


#Lists

squares=[2,1212,1212,121,21,1,2,12,1,12,121,2,12,2]
print(squares[6])
squares=squares[4],[4,'askddkkds',77,232.222,"true"],squares[2:4],squares[4:8],[1,2,2,False,2,2,2,2,2,True,2,0.0000000000,2,2,2,2,2]
print(squares)
# p=squares[4]+[4,'askddkkds',77,232.222,"true"]+squares[2:4]+squares[4:8]+[1,2,2,False,2,2,2,2,2,True,2,0.0000000000,2,2,2,2,2]
# print(p)

pmmms=[[[[[[2],[1],[2],[1],[2]],[[1],[1],[2],[1],[2]],[[2],[222222223],[3],[3],[2]],[[23],[3],[4],[3]]]]]]

#fibonacci series
fib = [0, 1]
i = 2

while i < 15:
    fib.append(fib[i-1] + fib[i-2])
    i += 1

print(fib)


for w in fib:
    if w<23:
        print("true\n")

    elif w<50:
        print("OK\n")
    elif w>34:
        print("no \n")
    else:
        print("error"+101+"\n")


for p in range(2,14):
      print(p)

list(range(1,5))

for i in range(len(fib)):
    print(i, fib[i])

print(sum(range(1,4)))

for n in range(2,13):
   for m in range(33,55):
    if n%m==0:
        print("Yes")
        break
    
    else:
        print("No")

prin=True
# while True:
#     pass
#does nothing no action 

prin=True
# while True:
#     pass
#does nothing no action 

a=1222
#    match a:
#       case 3:
#         return "OK"
#       case 9:
# #         return "OK"
# def check_value(a):
#     result = match a:
#         case 3:
#             return "OK"
#         case 9:
#             return "OK"
#         case _:
#             return "Not OK"
"""
from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color[input("Enter your choice: ")]

match color:
    case Color.RED:
        print("RREEDD")
    case Color.GREEN:
        print("pppppp")
    case Color.BLUE:
        print("mmmmm")
"""

def fib(n):
    a,b=0,1
    while a<n:
        print(a)
        a,b=b,a+b
        print(",")

fib(233)

