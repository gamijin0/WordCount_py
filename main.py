from WordCount.wordcount import WordCount

for i in range(0,10):
    one = WordCount(filename="sample/file%d.txt" % i)
    print(one.count())


