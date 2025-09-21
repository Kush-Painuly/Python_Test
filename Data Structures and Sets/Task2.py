

lst = []
for i in range(1,11):
    lst.append(i)
    first_five = lst[:5]
    reverse_five = first_five[::-1]

print(f"Original list: {lst}")
print(f"First five element of the list: {first_five}")
print(f"Reverse extracted first five elements: {reverse_five}")



