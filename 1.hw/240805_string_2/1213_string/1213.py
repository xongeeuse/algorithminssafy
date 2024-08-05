import sys
sys.stdin = open("input.txt", encoding='utf-8')

T = 10

for _ in range(1, T+1):
    tc = int(input())
    pattern = input()
    search_text = input()
    result = 0

    p_idx = 0       # pattern_index
    c_idx = 0       # compare_index

    while c_idx < len(search_text):
        if search_text[c_idx] != pattern[p_idx]:
            c_idx = c_idx - p_idx + 1
            p_idx = 0
            continue

        p_idx += 1
        c_idx += 1

        if p_idx == len(pattern):
            result += 1
            c_idx = c_idx - p_idx + 1
            p_idx = 0

    print(f'#{tc}', result)
