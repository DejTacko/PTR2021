#poskus pred odkritjem functools

pyramid = [[4, 6, 8, 8, 3, 8], [8, 3, 4, 7, 6], [3, 4, 9, 6], [2, 6, 5], [3, 5], [8]]
force = []
force2 = []
y = 0
x = 0

for y in range(len(pyramid[x])):
    for x in range(len(pyramid[y])):
        force.append(0)
        force2.append(0)
        force3.append(0)
        if y == 0:
            force[x] = force[x] + pyramid[y][x]
            force2[x] = force2[x] + pyramid[y][x]
        else:
            force[x] = force[x] + pyramid[y][x]
            force2[x+y] = force2[x+y] + pyramid[y][x]


        x += 1
    print(force)

    x = 0
    y += 1

print(max(force))
print(max(force2))
