import time

def first_in_row(nums, i):
    while i - 1 >= 0 and nums[i] == nums[i - 1]:
        i -= 1
    return i


def last_in_row(nums, i):
    size = len(nums)
    while i < size - 1 and nums[i] == nums[i + 1]:
        i += 1
    return i


def find_first(left, right, nums, cost):
    if left > right:
        return -1
    mid = (left + right) // 2
    if nums[mid] == cost:
        return first_in_row(nums, mid)+1
    elif nums[mid] > cost:
        prev = first_in_row(nums, mid) - 1
        if nums[prev] < cost or prev == -1:
            return first_in_row(nums, mid)+1
        elif nums[prev] == cost:
            return first_in_row(nums, prev)+1
        else:
            return find_first(left, first_in_row(nums, prev), nums, cost)
    else:
        return find_first(last_in_row(nums, mid) + 1, right, nums, cost)


# def find_binary(left, right, nums, cost):
#     if left >= right:
#         return -1
#     mid = (left + right) // 2
#     if nums[mid] == cost:
#         return mid
#     elif nums[mid] > cost:
#         return find_binary(left, mid, nums, cost)
#     else:
#         return find_binary(mid + 1, right, nums, cost)


# 3
# 1 2 4 4 4 4
# 1 3 5 6 8 9 12 13 15
# 0 1 2 3 4 5  6  7  8


if __name__ == '__main__':
    # f = open('input_resource.txt', 'r')
    # count = int(f.readline())
    # nums = [int(i) for i in f.readline().split()]
    # cost = int(f.readline())
    # count = int(input())
    # nums = [int(i) for i in input().split()]
    # cost = int(input())
    count = 1000000
    # start = 999900
    nums = [999900]*500000 + [999999]*500000
    # for i in range(100):
    #     start += i
    #     nums += [start]*count
    # count *= 100
    cost = 599951
    start_time = time.time()
    first_day = find_first(0, count-1, nums, cost)
    # print(first_day)
    second_day = find_first(first_day, count-1, nums, cost*2)
    print(f'{first_day} {second_day}')
    print("--- %s seconds ---" % (time.time() - start_time))


