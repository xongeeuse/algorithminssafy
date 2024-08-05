# sudoku

sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
n = 9

for t in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    r = 0

    for i in range(n):
        a, b = [], []

        for j in range(n):
            a.append(arr[i][j])
            b.append(arr[j][i])

        if (i-1) % 3 == 0 and (j-1) % 3 == 0:
            s = [arr[i][j]]

            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]

                s.append(arr[ni][nj])

            if sorted(a) == sorted(b) == sorted_arr:
                result += 1

        if result == 18 : r = 1

        print(f'#{t} {r}')