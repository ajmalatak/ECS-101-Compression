BitTable = open("CompTable.txt")
bt = BitTable.readlines()

strpassage = open("StrWords.txt", "w")

bitpassage = open("BitWords.txt")
s_b = bitpassage.read()

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
        if s_b[i:i+bitlen] == "10000110":
            strpassage.write("\n")
            break
        elif s_b[i:i+bitlen] == bt[j*2+1][0:len(bt[j*2+1])-1]:
            strpassage.write(bt[j*2][0:len(bt[j*2])-1])
            break
    i+=bitlen