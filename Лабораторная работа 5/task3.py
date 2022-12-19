def get_unique_list_numbers() -> list[int]:
 from random import shuffle
 list_numbers = list(range(-10,11,1))
 shuffle(list_numbers)
 return list_numbers[0:15]

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))