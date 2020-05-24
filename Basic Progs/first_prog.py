print("Printing using print function in python")

x = input('enter value of x:')

try:
	if int(x) < 5:
		print('x is less than 5')
	elif int(x) == 10:
		print('x is just same as 10')
	elif int(x) == 20:
		print('another uncessary elif is here')
	else:
		print('nothing! x is greater than 5')
	for i in range(5):
		print('*\t')
except:
	print('enter valid number x!')