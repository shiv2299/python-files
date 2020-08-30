# illustrating tuples

tuple_1 = (1,5,8,"Yagnesh Patil")
print(tuple_1[2])
print(tuple_1)

for item in tuple_1:
    print(item,end=" ")

print()

# tuples are immutablee
# tuple_1[1] = "not applicable"  #TypeError

#adding one tuple into another tuple
tuple_1.__add__((234,5656))

#alternate tuple assignment
(x,y) = (687,"Yagnesh")
x
y

#tuples are comparable
(3,625,32) < (32,562,12)  #compares first element of both tuples, if condition is False for first elements, then it will return False, else it will return False.


# getting top 10 most used words in a file:

file_handle = open('Basic Progs/romeo.txt')
counts = dict()
for line in file_handle:
    for word in line.split():
        counts[word] = counts.get(word, 0) + 1
    
# approach 1 - traditional
lst = list()
for key, value in counts.items():
    newtup = (value, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
    print(key, value)


# approach 2 - Using list comprehension
    # List comprehension - It creates a dynamic list
print(sorted([(v,k) for k,v in counts.items()], reverse=True)[:10])