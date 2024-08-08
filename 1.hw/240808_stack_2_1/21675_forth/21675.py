import sys
sys.stdin = open('input.txt')


# 후위표기식을 계산해주는 함수
def calculator(data):
    stack = []

    for d in data:
        if d.isdecimal():                   # d가 숫자면
            stack.append(int(d))            # int 변환해서 스택에 넣어라
        elif d == '.':                      # d가 점이고
            if len(stack) == 1:             # 스택에 남은 숫자가 하나면
                return int(stack.pop())     # 결과 리턴 (정상 완료)
            else:                           # 스택에 남은 숫자가 하나가 아니면
                return 'error'              # 에러 리턴
        else:                               # d가 숫자도 점도 아닐 때 (=연산기호)
            if len(stack) >= 2:             # 스택에 숫자가 2개 이상이면
                n1 = stack.pop()            # 순서대로 pop해서
                n2 = stack.pop()
                if d == '+':                # 연산 진행하고
                    result = n2 + n1
                elif d == '-':
                    result = n2 - n1
                elif d == '*':
                    result = n2 * n1
                elif d == '/':
                    result = n2 / n1
                stack.append(result)        # 연산 결과값 다시 스택에 넣기

            else:                           # d가 숫자도 .도 아닌데 스택에 숫자가 2개 미만이면
                return 'error'              # 에러 리턴


T = int(input())

for tc in range(1, T+1):
    data = input().split()

    print(f'#{tc}', calculator(data))