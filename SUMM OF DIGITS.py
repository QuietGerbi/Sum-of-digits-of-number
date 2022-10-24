number = int(input('Введите число'))
summ_of_digits = 0
while number != 0:
    summ_of_digits += number % 10
    number //= 10
print(f'Сумма цифр данного числа равна {summ_of_digits}')