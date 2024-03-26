first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
id_number = input("Enter ID: ")

set1 = first_name[:3]
set2 = last_name[:3]
set3 = id_number[-3:]

login_name = set1 + set2 + set3

print(login_name)