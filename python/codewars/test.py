import string


def is_pangram(s):
    al = list(string.ascii_lowercase)
    for l in s.lower():
        try:
            al.remove(l)
        except ValueError:
            pass
    return len(al) == 0


if __name__ == '__main__':
    print(is_pangram("The quick, brown fox jumps ver the lzy dog!"))
    ar = [('z', 9), ('a', 3), ('a', 2), ('b', 2), ('c', 10)]
    ar.sort(key=lambda x:(x[1], x[0]))
    print(ar)
