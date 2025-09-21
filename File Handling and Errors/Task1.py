

## Reading the data of a file line by line 

try:
    file1 = open('./File Handling and Errors/sample.txt', 'r')
    for data in file1:
        print(data)
    file1.close()
except FileNotFoundError:
    print(f"your {file1} does not exist")
finally:
    print('You learned the concept very good !')