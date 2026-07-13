counter1 = {"Cake", "Sandwich", "Ramen", "Cake", "Pasta"}
counter2 = {"Ramen", "Burger", "Sandwich", "Burger"}
print("Counter 1:", counter1)
print("Counter 2:", counter2)


counter1.add("Sushi")
print("Counter 1 after adding Sushi:", counter1)


common_snacks = counter1.intersection(counter2)
print("Snacks in both counters:", common_snacks)


import array as arr

snack_counts = arr.array('i', [3, 5, 2, 4])
print("Snack counts array:", snack_counts)


snack_counts.insert(0, 1)
snack_counts.append(6)
print("Snacks counts after adding items:", snack_counts)


count_of_4 = snack_counts.count(4)
print("Number of times 4 appears:", count_of_4)

snack_counts.reverse()
print("Reversed snack counts array:", snack_counts)


print("")
print("===== SCHOOL SNACK COUNTER =====")
print("Counter 1:", counter1)
print("Counter 2:", counter2)
print("Shared snacks:", common_snacks)
print("===================================================")
