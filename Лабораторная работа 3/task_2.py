# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sep_= ","):
    group1 = group1.split(sep_)
    group2 = group2.split(sep_)
    inter_list = set(group1).intersection(set(group2))
    inter_list = list(inter_list)
    inter_list.sort()
    return inter_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,"|"))