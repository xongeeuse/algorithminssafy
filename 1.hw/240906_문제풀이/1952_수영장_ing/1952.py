import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    day, month, three_month, year = map(int, input().split())
    data = list(map(int, input().split()))

    print(day, month, three_month, year)
    print(data)