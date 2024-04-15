import numpy as np


b=np.array([40,50,"60"])
a=np.zeros((3,4),dtype=int)
print(a,b)
#c=np.once((2,3,4),dtype=int)  #2d array ->3 rows ,4 cols
d=np.full((2,3,4),fill_value=7)
print(d)
e=np.full(shape=(2,3,4),fill_value=8)
print(e)
e=np.full((2,3,4),8)
print(e)

#eye():
#to generate identity matrix
#help(np.eye)

#f1(a,b)
#f2(a,/,b)-> we shoulld passs values and positional arg only
#f3(a,*,b) -> we have to compulsory provide valuse  to variables after sstar
#f(*g,y,d)--> g,y,d-> we should provide all values
def f1(a,*,b):
    print(f'a value:{a}')
    print(f'b valuse:{b}')

#f1(10,30)
f1(a=12,b=34) 
f1(10,b=29)
#f1(a=100,20)

#eye(N,M)
#   N--> No of rows 
#   M--> No of colmns if none no of col=no of rows
#k-->np.eye(3)
print(np.eye(2,4))





# ********** 5 *****************
"""
1> randint():
to generate random int values in the given range
randint(low,high=None,size=None,dtype=int)
it will generate a single random int value between specified range
"""
print (np.random.randint(10,20))
# to create 1 d array? of size 10 with randoom valies from 1 to 8
print(np.random.randint(1,8,size=10))

# to create 2d array with shape (3,5)
print(np.random.randint(1,8,size=(3,5)))

print(np.random.randint(100,size=(3,5)))
print(np.random.randint(1,800,size=(3,5,10)))
#each 2d array with 3 rows and 5 cols and 10 such 2d arrays
#each 2d array with 10 rows and 5 cols and 3 such 2d arrays

#print(np.random.randint(1,10,size=(10,5,3), dtype=float))   error
print(np.random.randint(1,10000000,size=(1,2,3)))  
a=np.random.randint(1,11,size=(2,3))
print(a.dtype)
a=np.random.randint(1,11,size=(10,20),dtype='int8')
print(a)
import sys
print(sys.getsizeof(a))   #size in bytes allocated


#how to converting one type array to another type array
b=a.astype('float')  #converting a into float type
print(b)



print(np.random.uniform(10,20))  
print(np.random.uniform(10,20,size=10))
print(np.random.uniform(10,20,size=(2,5,3,4)))



"""visualized """
# s=np.random.uniform(10,20,size=(100000000))
# #visualization of data
# import matplotlib.pyplot as pyplot
# cout,bins,ignored=pyplot.hist(s,15,density=True)
# pyplot.plot(bins,np.ones_like(bins),linewidth=2,color='r')
# pyplot.show()
# print(s.size)
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])


#randn()
#[0,1)
print(np.random.randn(100))
print(np.random.randn(2,3))
#normal destribution
print(np.random.randn())
#normal destribution
#we can customize mean and varience
print(np.random.normal(10,20,size=100))
"""
rand()--->uniform distribution in range [0,1)
uniform()--->uniform distribution  [low,high) our provided range
randn()--->normal distribution values with mean 0 varience is 1

varience-> how much varied the values are from mean   ex -1-0-1

normal()->normal distribution values with our mean and varience

"""
print(np.random.normal())
print(np.random.normal())
print(np.random.normal())
print(np.random.normal())
print(np.random.normal())

print(np.random.normal(10,4,size=10))



"""visualized """
# s=np.random.randn((1000000))
# #visualization of data
# import matplotlib.pyplot as pyplot
# cout,bins,ignored=pyplot.hist(s,15,density=True)
# pyplot.plot(bins,np.ones_like(bins),linewidth=2,color='r')
# pyplot.show()
# print(s.size)
# print(s.mean)
# print(s.var())
# print(s.std())#standard deviation
# print(s[3])

"""visualized """
# s=np.random.normal(10,4,(1000000))
# #visualization of data
# import matplotlib.pyplot as pyplot
# cout,bins,ignored=pyplot.hist(s,15,density=True)
# pyplot.plot(bins,np.ones_like(bins),linewidth=2,color='r')
# pyplot.show()
# print(s.size)
# print(s.mean)
# print(s.var())
# print(s.std())#standard deviation
# print(s[3])

"""randint()

rand()# for uniform distribution
uniform()# for uniform distribution

randn()# normal distributed values
normal()# normal distributed values

"""
#done till now

"""
1.an array with random int values in the given range--> np.random.randint()
2.an array with random float values in the range [0,1) from uniform distribution --> np.random.rand()
#probablity of next value is constant
3.an array with random float values in the specified range from uniform distribution --> np.random.uniform()
4.an array with random float with mean 0 and standard deviation 1 from  from normal distribution --> np.random.randn()
5.an array with random float with specified mean  and standard deviation  from  from normal distribution --> np.random.normal()

"""
# normal distribution is a probablity distribution where probablity of x is 
# highest at center and lowest in the ends where in uniform distributionprobablity of x
# is constant uniform distribution is a probablity distributionwhere probablity of x is constant 

""" *************** shuffle() ************************* """
#shuffle(x) x means nd array

#this function only shuffles the array along the first axis (axis - 0) of a 
#multidimensional array. the order of subarrays is changed but their 
#contents remains the same
a=np.arange(20)
print(a)
aShuff=np.random.shuffle(a)#it will perfomr inline modifications
print(aShuff)#--> output: None
print(a)
#only order will change
""" ********** for 2d arrays """
a=np.random.randint(1,101,size=(5,6)) # 2d array
print(a)  
np.random.shuffle(a)
print(a)  # observe the change in original  and shuffeled array
#it shuffles the array along the first axis only contents remains as it is 
# in 2d array only rows are shuffled

#only order will change
a=np.arange(60).reshape(3,4,5)
print(a) #3*4*5-> 60 elements to arange 
np.random.shuffle(a)
print(a)
#if we apply shuffle in 3d arr just order changed

# # array attributes**************************************
# a.ndim-----> returns the dimensions
# a.shape-----> return shape of the array (10,)  (2,3,5,)
# size ------> to get total number of elements 
# dtype-----> to get the data type of array elements 
# itemsize----> 4 bytes
#