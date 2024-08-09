# powerset을 구하는 백트래킹 알고리즘
def backtrack(a, k, n):                     # a: 주어진 배열, k: 결정할 원소, n: 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a, k)              # 답이면 원하는 작업을 한다
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

def construct_candidates(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2

def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end=' ')
    print()

MAXCANDIDATES = 2           # 후보군 개수
NMAX = 4                    # 몇 개의 원소에 대한 부분집합
a = [0] * NMAX              #
num = [1, 2, 3, 4]
backtrack(a, 0, NMAX)