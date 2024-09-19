# Задача 4. Модуль для проверки даты
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в
# формате DD.MM.YYYY Функция возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна. Для простоты договоримся, что год
# может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999
# года) действует Григорианский календарь. Проверку года на високосность
# вынести в отдельную защищённую функцию.

def checkdate(datestr):

    def visyear(year):
        """
        Возвращает True, если год високосный, иначе False.
        Аргументы:
        year -- год для проверки
        Возвращает:
        True, если год високосный; False в противном случае
        """

        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if len(datestr) != 10:
        return False

    datelist = datestr.split('.')
    if len(datelist) !=3:
        return False

    try:
     day, month, year = map(int, datelist)
    except ValueError:
        return False

    if 31<day<0:
        print (day,'day error')
        return False
    if 31<month<0:
        print ('month error')
        return False
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        if visyear(year) and day > 29:
            return False
        elif not visyear(year) and day > 28:
            return False

    # Если все проверки пройдены, дата валидна

    return True



if __name__ == '__main__':
    print(checkdate('21.12.2007'))