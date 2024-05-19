def fib2(n):
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

p=fib2(111222)
print(p)
"""
def ask_ok(prompt, retries=4, reminder='Please try again!'):
     while True:
             ok = input(prompt)
             if ok in ('y', 'ye', 'yes'):
                return True
             if ok in ('n', 'no', 'nop', 'nope'):
                return False
                retries = retries- 1
             if retries < 0:
                raise ValueError('invalid user response')
                print(reminder)
p=ask_ok("ok",3,"hello")
print(p)

"""




i=5
def f(arg=i):
    print(arg)
i=9
t=f()
print(t)
print(t)


def f(a,L=[]):
     L.append(a)
     return L
print(f(1))
print(f(2))
print(f(3))
print(f(4))

pass
def f2(a,L=None):
    if L is None:
        L=[]
        L.append(a)
        return L
print(f2(1))
print(f2(2))
print(f2(3))
print(f2(4))


def cheeseshop(kind,*arguments,**keywords):
        print("--Doyouhaveany",kind, "?")
        print("--I'msorry,we'realloutof",kind)
        for arg in arguments:
                  print(arg)
                  print("-" *40)
                  for kw in keywords:
                       print(kw,":",keywords[kw])
cheeseshop("Limburger", "It'sveryrunny,sir.",
 "It'sreallyvery,VERYrunny,sir.",
 shopkeeper="MichaelPalin",
 client="JohnCleese",
 sketch="CheeseShopSketch")


def f3(pos, *, pos1):
    print(pos, pos1)


f3(5, pos1=8)
def f4(pos3, /, pos, *, pos1):
    print(pos3, pos, pos1)

# Example usage:
f4(3, pos=5, pos1=8)

def standard_arg(arg):
      print(arg)

standard_arg(32)

def pos_only_arg(arg,/):
     print(arg)
pos_only_arg(2)
pos_only_arg("h")

def kwd_only_arg(*, arg):
     print(arg)

kwd_only_arg(arg=6)
#  error --->   kwd_only_arg(8)
def combined_example(pos_only, /, standard, *, kwd_only):
 print(34422)

 combined_example(1,std="h",kwd_only=2332)

def foo(name, **kwds):
     print(433)

foo("kunal",kwds=7888)

foo(1,**{"kunal":2332})
