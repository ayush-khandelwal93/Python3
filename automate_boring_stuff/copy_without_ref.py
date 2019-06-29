import copy

# Copy with reference
a = [1,2,3]
b = a
b[0] = 4
print(a)
print(b)
#[4, 2, 3]
#[4, 2, 3]


# Copy without reference
a = [1,2,3]
b = copy.copy(a)
b[0] = 4
print(a)
print(b)
#[1, 2, 3]
#[4, 2, 3]

