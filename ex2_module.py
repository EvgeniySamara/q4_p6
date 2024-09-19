# Задача 2. Модуль для удаления дублирующихся подряд символов
# Напишите модуль с функцией, которая принимает строку и возвращает строку с
# удаленными дублирующимися подряд идущими символами. Например, строка
# "aaabbcccaa" должна быть преобразована в "abca".

def removedbl(st):
    stlist = list(st)
    res =stlist[0]
    for i in range(1,len(stlist)):
        if stlist[i]!=stlist[i-1]:
            res+=stlist[i]
        else:
            continue
    return res

if __name__ == "__main__":
    print(removedbl('aabbccaa'))
