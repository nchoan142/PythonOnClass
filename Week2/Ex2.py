dict_subjects = {
    "History" : "Lich su",
    "Geography" : "Dia ly",
    "Physics" : "Vat ly",
    "Maths" : "Toan",
    "Biology" : "Sinh hoc",
    "Literature " : "Van",
    "Chemistry" : "Hoa hoc",
    "English" : "tieng Anh",
    "Music" : "Am nhac",
    "Science" : "Khoa hoc"
}
# print("Before update: ")
# print(dict_subjects)

# key = str(input("Enter key: "))
# value = str(input("Enter value: "))

# dict_subjects[key] = value
# print("After update: ")
# print(dict_subjects)

# print(len(dict_subjects))

# dict_subjects_copy = dict_subjects.copy()
# print(dict_subjects_copy)

check_key_th = False
for x in dict_subjects.keys():
    if x == "th":
        check_key_th = True

if check_key_th == True:
    print("Key 'th' exists in dictionary")
else:
    print("Key 'th' does not exist in dictionary")

print(dict_subjects.get("kd"))

dict_subjects.update({
    "subject1" : "subject1_name",
    "subject2" : "subject2_name",
    "subject3" : "subject3_name"
})

print(dict_subjects)