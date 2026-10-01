#5] Remove duplicates from list
list=(10,20,40,34,20,10,45,40)
d_list=[]
for i in list:
    if i not in d_list:
        d_list.append(i)
    print(d_list)

a=[10,20,40,34,20,10,45,40]
print(set(a))