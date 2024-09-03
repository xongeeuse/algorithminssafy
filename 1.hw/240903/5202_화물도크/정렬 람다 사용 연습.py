data_list = ['but','i','wont','hesitate','no','more','no','more','it','cannot','wait','im','yours']

for index in range(len(data_list)) :
    data_len = len(data_list[index])
    data_list[index] = (data_list[index], data_len)

data_list.sort(key = lambda x :(x[1], x[0]))
print(data_list)