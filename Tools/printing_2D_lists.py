numbers = [
    ['1', '2', '3'],
           ['4', 5, 6],   # Contains integers as well.
           ['7', '8', '9']
]

for x in numbers:
    print(*x, sep=" ", end=" ")