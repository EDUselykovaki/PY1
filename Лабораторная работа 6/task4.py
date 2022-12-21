import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_N) -> list[dict]:
    # TODO реализовать конвертер из csv в json
    data=[]
    with open(file_N, 'r')  as f:
        for line in f:
            data.append(line[:-1])
    data_z=data[0:1][0].split(sep=",")
    data_m=data[1:]
    data_all=[]
    for i in data_m:
        slovo = dict(zip(data_z, i.split(sep=",")))
        data_all.append(slovo)
    return(data_all)


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
