students_amount = int(input("Montako opiskelijaa? "))
group_size = int(input("Mikä on ryhmän koko? "))

groups = students_amount // group_size

if students_amount % group_size != 0:
    groups += 1

print(f"Ryhmien maara: {groups}")
