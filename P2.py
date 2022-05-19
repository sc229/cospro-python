def solution(price, grade):
    answer = 0
    price = 10000
    if grade == "S":
        answer = (price * 0.95)
    elif grade == "G":
        answer = (price * 0.9)
    elif grade == "V":
        answer = (price * 0.85)
    return answer

silver = solution(10000, "S")
gold = solution(10000, "G")
vip = solution(10000, "V")

print(silver, gold, vip)