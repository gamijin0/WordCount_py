import re
from collections import Counter
class WordCount:

    def __init__(self,filename):
        self.filename = filename

    def count(self):
        with open(self.filename,mode='r') as f:
            tmp=""
            for line in f.readlines():
                tmp += re.sub('[^\w]', ' ', line)
            return Counter(tmp.split())

