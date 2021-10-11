BitTable = open("CompTable.txt")
bt = BitTable.readlines()

strpassage = open("StrPassage.txt", "w")

bitpassage = open("BitPassage.txt")
temp = bitpassage.read()
s_b = temp[temp.index(".")+1:]

b_newline = ""

for x in range(0, len(bt)-1):
    if bt[x] == ("\\n"+"\n"):
        b_newline = bt[x+1][0:len(bt[x+1])-1]
        break
if b_newline == "":
    print("fail")
    exit()

bitlen = 0
i=0
while i < len(s_b):
    if s_b[i:i+2] == "00":
        bitlen = 5
    elif s_b[i:i+2] == "01":
        bitlen = 7
    elif s_b[i:i+2] == "10":
        bitlen = 8
    elif s_b[i:i+2] == "11":
        bitlen = 6
    for j in range(0, int(len(bt)/2)):
        if s_b[i:i+bitlen] == b_newline:
            strpassage.write("\n")
            break
        elif s_b[i:i+bitlen] == bt[j*2+1][0:len(bt[j*2+1])-1]:
            strpassage.write(bt[j*2][0:len(bt[j*2])-1])
            break
    i+=bitlen