def finish_file(file_name):
    file_list = {}
    for name in file_name:
        with open(name, encoding='utf-8') as file:
            strok = 0
            for line in file:
                strok += 1
        file_list[name] = strok

    sorted_values = sorted(file_list.values())
    sorted_dict = {}

    for i in sorted_values:
        for k in file_list.keys():
            if file_list[k] == i:
                sorted_dict[k] = file_list[k]

    return sorted_dict


def total_file():
    with open('4.txt', 'at', encoding='utf-8') as file:
        for i, k in finish_file(['1.txt', '2.txt', '3.txt']).items():
            with open(i, encoding='utf-8') as fil:
                file.write(f'{i} \n')
                file.write(f'{k} \n')

                for line in fil:
                    file.write(line)
            file.write('\n')


total_file()
               