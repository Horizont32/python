def age(n):
	n=int(input("input ur age: "))
	if(n>=0 and n<7):
		print("Вам в детский сад ")
	elif (n>=7 and n<18):
		print("Вам в школу")
	elif (n>=18 and n<25):
		print("Вам в профессиональное учебное заведение")
	elif (n>=25 and n<60):
		print("Вам на работу")
	elif (n>=60 and n<120):
		print("Вам предоставляется выбор")
	else:
		i=0
		while i<4:
			print("Ошибка! Это программа для людей!")
age(0)