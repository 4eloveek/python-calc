kek = 1
while kek >= 1:
	print('Выберите действие')
	print('Сложение +, вычитание -, деление /, умножение *, выход из программы exit')
	x = input()
	if x == '+':
		print('Напишите первое число')
		y = int(input())
		print('Напишите второе число')
		z = int(input())
		print('Ответ:')
		print(y+z)
		print()
	if x == '-':
		print('Напишите первое число')
		y = int(input())
		print('Напишите второе число')
		z = int(input())
		print(y-z)
		print('Ответ:')
		print()
	if x =='/':
		print('Напишите первое число')
		y = int(input())
		print('Напишите второе число')
		z = int(input())
		print('Ответ:')
		print(y//z)
		print()
	if x =='*':
		print('Напишите первое число')
		y = int(input())
		print('Напишите второе число')
		z = int(input())
		print('Ответ:')
		print(y*z)
		print()
	if x == 'exit':
		exit('Спасибо за использование!')