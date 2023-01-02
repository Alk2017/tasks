import requests


def mew_request(names):
    r = requests.request(
        method='MEW',
        url='http://127.0.0.1:7777/',
        headers={
            "X-Cat-Variable": f"{', '.join(names)}"
        }
    )
    print(r)
    print(r.headers)
    return r.headers.get('x-cat-value').split(', ')


def except_list_from_list(ls1, ls2):
    res_ls = list(ls1)
    for n in ls2:
        if n in ls1:
            res_ls.remove(n)
    return res_ls


def gen_four_answer_comb():
    res = []


def gen_permutations(count_words, store=None):
    store = store or []
    if len(store) == count_words:
        return


def gen_numbers(n: int, m: int, prefix=None):
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for i in range(n):
        prefix.append(i)
        gen_numbers(n, m - 1, prefix)
        prefix.pop()


if __name__ == '__main__':
    # name1 = input()
    # name2 = input()
    # name3 = input()
    # name4 = input()
    name1 = 'Window'
    name2 = 'Bird'
    name3 = 'Food'
    name4 = 'Human'

    res = []
    gen_numbers(4, 4)
    # req1 = mew_request([name1, name2])
    # req2 = mew_request([name1, name2, name3])
    # req3 = mew_request([name2, name3, name4])
    #
    # if req2 == req3:
    #     count = len(set(req1 + req2 + req3))
    #     if count == 3:
    #         pass
    #
    #
    #     res.append(except_list_from_list(req2, req1)[0])
    #     res.append(except_list_from_list(req3, req2)[0])
    #     res.insert(0, except_list_from_list(req3, res)[0])
    #     res.insert(0, except_list_from_list(req1, res[0])[0])
    #
    # else:
    #     res.append(except_list_from_list(req2, req3)[0])
    #     res.append(except_list_from_list(req1, res)[0])
    #     res.append(except_list_from_list(req2, res)[0])
    #     res.append(except_list_from_list(req3, res)[0])
