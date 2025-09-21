
user_input = input("Enter text to write to the file: ")

try:
    with open('./File Handling and Errors/output.txt', 'w') as file1:
        write_data = file1.write(user_input)
        print(f'Data Successfully added to the output.txt')
except FileNotFoundError:
    print(f"your File does not exist")
    

additional_data = input("enter additional data to append to  the file: ")
try:
    with open('./File Handling and Errors/output.txt', 'a') as file1:
        append_data = file1.write('\n'+ additional_data)
        print("Data successfully appended")

except FileNotFoundError:
    print(f'Your File does not exist')
    

try:
    file1 = open('./File Handling and Errors/output.txt', 'r')
    print("Final content of the file: ")
    for data in file1:
        print(data.strip())
    file1.close()
except FileNotFoundError:
    print(f"Your file does not exist")
finally:
    print('you learned the concept very well !')
    