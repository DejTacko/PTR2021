from functools import (reduce)

def maxPathSum(rows):
    return reduce(
        lambda x, y: [
            a + max(b, c) for (a, b, c) in zip(y, x, x[1:])
        ],
        reversed(rows[:-1]), rows[-1]
    )[0]

print(
    maxPathSum([
        [8],
        [5, 6],
        [3, 5, 6],
        [4, 5, 6, 6],
        [3, 2, 3, 4, 5],
    ])
)
