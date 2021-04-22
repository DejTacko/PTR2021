counter = 0
curr = 0
high = 0
i = 0
games = [10, -20, 10, 10, 20, 20, -35]
for i in range(0, len(games)):
    curr = curr + games[i]
    if curr < 0:
        counter = 0
    if high < counter:
        high = counter

    counter = counter + 1


print(high)
