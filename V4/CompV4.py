BitTable = open("CompTable.txt")
bt = BitTable.readlines()

strpassage = open("TestWords.txt")
s_p = strpassage.readlines()

test = open("TestWords.txt")
abc = test.read()
print(len(abc)*8)

bitpassage = open("BitWords.txt", "w")

b_newline = "10000110"

bitstr=""
strlen = -1

for h in range(0, len(s_p)):
    i=0
    while i < len(s_p[h]):
        for j in range(0, int(len(bt)/2)):
            strlen = len(bt[j*2])-1
            if bt[j*2][0:strlen] == s_p[h][i:i+strlen]:
                bitstr+=(bt[j*2+1][0:len(bt[j*2+1])-1])
                break
        i+=strlen
    bitstr+=b_newline

bitpassage.write(len(bitstr).__str__()+"."+bitstr)
