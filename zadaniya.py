print('1 задача. Поработайте с переменными....')
day = (input('День рождения: '))
if day.isdigit() and int(day)>0:
    day = int(day)
else:
    print('Ошибка! Введите цифры!')
if not day:
    print('Заполните день')

month = (input('Месяц рождения: '))
if month.isdigit() and int(month)>0:
    month = month
else:
    print('Ошибка! Введите цифры!')
if not month:
    print('Заполните месяц')

god = (input('Год рождения: '))
if god.isdigit() and int(god)>0:
    god = int(god)
else:
    print('Ошибка! Введите цифры!')
if not god:
    print('Заполните год')
import datetime
god2 = int(datetime.datetime.today().strftime('%Y'))
day2 = int(datetime.datetime.today().strftime('%d'))
segodnya = datetime.datetime.today()
vozrast = (god2 - int(god))
print('Вам', vozrast, 'лет')

day3 = int(int(day) - day2)
if day3 % 10 == 1:
    day4 = 'день'
elif 1 < day3 % 10 < 5:
    day4 = 'дня'
else: day4 = 'дней'

print('Дата рождения:', day, month, god)
print('Ваш день рождения через', day3, day4)
print('Далее 2 задача. Пользователь вводит время в секундах...')
# 2 задача
secundy = int(input('Введите секунды: '))
chas = secundy // 3600
min = (secundy // 60) % 60
sec = secundy % 60
print(str(chas)+':'+str(min)+':'+str(sec))

print('Далее 3 задача')
# 3 задача
chislo = int(input('Введите число: '))
vtoroe_chislo = (chislo * 10) + chislo
tretye_chislo = (vtoroe_chislo * 10) + chislo
resultat = chislo + vtoroe_chislo + tretye_chislo
print (chislo, '+', vtoroe_chislo, '+', tretye_chislo, '=', resultat)
print('Далее 4 задача')
# 4 задача
user_chislo = int(input('Введите второе число: '))
user_chislo2 = -1
while user_chislo > 10:
    user_chislo3 = user_chislo % 10
    user_chislo //= 10
    if user_chislo > user_chislo2:
        user_chislo2 = user_chislo3
print('Самая большая цифра: ', user_chislo2)
print('Далее 5 задача')
# 5 задача
ukazji_vyruchku = int(input('Укажите выручку: '))
ukazji_izderjki = int(input('Укажите издержки: '))
pribyl = ukazji_vyruchku - ukazji_izderjki
print('Ваша прибыль составляет ', pribyl, 'руб.')

print('Далее 6 задача')
# 6 задача Спортсмен занимается ежедневными пробежками
den = (input('Введите начальный день: '))
kilometer = int(input('Введите начальный километр: '))
maximum_km = int(input('Введите конечный километр, на который собираетесь пробежать: '))
procent = int(input('Введите % который планируете увеличить клиометр пробежки, пока не пробежите более {} км: '.format(maximum_km)))

result = (kilometer / 100) * procent
while result < maximum_km:
    den = int(den) + 1
    result = result + result
    if result > maximum_km:
        new_result = result - maximum_km
        print('На ', den, 'й день пробежите на', result, 'км, то есть на {:.2f}'.format(new_result), 'км больше запланированного')
    else:
        print('На ', den, 'й день пробежите больше изначальных км на', result, 'км')
