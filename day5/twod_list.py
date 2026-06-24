# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix)

# print(matrix[2])
# print(matrix[0])
# print(matrix[1])



# print(matrix[1][0])

lst_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



for row in range(3):
    # current_row = lst_2d[row]
    for col in range(3):
        # item = current_row[col]
        item = lst_2d[row][col]
        if row==1 and col==0:
          print(lst_2d[row][col])

# row=0
# col=1
# print(lst_2d[row][col])
# print(lst_2d[row])
# for i in range(len(lst_2d)):
#  print(lst_2d[i])



# for row in range(3):
#     row = lst_2d[row]
#     for col in range (3):
#         item = row[col]
#         print(item)

# nested_list = ['abc',
#                [1, 3, 4],
#                [2, 5, 6],
#                3
#                ]

# a = nested_list [2] #[2, 5 , 6]
# print(a[2]) #6

# print(nested_list[1][2])


# lst2 = [5,6,7]
# lst.append(lst2)
# print(lst)

# lst2.extend(lst2)
# print(lst)

# lst2 = [2, 3, 4, 1, 8, 4]
# sorted_lst = sorted(lst2)