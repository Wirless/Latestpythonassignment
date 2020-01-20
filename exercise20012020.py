


def printit(string,count):
	for idx in range(count):
		print(string)

printit("Hello",5)

def powerof():
	num = int(input("please input a number: "))
	return num**5
	
hey = powerof()
print("Power of your number is: "+str(hey))

def centrifugal(m,r,v):
	return m*((v**2)/r)

callme = centrifugal(5,6,3)

print("Centrifugal value of m5 r6 v3 is :" + str(callme))


def takenumbers():
	list = ''
	while True:
		nums = int(input("enter number: "))
		if nums != [0-9]:
			break
		else:
			list.append(num)
	for num in range(list):
		print(list[num])
		
# takenumbers() todo
