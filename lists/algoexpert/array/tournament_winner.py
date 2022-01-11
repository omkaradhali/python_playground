def tournamentWinner(competitions, results):
    result = ""

    score_card = {}

    for index, item in enumerate(competitions):
        print(index)
        if results[index] == 0:
            if item[1] in score_card:
                score_card[item[1]] += 3
            else:
                score_card[item[1]] = 3
        else:
            if item[0] in score_card:
                score_card[item[0]] += 3
            else:
                score_card[item[0]] = 3

    max_value = 0

    for key, value in score_card.items():
        if value > max_value:
            max_value = value
            result = key

    return result


if __name__ == "__main__":
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"],
    ]

    result = [0, 0, 1]

    print(tournamentWinner(competitions, result))
