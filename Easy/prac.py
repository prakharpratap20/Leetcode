import array as arr

# a = arr.array("i", [1,2,3,4,5])

# print(a)

# a.append(1)

# print(a)

# a.pop()

# print(a)

# a = a[1:]

# print(a)

# # print(a[-1])

# print(a.pop())

# print(a)

# a.append(5)
# a.append(6)
# a.append(7)
# print(a)

# a.remove(3)

# print(a)

# b = arr.array("i", [1,2,3,4,5])

# c = a + b

# print(c)
# # reverse the array
# c = c[::-1]

# print(c)

a = arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
x = 6

for n in a:
    if n % 2 != 0:
        print(n)


def search(a, x):
    for n in a:
        if x == n:
            return print("Found")


search(a, x)
b = 0
while b < len(a):
    print(a[b] if a[b] % 2 == 0 else 0)
    b = b + 1
    
