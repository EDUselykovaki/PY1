def delete(list_, index=None):
 # TODO реализовать функцию удаления элемента из списка по индексу
    if index is None:
        index=-1
        list_n=list_[:-1]
        return (list_n)
    else:
        left_list = list_[:index]
        right_list = list_[(index+1):]
        list_n=left_list+right_list
        return (list_n)

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
