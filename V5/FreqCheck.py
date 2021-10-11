strpassage = open("FreqTest.txt")
s_p = strpassage.readlines()


def sortwords(i_arr):
    arr = i_arr
    for j in range(0, len(arr)):
        for i in range(0, len(arr)-1):
            if arr[i][1] < arr[i+1][1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

allletters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','.',',','-','!','\'','\"']
words = [["PLACEHOLDER&!", 0]]
minlen = int(input("smallest length: "))
maxlen = int(input("largest length: "))

for strlen in range(minlen, maxlen+1):
    for h in range(0, len(s_p)):
        i=0
        while i < len(s_p[h])-strlen+1:
            if not(s_p[h][i:i + strlen].__contains__("\n") or s_p[h][i:i + strlen].__contains__(" ")):
                for x in range(0, len(words)):
                    if s_p[h][i:i + strlen] == words[x][0]:
                        words[x][1]+=1*strlen
                        break
                    elif x == len(words)-1:
                        words.append([s_p[h][i:i + strlen], 1*strlen])
            i += 1
            contbad = 1
            while contbad == 1 and i<len(s_p[h])-strlen:
                contbad = 0
                for q in range(0, strlen):
                    if not allletters.__contains__(s_p[h][i+q]):
                        contbad = 1
                i+=contbad


words = sortwords(words)
comparr = []
t_b = open("BinList.txt")
binlist = t_b.readlines()

comparr.append([" "+"\n",binlist[0]])
comparr.append(["\\n"+"\n",binlist[1]])

reqchar = 58
count=2
for a in words:
    if reqchar == 0:
        break
    if allletters.__contains__(a[0]):
        reqchar-=1
        allletters.remove(a[0])
    elif count+reqchar>=120:
        continue
    comparr.append([a[0]+"\n",binlist[count]])
    count+=1
while len(allletters) != 0:
    comparr.append([allletters.pop(),"\n"+binlist[count]])
    count+=1



# sort largest words first
comptable = open("CompTable.txt", "w")

for j in range(0, len(comparr)):
    for i in range(0, len(comparr)-1):
        if len(comparr[i][0]) < len(comparr[i+1][0]):
            temp = comparr[i]
            comparr[i] = comparr[i+1]
            comparr[i+1] = temp

for a in comparr:
    comptable.write(a[0]+a[1])
