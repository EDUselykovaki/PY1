def get_count_char(str_):
     # TODO посчитать количество каждой буквы в строке в аргументе str_
     alfavit_dict = {}
     DEFAULT_COUNT = 0
     str_mal=str_.lower()

     for grade in str_mal:

               if grade.isalpha():
                    alfavit_dict[grade] = alfavit_dict.get(grade, DEFAULT_COUNT) + 1

     return (alfavit_dict)

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
