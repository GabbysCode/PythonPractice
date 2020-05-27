a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
while a[0] < 5:
    print(a[0])
    b.append(a[0])
    a.pop(0)
print(b)
smalls = []
number = input("what's ya number? ")
for i in a:
    if i < int(number):
        smalls.append(i)

print(smalls)

