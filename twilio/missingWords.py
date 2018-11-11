def missingWords(s, t):
    missingWords = []
    indexS = 0
    indexT = 0
    startS = indexS
    startT = startS
    while indexS < len(s):
        # compare first word
        while indexS < len(s) and indexT < len(t) and s[indexS] == t[indexT] and s[indexS] != ' ':
            indexS += 1
            indexT += 1

        while indexS < len(s) and s[indexS] != ' ':
            indexS += 1

        if indexS - startS == indexT - startT:
            indexS += 1
            indexT += 1
            startS = indexS
            startT = indexT
        else:
            # reset t
            indexT = startT
            # add missing word
            missingWords.append(s[startS:indexS])
            # skip space
            indexS += 1
            startS = indexS
    print(missingWords)


missingWords("I love C Python Ruby and Java", "I love Ruby Java")
