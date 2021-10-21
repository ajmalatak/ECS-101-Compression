BitTable = open("CompTable.txt")
comp_table = BitTable.readlines()

output_text = open("StringOutput.txt", "w")

t_binary = open("BinaryOutput.txt")
temp = t_binary.read()
input_binary = temp[temp.index(".")+1:]

NEWLINE_BINARY_VALUE = ""

for x in range(0, len(comp_table)-1):
    if comp_table[x] == ("\\n"+"\n"):
        NEWLINE_BINARY_VALUE = comp_table[x+1][0:len(comp_table[x+1])-1]
        break
if NEWLINE_BINARY_VALUE == "":
    print("fail")
    exit()

num_of_bits = 0
i=0
while i < len(input_binary):
    if input_binary[i:i+2] == "00":
        num_of_bits = 5
    elif input_binary[i:i+2] == "01":
        num_of_bits = 7
    elif input_binary[i:i+2] == "10":
        num_of_bits = 8
    elif input_binary[i:i+2] == "11":
        num_of_bits = 6
    for j in range(0, int(len(comp_table)/2)):
        if input_binary[i:i+num_of_bits] == NEWLINE_BINARY_VALUE:
            output_text.write("\n")
            break
        elif input_binary[i:i+num_of_bits] == comp_table[j*2+1][0:len(comp_table[j*2+1])-1]:
            output_text.write(comp_table[j*2][0:len(comp_table[j*2])-1])
            break
    i+=num_of_bits