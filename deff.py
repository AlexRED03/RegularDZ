import re
from collections import OrderedDict


def rename(contacts_list):
    pattern_1 = r"(\+7|8|7)?\s*\(?(\d{3,5})\)?(\s*|[-])(\d{1,3})[- ]?(\d{2})[- ]?(\d{2})( |,)?(\(?)(доб.[ ]\d{4})?\)?"
    new_pattern_1 = r'+7 (\2) \4-\5-\6,\9'

    for i in contacts_list:
        i[5] = re.sub(pattern_1, new_pattern_1, i[5])
        name_list = i[0].split()
        name_list2 = i[1].split()

        if len(name_list) == 1:
            i[0] = i[0]
            if len(name_list2) == 2:
                i[2] = name_list2[1]
                i[1] = name_list2[0]
        elif len(name_list) == 2:
            i[1] = name_list[1]
            i[0] = name_list[0]
        elif len(name_list) == 3:
            i[2] = name_list[2]
            i[1] = name_list[1]
            i[0] = name_list[0]



def d21 (contacts_list):
    a = 0
    while a <= len(contacts_list):
        j = 1 + a
        while j <= len(contacts_list) - 1:
            if contacts_list[j][0] == contacts_list[a][0] and contacts_list[j][1] == contacts_list[a][1]:
                r = contacts_list[j]
                for g in range(7):
                    if contacts_list[a][g] != contacts_list[j][g]:
                        contacts_list[a][g] = max(contacts_list[j][g], contacts_list[a][g])
                contacts_list.remove(r)
            j += 1
        a += 1
