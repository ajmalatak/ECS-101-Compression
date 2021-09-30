BitTable = open("CompTable.txt")
bt = BitTable.readlines()

strpassage = open("TestWords.txt")
s_p = strpassage.readlines()

bitpassage = open("BitWords.txt", "w")

for h in range(0, len(s_p)):
    i=0
    while i < len(s_p[h]):
        if s_p[h][i:i+3] == "and":
            bitpassage.write("00001")
            i+=2
        elif s_p[h][i:i+3] == "the":
            bitpassage.write("00000")
            i+=2
        elif s_p[h][i:i+2] == "er":
            bitpassage.write("00010")
            i+=1
        else:
            for j in range(3, int(len(bt)/2)):
                if bt[j*2][0:1] == s_p[h][i]:
                    bitpassage.write(bt[j*2+1][0:len(bt[j*2+1])-1])
        i+=1
    bitpassage.write("10000110")
