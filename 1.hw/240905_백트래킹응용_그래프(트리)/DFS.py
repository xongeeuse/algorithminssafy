# 데이터가 트리로 주어지는 경우 DFS
tree = {'1' : ['2', '3'],
        '2' : ['4', '5'],
        '3' : ['6'],
        '4' : ['7']}

def dfs(tree, node):

    print(node)

    if node not in tree:
        return

    for child in tree[node]:
        dfs(tree, child)


dfs(tree, '1')



# 데이터가 그래프로 주어지는 경우 DFS