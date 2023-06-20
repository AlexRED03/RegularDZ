from pprint import pprint
import csv
from deff import rename, d21

with open("phonebook_raw.csv", encoding="utf-8") as f:
    g = csv.reader(f, delimiter=",")
    contacts_list = list(g)
rename(contacts_list)
d21(contacts_list)



with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)