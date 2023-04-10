num = int(input("請輸入一個數字："))

bits =  [0] * num

combinations = []
for i in range(2**len(bits)):
    combination = []
    for j in range(len(bits)):
        combination.append(i >> j & 1 == 1)
    combinations.append(combination)

for combination in combinations:
    count = 0
    for bit in combination:
        if bit:
            count += 1
    print(combination, count)
