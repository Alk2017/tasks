import requests as requests


def run():
    host = input()
    port = input()
    a = input()
    b = input()
    res = requests.get(
        url=f'{host}:{port}/',
        params={'a': a, 'b': b}
    )
    json_res = res.json()
    nums = [line for line in json_res]
    print(sum(nums))


def run2():
    # host = input()
    # port = input()
    # a = input()
    # b = input()
    host = 'https://gorest.co.in/public/v2/posts'
    a = 'hello'
    r = requests.get(
        url=f'{host}/',
        # url=f'{host}:{port}/',
        # params={'q': a}
    )
    json_res = r.json()
    nums = [line['id'] for line in json_res]
    print(sum(nums))
    print(r.status_code)


if __name__ == '__main__':
    run()
