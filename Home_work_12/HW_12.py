import json

with open('E:/py/Home_works2/Home_work_12/HW.json', 'r') as file:
    dict_data = json.load(file)
    print(dict_data)
    list_ = []

    # dict_ = {1: 2, 5: 9}
    # tuple_ = ("Alex", "Mark")
    # dict_[tuple_[0]] = tuple_[1]
    # print(dict_)

    for i in dict_data['employee']:
        for k, v in dict(i).items():
            list_.append((k, v))

        # t = (k, v)
        # list_.append(t)
    #     list_types.append(v)
    #     list_.append(k)
    #     for i in list_types:
    #         if type(i).__name__ == 'int':
    #             list_int.append(k)
    #         elif type(i).__name__ == 'str':
    #             continue
print(list_)

# for i in list_:
#     dict_type_value = dict(zip(type(i).__name__, i))
# print(type_value)
    #     print(v)
    # print(type_set)

