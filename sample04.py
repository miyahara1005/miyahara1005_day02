# Listにまつわる　あるあるErrorをわざと起こそう！

members = ['Bob', 'Tom', 'Ken']

# print(members[9999])

# IndexError: list index out of range

print(members[-1]) #Ken
print(members[-2]) #Tom
print(members[-3]) #Bob
# print(members[-4]) #IndexError: list index out of range
print(members[-1.1]) #TypeError: list indices must be integers or slices, not float


