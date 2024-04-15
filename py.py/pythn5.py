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

def f2(a,L=None):
    if L is None:
        L=[]
        L.append(a)
        return L
print(f2(1))
print(f2(2))
print(f2(3))
print(f2(4))