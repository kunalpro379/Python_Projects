#how to create NumPy arrays
"""
1. array()
2. linspace() //linearly spaced elements in a given range and returns ndarray
3. zeros()
4. ones()
5. arange()
6. logspace()
7. eye() //returns 2D array with ones on the diagonal and zeros elsewhere
numpy.random library
8. random.random() 
a) random.randint()
b) random.randn()
c) random.rand()
d) random.random_sample()
e) random.choice()
f) random.bytes()
g) random.shuffle()
h) random.permutation()
i) random.normal()
j) random.uniform()
k) random.triangular()
l) random.gamma()
m) random.exponential()
n) random.poisson()
o) random.chisquare()
, etc.......
9. full()
23. identity()
10. empty()
11. copy()
12. asarray()
13. fromfunction()
14. fromfile()
15. fromstring()
16. fromiter()
17. loadtxt()
18. savetxt()
19. genfromtxt()
20. ndarray()
21. diag()
22. diagflat()
,etc....


"""
# creation of numpy arrays by using arrays() fn
"""
for given list or tuple
"""
import numpy as np

#help(np.array)
"""
copy                                    view
new object will be created    existing obje we are going to reused 


"""
#1d array
l=[10,20,30]  #type of l -> list
a=np.array(l)
print(type(a))
print(a)
#m=np.array([23,1,1,33,[1,23,3,3332,3],32])
#ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (6,) + inhomogeneous part.
p=np.array([23,1,1,33,1,23,3,3332,3,32])

print(p)
print(p.ndim)
"""
Note:p.ndim----> To know dimension of ndarray
a.dtype---> to know data type of elements 
"""
#2d array creation
"""
List of lists
[[],[],[[],[],[[],[],[],[[],[]]]],[[],[]]]--> nested lists

a=np.array([[2,2,2,2],[1,1,1,1,1,1],[[3,3,3,3],[4,4,4,4,4]],[[2,2,2,2],[[6,6,6,6,6],[5,5,5,5,5]],[5,4,3,3,2,1]]])
print(type(a))
print(a.ndim())
print(a)
print(a.dtype)

"""
# 1d array creation

a=np.array(("kunal","deepak","patil"))
print(type(a))
print(a.shape)
#(3,)
print(a.ndim)
print(a.size)
print(a.dtype)

"""array constains only homogenious elements
if the list contains heterogenoius elements then it will convert into string
then upcasting will be performed

"""
a=np.array([10,20.929292929,10.4,20.5,30.6,6,2,222,2,222])
#if upcasting not possible then we may get error
#why not promoted from float to int ?
#downcasting --> loss of information  anything happen automatically
print(type(a))
print(a)

a=np.array([10,303.8887,'a'])#converted into string   converted into common type without losing data
print(a)
m=np.array([122.2,332.665,23,33.776],dtype=int)
print(m)
m=np.array([122.2,332.665,23,33.776,0],dtype=bool)  #nonzero will be true else false
print(m)
m=np.array([122.2,332.665,23,33.776],dtype=float)
print(m)
#how to create array of particular array
m=np.array([122.2,332.665,23,33.776],dtype=complex)
print(m)
m=np.array([122.2,332.665,23,33.776],dtype=str)
print(m)
#if the elements unable to convert to given type , immediately error will be raised
#a=np.arraay([10,"kunal"],dtype=int)#error
"""
how to create object type array??
here any th]ype of elemetnts are allowed 
"""
a=np.array([10,"kunal",293.332,True,10+20j],dtype=object) # elemnt wont converted
print(a)
#now array contain homogeneous elemetnts or not???  yess bro but all the elements are object type
a=np.array([10,"kunal",293.332,True,10+20j]) # elemnt wont converted
print(a)# all the elemetns are converted into strings

#creation of ndarray using arrange() function
"""
normal Python:
range(n)--->n values from 0 to n-1
range(m,n)--> m to n-1

range(begin, end ,step)-> from begin to end-1 with step size
range(1,11,1)---> 1 to 10
range(1,11,2)---> 1,3,5,7,9
range(10,0,-1)---> 10 to 1
range(10,0,-2)---> 10,8,6,4,2

"""
# arrange
"""

"""
a=np.arange(10)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
a=np.arange(1,11)
print(a)

a=np.arange(1,11,3,dtype=float)
print(a)

# so no 2d array by arange() ?

#linspace  function
#---------------------------------------
#linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None,axis=0)
"""
#in the sppecified interval linearly spaced values are generated

arange()vs Linespace()
arange()--> elemetnts will be considered in the given range based on the step svalue
linespace ()---> the specified number of values will be considfered in the given range


"""
p=np.linspace(0,1,30)
print(p)
p=np.linspace(0,2,3)
print(p)# float 



# ******************Zeroes function************
"""
(10,)-> 1d array containes 10 elements 
(5,2)--> 2d array contains 5 rows and 2 columns
(2,3,4)--> 3d array contains 2 matrices each matrix contains 3 rows and 4 columns
"""
#2d array collections of 1d arrays
#3d array collections of 2d arrays


#  (2,3,4)---->3d array-->
"""
2----> 2 number of 2d arrays
3---> the number of rows in every 2d array
4----> the number of colms in every 2d arry
i can consider in this manner also linke 3 2d array and 2 rows and 4 columns is it correct?
"""
a=np.zeros((10,10,10))
#10 2d arrays  each having 10 rows and 10 columns
a=np.zeros((10,10,10,10))
#10 3d arrays  each having 10 2d arrays each having 10 rows and 10 columns
a=np.zeros((10,10,10,10,10),dtype=int)
#10 4d arrays  each having 10 3d arrays each having 10 2d arrays each having 10 rows and 10 columns
print(a)

#do we have (1,3,2)array ?   1 2d array having 3 rows and 2 colmns
#in 1-d array 
#axis-0---> no of rows
#axis-1----> no of columns 
"""
shape: (4,3,4)
4 - 2d arrays  are there(axis-0)
in every 2d array 3 rows are there(axis-1)
4 columns in every 2d array (axis-2)
"""
# order of 2d arrays will be changed but not its internal contents 
