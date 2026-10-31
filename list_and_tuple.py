initial_list = input("Enter sequence of numbers :")
converted_list = initial_list.split(",")
number_list = []
for i in converted_list:
    cleaned = i.strip()
    number_list.append(int(cleaned))
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)
Total = len(number_list)
print("Total elements in list:", Total)
print("First element in list:", number_list[0])
print("Last element in list:", number_list[-1])
print("Reversed list:", number_list[::-1])