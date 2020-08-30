file_handle = open('Basic Progs/romeo.txt','r')
for line in file_handle:
    for ch in line:
        print(ch , end='')


file2 = open('Basic Progs/romeo.txt')
file_content = file2.read()
print(file_content)

dir(file2)

# Exercise
fh = open('Baic Progs/romeo.txt','r')
sum = count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence: 0.") : continue
    val = float(line[-7:])
    count = count + 1
    sum = sum + val
ans = sum/count
print("Average spam confidence:",ans)

# to check if path exists
import os.path
from os import path

path.exists('Basic Progs/mbox-short.txt')