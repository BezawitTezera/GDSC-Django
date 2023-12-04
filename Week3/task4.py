sum = 0
count = 0
for i in range(2,51,2):
    sum+=i
    if i % 3 == 0:
        count += 1
        print("Three")
    elif i % 5 == 0:
        count += 1
        print("Five")
    else:
        print(i)
print(f"The sum of the numbers is {sum}. And count of numbers replaced by 'Three' or 'Five' are {count}.")
