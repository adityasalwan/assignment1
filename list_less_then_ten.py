list = [2,4,5,3,6,8,9,7,10,34,23,45]

num = int(input("enter the number : "))

new_list = []

for i in list :
    if i < num :
        new_list.append(i)


print(new_list)

