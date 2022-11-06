import random

#Возвращает список цифр из числа
def getDigits(num):
	return [int(i) for i in str(num)]
	

#Проверка на дубликаты 
def noDuplicates(num):
	num_li = getDigits(num)
	if len(num_li) == len(set(num_li)):
		return True
	else:
		return False


#Генерирует 4-ех значное число
def generateNum():
	while True:
		num = random.randint(1000,9999)
		if noDuplicates(num):
			return num


#Проверка на количество коров и быков
def numOfBullsCows(num,guess):
	bull_cow = [0,0]
	num_li = getDigits(num)
	guess_li = getDigits(guess)
	
	for i,j in zip(num_li,guess_li):
		
		if j in num_li:
		
			if j == i:
				bull_cow[0] += 1
			
			else:
				bull_cow[1] += 1
				
	return bull_cow
	
#Ввод количества попыток
num = generateNum()
tries =int(input('Введите количество попыток: '))

#Игровой модуль
while tries > 0:

	guess = input("Введите свои догадки: ")
	try:
	    guess = int(guess)
	except:
	    print("Вы ввели не число!")
	    
	if not noDuplicates(guess):
		print("Число не должно содержать повторяющихся цифр. Давайте еще раз!.")
		continue
	if guess < 1000 or guess > 9999:
		print("Введите только 4-ех значное число. Давайте еще раз!")
		continue
	bull_cow = numOfBullsCows(num, guess)
	print(f"{bull_cow[0]} быки, {bull_cow[1]} коровы")
	tries -=1
	
	if bull_cow[0] == 4:
		print("Число угадано!")
		break
else:
	print(f"Увы, но закончились попытки :(. Загаданным числом было {num}")
