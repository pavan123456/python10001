#input string accept string and return the count of vowels in the string 
def countVowels(inputstring):
    strdict = {"a": 0, "e": 0, 'i': 0, 'o': 0, 'u': 0}
    inputlist = list(inputstring.lower())

    for i in inputlist:
        if i in strdict:
            print(i)
            strdict[i] += 1
    print(strdict)


countVowels("pAvan")
