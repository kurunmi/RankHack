def nuscores(scores):
    changed = True
    size = len(scores)
    while changed:
        new = scores.copy()
        changed = False
        for i in range(1, size-1):
            if scores[i-1] > scores[i] and scores[i+1] > scores[i]:
                new[i] += 1
                changed = True
            elif scores[i-1] < scores[i] and scores[i+1] < scores[i]:
                new[i] -= 1
                changed = True
        scores = new
        new = []


if __name__ == '__main__':
    scores = [1, 6, 3, 4, 3, 5]
    print(nuscores(scores))