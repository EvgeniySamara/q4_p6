# Задание 1. Модуль для подсчета количества повторений слов
# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений
# в списке.


def w_count(wlist):
    wdict = dict()
    for word in wlist:
        if word in wdict:
            wdict[word]+=1
        else:
            wdict[word] = 1
    return wdict


if __name__=='__main__':
    print(w_count(['apple', 'banana', 'apple','orange']))
    print('from module')