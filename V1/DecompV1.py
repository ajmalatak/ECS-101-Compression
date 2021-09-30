BitTable = open("vals.txt", encoding="utf-16")
bt = BitTable.readlines()

strpassage = open("StrWords.txt", "w")

bitpassage = open("BitWords.txt")
s_b = bitpassage.read()

for i in range(0, int(len(s_b)/6)):
    for line in bt:
        if line[4:10].__contains__(s_b[i*6:(i+1)*6]):
            strpassage.write(line[0])
