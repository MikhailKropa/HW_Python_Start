# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = int(input("Введите номер билета: "))

if ticket > 999999 or ticket < 100000:
    print('Номер билета не шестизначный')

sum1 = 0
while ticket > 1000:         # цикл отрабатывает первые три цифры числа
     sum1 = sum1 + ticket % 10
     ticket = ticket // 10

number = ticket % 1000  # число, равное первым трем цифрам
sum2 = 0

while number > 0:                 # цикл отрабатывает последние три цифры числа
     sum2 = sum2 + number % 10
     number = number // 10

if sum1 == sum2:
    print('yes')
else:
    print('no')
