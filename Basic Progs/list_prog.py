# Reading a file and then splits words and prints them in ascending order without any repeatation of words.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for l in line.split():
        if l in lst: continue
        lst.append(l)
    
lst.sort()
print(lst)