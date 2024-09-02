def inorder(node):
    global result
    if node < 8:
        inorder(node * 2)
        result += tree[node]
        inorder(node * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = input()
    print(f'#{tc}', end=' ')
    for i in range(N):
        tree = list(f'{ord(data[i]):08b}')
        result = ''
        inorder(node = 1)
        print(result, end=' ')
    print()