BitTable = open("CompTable.txt")
bt = BitTable.readlines()

strpassage = open("TestPassage.txt")
s_p = strpassage.readlines()

test = open("TestPassage.txt")
abc = test.read()

bitpassage = open("BitPassage.txt", "w")

b_newline = ""

for x in range(0, len(bt)-1):
    if bt[x] == ("\\n"+"\n"):
        b_newline = bt[x+1][0:len(bt[x+1])-1]
        break
if b_newline == "":
    print("fail")
    exit()

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

print(len(bitstr))
print(len(abc)*8)
print(str(round(1-len(bitstr)/(len(abc)*8), 4)*100)+"% decrease")

bitpassage.write(len(bitstr).__str__()+"."+bitstr)
