def check_str(input_string):
    code_list = [ord(ch) for ch in input_string]
    if len(code_list) == 4:
        if (code_list[0] != code_list[1] and code_list[0] + code_list[1] ==
                code_list[2] + code_list[3]):
            return "Yes"
        if (code_list[0] != code_list[2] and code_list[0] + code_list[2] ==
                code_list[1] + code_list[3]):
            return "Yes"
    return "No"


if __name__ == '__main__':
    count = int(input())
    for _ in range(0, count):
        print(check_str(input()))
