def check_score(team_data):
    scores = {}
    for data in team_data:
        team_1 = data[0]
        team_2 = data[1]
        score_1, score_2 = map(lambda i: int(i), data[2].split(':'))
        if score_1 == score_2:
            if team_1 in scores.keys():
                scores[team_1] += 1
            else:
                scores[team_1] = 1
            if team_2 in scores.keys():
                scores[team_2] += 1
            else:
                scores[team_2] = 1
        elif score_1 > score_2:
            if team_1 in scores.keys():
                scores[team_1] += 3
            else:
                scores[team_1] = 3
            if team_2 not in scores.keys():
                scores[team_2] = 0
        else:
            if team_2 in scores.keys():
                scores[team_2] += 3
            else:
                scores[team_2] = 3
            if team_1 not in scores.keys():
                scores[team_1] = 0
    return scores


def print_table(scores, data):
    names = list(scores.keys())
    names.sort()
    max_name = max(list(map(lambda _: len(_), names)))
    sep = f'+-+{(max_name + 1)*"-"}+{"-+"*len(scores)}-+-+'
    print(sep)
    for i in range(0, len(scores)):
        games = ''
        current_team = names[i]
        for j in range(0, len(scores)):
            if i == j:
                games += 'X|'
                continue
            enemy_team = names[j]
            for d in data:
                if {current_team, enemy_team} == {d[0], d[1]}:
                    score_1, score_2 = map(lambda i: int(i),
                                           d[2].split(':'))
                    if score_1 == score_2:
                        games += 'D|'
                    else:
                        if (d[0] == current_team and score_1 > score_2 or
                                d[1] == current_team and score_1 < score_2):
                            games += 'W|'
                        else:
                            games += 'L|'
            if len(games)//2 != (j + 1):
                games += ' |'

        print(f'|{i+1}|{current_team} {(max_name - len(current_team))*" "}|'
              f'{games}{scores[current_team]}|')
        print(sep)


if __name__ == '__main__':
    count = int(input())
    input_data = []
    for _ in range(0, count):
        input_data.append(tuple(input().split(' - ')))
    team_scores = check_score(input_data)
    print(team_scores)
    print_table(team_scores, input_data)
