def WordCount(lyrics):
    with open(lyrics) as file:
        readwords = file.read()
    splitreadwords = readwords.split()
    wordcount = {}
    for i in range(0,len(splitreadwords)):
        if not splitreadwords[i] in wordcount:
            wordcount.update({splitreadwords[i]:1})
        else:
            wordcount[splitreadwords[i]] += 1
    #print(wordcount)
    import operator
    sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_wordcount)
    print(len(sorted_wordcount))

WordCount("Double Album.txt")

        
