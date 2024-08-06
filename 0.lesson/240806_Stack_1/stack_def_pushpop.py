# 스택 push, pop 함수로 만들어보기
def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1            # push(20)
stack[top] = 20     #


def my_pop():
    global top
    if top == -1:
        print('underflow!')
        return 0
    else:
        top -= 1
        return stack[top + 1]


print(my_pop())

if top > -1:
    top -= 1
    print(stack[top + 1])