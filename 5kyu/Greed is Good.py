def score(dice):
    scores = 0
    stack = []
    for x in dice:
        stack.append(x)
        i = stack.count(x)
        if x in [2, 3, 4, 6] and i == 3:
            scores += int(str(x) + '0' * 2)
            stack.clear()
        if x in [1, 5] and 0 < i < 3:
            if x == 1:
                scores += 100
            if x == 5:
                scores += 50
        if x in [1, 5] and i == 3:
            stack.clear()
            if x == 1:
                scores += 1000 - 200
            if x == 5:
                scores += 500 - 100
    return scores