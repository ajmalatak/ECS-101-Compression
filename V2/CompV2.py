BitTable = open("vals.txt", encoding="utf-16")
bt = BitTable.readlines()
print(bt)

strpassage = open("TestWords.txt")
s_p = strpassage.readlines()

bitpassage = open("BitWords.txt", "w")

for i in range(0, len(s_p)):
    for j in range(0, len(s_p[i])):
        for line in bt:
            if line[0] == s_p[i][j]:
                bitpassage.write(line[4:10])
                break
    bitpassage.write(bt[58][5:11])
