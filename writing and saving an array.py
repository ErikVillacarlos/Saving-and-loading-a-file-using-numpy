import numpy as np
# First, Save and Write Files using NumPy
# Second, Load data from files using Numpy:
# Here are three examples of it:

print(' Number 1:')

#create an array
a = np.array([[5,6,7,8],[2,5,3,2]])
b = np. array([[9,8,7,6],[10,12,13,15]])
c = np.array([[6,7,5,3],[2,3,4,7]])

#Save the array to a text file
np.savetxt('a.txt',a)
np.savetxt('b.txt',b)
np.savetxt('c.txt',c)

#load data from text file
d = np.loadtxt('a.txt')
e = np.loadtxt('b.txt')
f = np.loadtxt('c.txt')

print(d)
print()
print(e)
print()
print(f)
print()

#number 2 

print('Number 2:')
#create an array
x = np.array([[2,3,6,7],[9,8,7,6]])
y = np.array([[15,16,17,18],[12,20,21,22]])
z = np. array([[7,8,9,10],[15,30,45,60]])

#save the array to a binary file
np.save('x.npy',x)
np.save('y.npy',y)
np.save('z.npy',z)

#load the array to a binary file
g = np.load('x.npy')
h = np.load('y.npy')
i = np.load('z.npy')

print()
print(g)
print()
print(h)
print()
print(i)
print()

print('Number 3:')

 #create arrays
j = np.array([[3,4,5,6]])
k = np. array([[9,7,6,7]])
l = np.array([[7,4,5,8]])
m = np.array([[5,6,7,9]])
n = np. array([[6,7,8,5]])
o = np.array([[5,4,9,8]])

#save the array to a single binary file
np.savez('data.npz', j=j, k=k, l=l, m=m, n=n,o=o,)

# load data from an npz file
loaded_data = np.load('data.npz')

#access the arrays
print(j[0])
print(k[0])
print()
print(l[0])
print(m[0])
print()
print(n[0])
print(o[0])
