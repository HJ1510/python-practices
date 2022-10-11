def solution(n):
    n = str(n) # 정수를 문자로(리버스하려고) print(n) = "123"
    answer = list(n) # n = ["1", "2", "3"]
    answer.reverse() #["3", "2", "1"]
    for el in range (0, len(answer)):
        answer[el] = int(answer[el])
    return answer
print(solution(12345))
print(solution(123))
print(solution(1234))
