counter = 0
curr = 0
high = 0

games = [20, 10, -35, 20, 15, -10, -20, 20, -30, -10]
for i in range(0, len(games)):
    curr = curr + games[i]
    if high < counter:
        high = counter

    counter = counter + 1

    if curr < 0:
        counter = 0

print(high)
