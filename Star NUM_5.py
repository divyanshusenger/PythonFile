# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3
# 6 5
# 7

for i in range(1, 8):
    k = i
    for j in range(1, 5):
        if j <= i:
            print(k, end=" ")
            k -= 1
        else:
            print(" ", end=" ")
    print()

