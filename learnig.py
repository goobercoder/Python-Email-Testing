list1 = [1, 2, 3]
list2 = [3, 2, 1]
list3 = [2, 1, "poop"]
list4 = ["goog", 3, "poop"]
list2d1 = [list1, list2, list3]
list2d2 = [list3, list1, list2]
list2d3 = [list4, list3, list1]

list3d = [list2d1, list2d2, list2d3]

print(list3d[2][0][0], end= " ")
print(list3d[2][0][2], end= " and then fuck you\n")