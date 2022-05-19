def solution(scores):
    count = 0
    for s in scores:
        if 650 <= s and s < 800:
            count += 1
        return count