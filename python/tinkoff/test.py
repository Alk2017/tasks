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
