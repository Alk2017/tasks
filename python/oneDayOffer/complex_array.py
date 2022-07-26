from collections import Counter

def run():
    line = input()
    nums = [
        int(i) for i in line.replace(',', '').replace('[', '').replace(']', '').split()
    ]
    nums_count = dict(Counter(nums))
    max_v = max(list(nums_count.values()))
    keys = []
    for k in nums_count.keys():
        if nums_count[k] == max_v:
            keys.append(k)
    keys.sort()
    print(' '.join([str(i) for i in keys]))


if __name__ == '__main__':
    run()