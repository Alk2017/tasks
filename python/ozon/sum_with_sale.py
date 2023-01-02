def ls_to_dict(ls):
    d = {}
    for item in ls:
        if item in d.keys():
            d[item] += 1
        else:
            d[item] = 1
    return d


def run():

    count = int(input())
    for _ in range(count):
        sum = 0
        c = input()
        purchs = [int(i) for i in input().split()]
        d_purchs = ls_to_dict(purchs)
        for p in d_purchs.keys():
            sale_count = d_purchs[p] // 3
            sum += p * (d_purchs[p] - sale_count)
        print(sum)


if __name__ == '__main__':
    run()

"""
G. Сумма к оплате (10 баллов)
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
В магазине акция: «купи три одинаковых товара и заплати только за два». Конечно, каждый купленный товар может участвовать лишь в одной акции. Акцию можно использовать многократно.

Например, если будут куплены 7
7
 товаров одного вида по цене 2
2
 за штуку и 5
5
 товаров другого вида по цене 3
3
 за штуку, то вместо 7⋅2+5⋅3
7
⋅
2
+
5
⋅
3
 надо будет оплатить 5⋅2+4⋅3=22
5
⋅
2
+
4
⋅
3
=
22
.

Считая, что одинаковые цены имеют только одинаковые товары, найдите сумму к оплате.

Неполные решения этой задачи (например, недостаточно эффективные) могут быть оценены частичным баллом.

Входные данные
В первой строке записано целое число 𝑡
t
 (1≤𝑡≤104
1
≤
t
≤
10
4
) — количество наборов входных данных.

Далее записаны наборы входных данных. Каждый начинается строкой, которая содержит 𝑛
n
 (1≤𝑛≤2⋅105
1
≤
n
≤
2
⋅
10
5
) — количество купленных товаров. Следующая строка содержит их цены 𝑝1,𝑝2,…,𝑝𝑛
p
1
,
p
2
,
…
,
p
n
 (1≤𝑝𝑖≤104
1
≤
p
i
≤
10
4
). Если цены двух товаров одинаковые, то надо считать, что это один и тот товар.

Гарантируется, что сумма значений 𝑛
n
 по всем тестам не превосходит 2⋅105
2
⋅
10
5
.

Выходные данные
Выведите 𝑡
t
 целых чисел — суммы к оплате для каждого из наборов входных данных.

Пример
входные данныеСкопировать
6
12
2 2 2 2 2 2 2 3 3 3 3 3
12
2 3 2 3 2 2 3 2 3 2 2 3
1
10000
9
1 2 3 1 2 3 1 2 3
6
10000 10000 10000 10000 10000 10000
6
300 100 200 300 200 300
выходные данныеСкопировать
22
22
10000
12
40000
1100
"""