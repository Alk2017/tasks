def check_winner(list_numbers):
    petya_score = 0
    vasya_score = 0
    while len(list_numbers) != 0:
        current_round = list_numbers[:3]
        petya_score += current_round[0]
        vasya_score += current_round[1]
        if current_round[0] < current_round[1]:
            petya_score += current_round[2]
        else:
            vasya_score += current_round[2]
        list_numbers = list_numbers[3:]
    if petya_score > vasya_score:
        print("Petya")
    elif petya_score < vasya_score:
        print("Vasya")
    else:
        print("Error")


if __name__ == '__main__':
    # count = int(input())
    # numbers = list(map(lambda i: int(i), input().split()))
    count = 3
    numbers = [1, 4, 2]
    check_winner(numbers)
