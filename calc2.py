help1 = input("Добро пожаловать в наш калькулятор введите 1 чтобы включить функцию помощь нажмите 0 чтобы ее         не включать")
if help1 == "1":
	print("1 Введите первое число")
	print("2 Нажмите 'Enter'")
	print("3 Введите оператор")
	print("4 Нажмите 'Enter'")
	print("5 Введите Второе число")
	print("6 Нажмите 'Enter' чтобы посмотреть на результат ")
else:
	print("Спасибо что заглянули в наш калькулятор")
# d = input("Нажмите 1 что бы не показывать больше это сообщение ")
# if d == 1:
# 	delete (help1)	
num1 = int(input("Введите 1 число  "))
z = input("Введите оператор (*, /, - ,+ ,% ,# - Корень из n ,^ - В степень n ,! - Факториал)                      ")	
num2 = int(input("Введите 2 число  "))

if z == "+":
	print(num1 + num2)
elif z == "!":
	fac = 1 
	i = 0 
	while i < num1:
		i += 1
		fac = fac * i 
	fac2 = 1 
	i = 0 
	while i < num2:
		i += 1
		fac2 = fac2 * i 
	print("Факториал 1 числа:", fac , ", и факториал 2 числа:", fac2)
elif z == "-":
	print(num1 - num2)
elif z == "%":
	print(num1 * (num2 / 100))
elif z == "*":
	print(num1 * num2)
elif z == "#":
	print(num1 ** (1 / num2))
elif z == "^":
	print(num1 ** num2)
# elif num2 == "0":
# 	z == "/"
# 	print("Деление на ноль!")
elif z == "/":
	print(num1 / num2)	
else:
	print ("Пиши правильно!")
print("Спасибо что воспользовались нашим калькулятором")

