

student_dict = {'John':56, 'Alice':98, 'Mike': 78, 'Suzi': 99, 'Cody': 100}
print(student_dict)

user_inp = input("Enter the student name to retrieve marks: ")

if user_inp in student_dict:
    print(f"{user_inp}'s marks: {student_dict[user_inp]}")
else:
    print("Student not found")
    
