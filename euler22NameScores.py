#Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

#What is the total of all the name scores in the file?

def ReadingFileSorted():
    list = open("p022_names.txt")
    for line in list:
        fields = line.rstrip('\n').replace('"',"").split(",")
        fields = sorted(fields)
    return fields


def AlphabetPosition(letter):
    return ord(letter.lower()) - 96

def SumAlphabets(word):
    sum = 0
    for letter in word:
        sum += AlphabetPosition(letter)
    return sum


def NameScores():
    
    list = ReadingFileSorted()

    sum = 0
    for i in range(len(list)):
        sum += SumAlphabets(list[i])*(i+1)
    return sum

final = NameScores()

print(final)