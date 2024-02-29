rows = 5
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(rows):
    for j in range(0, i + 1):
        print(alpha[i], end=" ")
    print()
