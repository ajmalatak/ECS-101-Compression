t_comp = open("CompTable.txt")
comp_table = t_comp.readlines()

t_test = open("TestPassage.txt")
input_text = t_test.readlines()

test = open("TestPassage.txt")
passage_length = len(test.read())

output_binary = open("BitPassage.txt", "w")

# Finding the binary value for "\n" in the compression table
NEWLINE_BINARY_VALUE = ""
for x in range(0, len(comp_table)-1):
    if comp_table[x] == ("\\n"+"\n"):
        NEWLINE_BINARY_VALUE = comp_table[x+1][0:len(comp_table[x+1])-1]
        break
if NEWLINE_BINARY_VALUE == "":
    print("fail")
    exit()

# binary_string holds the compressed string of 1s and 0s.
# num_of_characters is the current size of the string in comp_table:
#   this is why the compression table must be sorted with biggest strings first,
#   because we want to look for the biggest possible strings first to save the most space
binary_string=""
num_of_characters = -1
for h in range(0, len(input_text)):
    i=0
    while i < len(input_text[h]):
        for j in range(0, int(len(comp_table)/2)):
            num_of_characters = len(comp_table[j*2])-1
            if comp_table[j*2][0:num_of_characters] == input_text[h][i:i+num_of_characters]:
                binary_string+=(comp_table[j*2+1][0:len(comp_table[j*2+1])-1])
                break
        i+=num_of_characters
    binary_string+=NEWLINE_BINARY_VALUE

# Prints the efficiency of the compression
print(len(binary_string))
print(passage_length*8)
print(str(round(1-len(binary_string)/(len(abc)*8), 4)*100)+"% decrease")

# writing binary_string to the output file
output_binary.write(len(binary_string).__str__()+"."+binary_string)
