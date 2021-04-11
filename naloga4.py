pyramid = [[3, 2, 3, 4, 5], [4, 5, 6, 6], [3, 5, 5], [5, 6], [8]]
force = []
force2 = [0]
y = 0
x = 0

for y in range(len(pyramid[x])):
    for x in range(len(pyramid[y])):
        force.append(0)
        force2.append(0)
        force[x] = force[x] + pyramid[y][x]
        if y == 0:
            force2[x] = force2[x] + pyramid[y][x]
        else:
            force2[x+y] = force2[x+y] + pyramid[y][x]

        x += 1
    print(force2)

    x = 0
    y += 1

#print(force)
