
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def is_greater_than_5(x):
#     if x > 5:
#         return True
#     else:
#         return False

new = list(filter(lambda x: x>5, num))
print(new)