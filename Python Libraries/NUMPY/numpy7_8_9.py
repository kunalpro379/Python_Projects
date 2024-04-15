"""
how to get  access elements of NumPy Array:
1. indexing --> only one element
2. slicing ---> group of elements
Advanced Indexing

"""
# Indexing *****************
"""By using index, we can get/access single elements of the array
numpy follows zeero based elements . i.e the index of first element is 0
numpu supporst both + and _ve indexes
 """
import numpy as np
import time

start=time.time()
a=np.array([10,2,2,3,3,4,4,5,6,6,6])
print(a)
print(a[2])
#print(a[20])
print(a[-5])
"""accessing elements from 2d array"""
#a[RowIndex][ColumnIndex]
b=np.array([[10,2,3],
           [23,23,11]])
print(b[1][2])
# to accesss 23 
print(b[-1][-2],b[1][1],b[1][-2],b[-1][1])
# accessing 3d array elements
#a[i][j][k]  i,j,k -> pos or neg 
#i---->which 2d array
#j----> row index in 2d array 
#k----> column index in 2d array
l=[[[1,2,3],[4,5,6],[6,7,8]],[[1,3,5],[2,4,6],[5,8,0]],[[1,5,9],[2,4,6],[4,8,3]]]
print(l)#----> not a nd array
a=np.array(l)
print(a)#->nd array
## accessing 4d 
#a[i][j][k][l]--->i,j,k,l-->pos or neg
#I-> which 3d array /NO OF 3D ARRAY
#j-->which 2d array/every 3d array contains j 2d arrays
#k-->which row in 2d array
#l-->which column in 2d array
a=np.arange(1,121).reshape(2,3,4,5)
print(a)
print(a[1][2][3][4])
print(np.where(a==98))

#accessing elements of ndarray by using slice operator :
#pythons slice operator
l=[10,23,4,5,6,7,5,33,223]
'''syntax :
l[begin:end]
it returns elemennts from begin index to end-1 index
'''
print(l[2: 7])
print(l[-6:6])
print(l[2:])

#l[begin:end:step]
#default value for step is 1
print(l[1:7])
print(l[1:7:1])
print(l[1:7:2])# every second element
print(l[1:7:3])# every third element
print(l[1:7:4])
print(l[1:7:5])
print(l[1:7:6])# every sixth element
print(l[::4])# 
print(l[::9999999999999999])#until available elements
print(l[::1])# all elements
print(l[10000:20000:3000000])# empty list
print(l[::-1])# total reverse of list
"""for step u cant 0 ,only pos& neg allowed """
#print(l[::0])# error
#print(l[::0.887])#error
# +ve step value-> begin to end-1  in forward direction
#--ve step value-> begin to end+1  in backward direction
# in forward direction if end value is 0 then result is empty list
# in backward direction if end value is -1 then result is empty list

print(l[1:-1:-1])#
print(l[5::-9])# from 5 to 0 in backward direction
#slice oerator on 1d numpy array 
a=np.arange(10,100,1)#same rules as py slice operator
print(a[1:7])
print(a[1:7:1])
print(a[1:7:2])# every second element
print(a[1:7:3])# every third element
print(a[1:7:4])
print(a[1:7:5])
print(a[1:7:6])# every sixth element
print(a[::4])# 
print(a[::9999999999999999])#until available elements
print(a[::1])# all elements
print(a[10000:20000:3000000])# empty list
print(a[::-1])# total reverse of list 
#*************************************************
#b=np.arange()
b=np.random.randint(1,8,size=(3,5))
print(b)
#a[row,col]

#a[begin:end:step,begin:end: step]

print(b[1:3,:])
print(b[0::2,0::2])
print(b[1:2:3,::1])

end=time.time()
total=end-start
print("total execution time:")
print(total)
# ex: 4 by 4
c=np.random.randint(1,8,size=(3,2,6,7))
print(c)

