# TODO Напишите функцию find_common_participants

def find_common_participants(first, second, splitter='|'):

    first_group = first.split(splitter)
    second_group = second.split(splitter)

    common_participants = list(set(first_group).intersection(second_group))

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print("Общие участники:", find_common_participants(participants_first_group, participants_second_group))