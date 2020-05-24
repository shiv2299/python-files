import sklearn as np
x = "Yagnesh "
y = "Patil"
z = x + y
try:
    x = int(x)
    print(z)
except:
    print('Invalid conversation done here')
    x = 10
print("int of x:", x)