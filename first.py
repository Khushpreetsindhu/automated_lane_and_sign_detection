import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a)
print(a[1,2])   
print(a[0,:])
print(a[0,0:4:2]) #startindex:endindex:stepsize
a[1,2]=11
print(a)
#np.zeros
#np.ones
b=np.full((2,3),12)
print(b)
c=np.random.randint( 7,size=(3,3))#to fill random nos
print(c)
d=np.identity(3)
print(d)
#to print multiple times
arr=np.array([[1,2,3]])
r1=np.repeat(arr,4,axis=0)
print(r1)
#que
output=np.ones((5,5))
print(output)
z=np.zeros((3,3))
z[1,1]=9
print(z)
output[1:4,1:4]=z
print(output)
#be carefullllll
#to make direct copy
k=np.array([1,2,3])
h=k.copy()
print(k)
print(h)
h[1]=8
print(k)
print(h)
print(k+h)
print(np.max(h))
#load data from file
#np.genfromtxt('filename',delimiter=',')
#............boolean masking & adv indexing........
#filedata[filedata>50] will return all values which are greter than 50
#you can index with a list in numpy
eg=np.array([1,2,3,4,5,6,7,8,9])
print(eg[[1,2,8]])#to grt 2,3,9 values
#np.any.......axis=0 means column
#np.all.......axis=1 means rows



