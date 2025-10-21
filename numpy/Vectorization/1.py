list1 = [1,2,4]
list2 = [3,5,6]

result = [a + b for a, b in zip(list1, list2)]
print(result)  # Output: [4, 7, 10]