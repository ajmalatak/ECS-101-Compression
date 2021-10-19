# Open the training file and read its lines to test_passage
freq_test = open("FreqTest.txt")
test_passage = freq_test.readlines()

# A list of all required characters for the project, used later to fill in characters not found in the test passage
req_chars = ['q','w','e','r','t','y','u','i','o','p',
             'a','s','d','f','g','h','j','k','l','z',
             'x','c','v','b','n','m','Q','W','E','R',
             'T','Y','U','I','O','P','A','S','D','F',
             'G','H','J','K','L','Z','X','C','V','B',
             'N','M','.',',','-','!','\'','\"']

# Array of strings with their bit values
string_values = [["PLACEHOLDER&!", 0]]

# Smallest string and largest string to search for and include in the compression table
#   (ex. a max_string_length of 3 and a min_string_length of 1 would include 3, 2, and 1 character strings)
min_string_length = int(input("smallest length: "))
max_string_length = int(input("largest length: "))

# Repeat for all string lengths inputted by the user
# In this loop, each set of {string_length} characters in each line of test_passage is examined
#   if it is not already in string_values, it is added along with a value proportional to its size
#   if it is already in string_values, it's value is increased
for string_length in range(min_string_length, max_string_length+1):
    for line in range(0, len(test_passage)):
        # j is the index of the current character in the current line of test_passage
        j=0
        while j < len(test_passage[line])-string_length+1:
            if not(test_passage[line][j:j + string_length].__contains__("\n")):   # For simplicity, newlines are not included in the multi-character strings. ( or test_passage[line][j:j + string_length].__contains__(" "))
                for x in range(0, len(string_values)):
                    if test_passage[line][j:j + string_length] == string_values[x][0]:
                        string_values[x][1] += 1 * string_length
                        break
                    elif x == len(string_values)-1:
                        string_values.append([test_passage[line][j:j + string_length], 1*string_length])
            j += 1


# Sort the strings largest to smallest value
def sort_string_values(i_arr):
    arr = i_arr
    for j in range(0, len(arr)):
        for i in range(0, len(arr)-1):
            if arr[i][1] < arr[i+1][1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


string_values = sort_string_values(string_values)

# At this point, string_values is a sorted array of arrays that each contain:
#   1) a string
#   2) a value that changes depending on the frequency of the string
# Now the goal is to combine the string with a bit value depending on its frequency.
# comp_arr will contain these.

comp_arr = []

# binary_list is an ordered list of all bit values that the compression code will read
t_b = open("BinList.txt")
binary_list = t_b.readlines()

# Adding the \n character, which isn't searched for in test_passage
comp_arr.append(["\\n"+"\n",binary_list[0]])
count=1

# All of the string and their bit values are added until
#   the number of available bits is equal to the number of required characters not yet used.
# Afterward the rest of the required characters are added.
for a in string_values:
    if len(req_chars) == 0:
        break
    if req_chars.__contains__(a[0]):
        req_chars.remove(a[0])
    elif count+len(req_chars)>=120:
        continue
    comp_arr.append([a[0]+"\n",binary_list[count]])
    count+=1
while len(req_chars) != 0:
    comp_arr.append([req_chars.pop(),"\n"+binary_list[count]])
    count+=1


# sort largest strings first, which is required for the compression code
for j in range(0, len(comp_arr)):
    for i in range(0, len(comp_arr)-1):
        if len(comp_arr[i][0]) < len(comp_arr[i+1][0]):
            temp = comp_arr[i]
            comp_arr[i] = comp_arr[i+1]
            comp_arr[i+1] = temp


# Finally the values are added to the table
comp_table = open("CompTable.txt", "w")

for a in comp_arr:
    comp_table.write(a[0]+a[1])
