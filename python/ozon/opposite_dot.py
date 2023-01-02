def run():
    c = int(input())
    for _ in range(c):
        n = int(input())
        l_l = [[int(j) for j in input().split()] for _ in range(n)]
        check = l_l[0][2]
        res = [l_l[0][0], l_l[0][1]]
        l_l.remove(l_l[0])
        while n != len(res):
            next = list(filter(lambda x: x[0] == res[-1], l_l))[0]
            l_l.remove(next)
            if next[1] == res[res.index(next[0]) - 1]:
                res.append(next[2])
            else:
                res.append(next[1])
        else:
            if check != res[-1]:
                print('error')
        for i in range(n//2):
            print(f'{res[i]} {res[i+n//2]}')
        print('')



# 20.10.
if __name__ == '__main__':
    run()

"""
K. Противоположные элементы (20 баллов)
ограничение по времени на тест10 секунд
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Вам задан циклический двусвязный список целых чисел. Иными словами, заданный список замкнут в «кольцо», а для каждого его элемента вам известны его соседи (в произвольном порядке).

Список задан набором троек вида «𝑒𝑖𝑎𝑖𝑏𝑖
e
i
a
i
b
i
». Каждая такая тройка означает, что соседями элемента 𝑒𝑖
e
i
 являются элементы 𝑎𝑖
a
i
 и 𝑏𝑖
b
i
. У вас нет информации какой из этих двух элементов следующий, а какой предыдущий. Иными словами, соседи 𝑎𝑖
a
i
 и 𝑏𝑖
b
i
 заданы в соответствующей тройке в произвольном порядке.

Известно, что всего в списке чётное количество элементов.

Для каждого элемента выведите тот, который ему противоположен (то есть расположен строго напротив, если изобразить список в виде правильного 𝑛
n
-угольника).

Неполные решения этой задачи (например, недостаточно эффективные) могут быть оценены частичным баллом.

Входные данные
В первой строке входных данных записано целое число 𝑡
t
 (1≤𝑡≤104
1
≤
t
≤
10
4
) — количество наборов входных данных в тесте. Далее следуют описания наборов входных данных.

Наборы входных данных в тесте являются независимыми. Друг на друга они никак не влияют.

В первой строке набора записано чётное целое число 𝑛
n
 (4≤𝑛≤105
4
≤
n
≤
10
5
) — длина списка.

Следующие 𝑛
n
 строк содержат тройки 𝑒𝑖,𝑎𝑖,𝑏𝑖
e
i
,
a
i
,
b
i
 (1≤𝑒𝑖,𝑎𝑖,𝑏𝑖≤109
1
≤
e
i
,
a
i
,
b
i
≤
10
9
), которые обозначают, что соседями элемента 𝑒𝑖
e
i
 являются элементы 𝑎𝑖
a
i
 и 𝑏𝑖
b
i
. Гарантируется, что все 𝑛
n
 элементов списка — различные числа.

Сумма значений 𝑛
n
 по всем наборам входных данных теста не превосходит 105
10
5
.

Выходные данные
Для каждого набора выходных данных выведите 𝑛/2
n
/
2
 строк, каждая из которых должна содержать два целых числа 𝑥𝑖,𝑦𝑖
x
i
,
y
i
, которые означают, что элемент 𝑥𝑖
x
i
 расположен строго напротив элемента 𝑦𝑖
y
i
 в циклическом списке. Числа в парах и сами пары можно выводить в любом порядке.

Для улучшения читаемости ответа между ответами для наборов выходных данных можно выводить пустую строку.

Пример
входные данныеСкопировать
2
4
4 2 1
2 4 3
3 2 1
1 3 4
6
20 30 10
40 30 50
30 20 40
60 10 50
10 60 20
50 40 60
выходные данныеСкопировать
4 3
1 2

30 60
20 50
40 10
"""