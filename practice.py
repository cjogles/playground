# def checkFermat(a, b, c, n):
#     if a**n + b**n == c**n:
#         print("Holy smokes fermat was wrong!")
#     else:
#         print("Nope that doesn't work")

# print(checkFermat(2, 2, 2, 3))
### create a list
new_list = []
print(type(new_list))
new_list.append(2)
print(new_list)
new_list[0] = 1
print(new_list[0])
new_list.append(2)
new_list.append(4)
new_list.append(6)
new_list.append(7)
for x in new_list:
    print(x)
