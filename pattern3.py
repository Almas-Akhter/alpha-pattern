rows = 5
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(rows, 0, -1):
    for j in range(i):
        print(alpha[j], end=" ")
    print()
