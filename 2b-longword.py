def longword(wordslst):
    wordlen = []
    for n in wordslst:
        wordlen.append((len(n),n))
        wordlen.sort()
    return wordlen[-1][0], wordlen[-1][1]
result = longword(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
