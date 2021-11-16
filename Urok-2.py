# Задача-1:
age = 18
user_age = int (input('Сколько вам лет?'))
if user_age >= age:
    print('Добро пожаловать')

else:
    print('Доступ закрыт')

# Задача-2:
user_answer = input('Чет или нечет?\n')
if user_answer == 'чет':
    print('0 2 4 6 8 10 12 14 14 16 18 20')
elif user_answer == 'нечет':
    print('1 3 5 7 9 11 13 15 17 19')
else:
    print('Я не понимаю, что вы от меня хотите?')

# Чётные
i = 0
my_list = []
while i < 21:
    if i % 2 == 0:
        my_list.append(i)
    i = i + 1
print(my_list)

# Нечётные
i = 0
my_list = []
while i < 20:
    if i % 2 == 0:
        my_list.append(i)
    i = i + 1
print(my_list)

# Чётные
my_list = []
for i in range(0, 21, 2):
    my_list.append(i)
print(my_list)

# Нечётные
my_list = []
for i in range(0, 20, 2):
    my_list.append(i)
print(my_list)

# Задача 3
x = 58375
a = -1
while x > 10:
    b = x % 10
    x //= 10
    if b > a:
        a = b
print(a)