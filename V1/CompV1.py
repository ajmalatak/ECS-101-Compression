BitTable = open("vals.txt", encoding="utf-16")
bt = BitTable.readlines()

strpassage = open("TestWords.txt")
s_p = strpassage.read()

bitpassage = open("BitWords.txt", "w")

for i in range(0, len(s_p)):
    for line in bt:
        if line[0].__contains__(s_p[i]):
            bitpassage.write(line[4:10])