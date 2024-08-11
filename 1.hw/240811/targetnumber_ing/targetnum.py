def solution(numbers, target):
    answer = 0
    current_sum = 0

    while numbers:
        for i in range(len(numbers)):
            temp = numbers.pop()
            current_sum += temp
    if current_sum == target:
        answer += 1
    else:
        solution(numbers + [-temp], target)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))        # 5
