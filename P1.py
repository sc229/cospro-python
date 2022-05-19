def solution(shirt_size):
    answer = [0] * 6
    for s in shirt_size:
        if s == 'XS':
            answer[0] += 1
        elif s == 'S':
            answer[1] += 1
        elif s == 'M':
            answer[2] += 1
        elif s == 'L':
            answer[3] += 1
        elif s == 'XL':
            answer[4] += 1
        elif s == 'XXL':
            answer[5] += 1
    return answer
shirt_size = ["XS", "S", "XXL", "L", "L", "XS", "XL"]
print(solution(shirt_size))