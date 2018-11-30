"""
def HelloCycle(k):
    stroka = str('Hello world')
    i=0
    while i < k:
        print(stroka)
        i+=1
n=int(input())
HelloCycle(n)

####
def kek(j, o, m):
    global g
    if m=='+':
        g=j+o
        print(g)
    elif m=='-':
        g=j-o
        print(g)
    elif m=='*':
        g=j*o
        print(g)
    elif m=='/':
        g=j/o
        print(g)
    else:
        print('Неизвестная операция опсоса')

u=str(input())
kek(5, 7, u)

###########
def visoc_god(num):
    if num%4 == 0:
        print("true")
    else:
        print("Невисокосный")

n=int(input("Введите год: "))
visoc_god(n)
###########
def visoc_god_true(num):
    if num%4:
        print("Невисокосный")
    else:
        print("Високосный")

n=int(input("Введите год: "))
visoc_god_true(n)
###############
import math as mt
def square(side):
    global array
    p=side*4
    s=side**2
    diag=mt.sqrt(3)*side
    array=p,s,diag
    return print(tuple(array))

square(3)

print(array)
###############
def season(month):

    if month in (12, 1, 2):
        return print("зима")
    elif month in (3, 4, 5):
        return print("весна")
    elif month in (6, 7, 8):
        return print("лето")
    elif month in (9, 10, 11):
        return print("осень")

season(4)
"""

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