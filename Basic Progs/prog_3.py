largest = None
smallest = None
while True:
	num = input('Enter a number:')
	if num == 'done': break
	try:
		num = int(num)
		if largest is None and smallest is None:
			largest = smallest = num
		if num >  largest:
			largest = num
		if num < smallest:
			smallest = num
	except:
		print('Invalid number')
print('Maximum is', largest)
print('Minimum is', smallest)
