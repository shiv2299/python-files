import numpy as np

#creating np array with zeros, we can also create sae for 1 using np.ones(size) method
arr0 = np.zeros(3)
print(arr0)

print(arr0[0].dtype)

#creating np array with empty() method, which puts random numbers in the array to increase speed in compare to zeros & ones
arr_empty = np.empty(4)
print(arr_empty)

# creating numpy array
arr1 = np.array([2345,234,2,4,86,54])
print(arr1)

# reshaping an array - changing dimension & size of array
arr2 = np.array([2345,234,2,4,86,54]).reshape(6,1)
print(arr2)

# np array from given range
arr_range = np.arange(13)
print(arr_range)

# np array within specified range & step size, Args - rangelimit1, rangelimit2, step
arr2_range = np.arange(52,45,-2.5)
print(arr2_range)

# np array with linspace() to diving range in linear interval given in num argument.
arr_linspace = np.linspace(2, 3, num=10)
print(arr_linspace)

# creating array with your specified dataype instead of positive number, default is np.float64
arr_with_dtype = np.array([23, 6, 3, 5, 67, 3, 31], dtype = np.int64)
print(arr_with_dtype)

# crreating array with random numbers
random_array = np.random.default_rng(1)
print(random_array.random(3))

# sorting np array
arr1.sort()
print(arr1)

# concatenating np arrays (two or more)
print(np.concatenate((arr1, arr0)))

# getting attributes of np array
nd_array = np.array([[[1,2,3,4,5],[6,7,8,9,10]], [[1,2,3,4,5],[6,7,8,9,10]], [[1,2,3,4,5],[6,7,8,9,10]]])
print(nd_array)

print(nd_array.ndim) # printing dimensions of array

print(nd_array.size) # size of array

print(nd_array.shape) # shape of array

# slicing is same as lists
print(arr1[2:5])

print(arr1[:])

print(arr1[3:])

print(arr1[-2:])

print(arr1[:-2])

print(arr1[arr1 > 10]) # slicing from patterns

print(nd_array[1,0,2]) # accessing elements in nd array

print(arr1[(arr1 > 5) & (arr1 < 55)])

# operations on array

# sum of elements
print(arr1.sum())

# sum of 2 arrays
print(arr1 + arr2)

# sum of elements on axis
print(nd_array.sum(axis=2))

print(arr1 + 5) # sum of 5 and every element of array

# other operations are max, min
print(arr1.min(), arr1.max())

# printing unique values from array, repitations will be ignored
print(np.unique(nd_array))

# printing unique values & their indices from array, repitations will be ignored
print(np.unique(arr2, return_index=True))

# printing unique values & their counts from array, repitations will be ignored
print(np.unique(nd_array, return_counts=True))

print(arr1.reshape(2,3).transpose()) # transposing a matrix

print(np.flip(arr1)) # reversing array


# plotting np array on graph
import matplotlib.pyplot as plt
plt.plot(arr2)
plt.show()

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')