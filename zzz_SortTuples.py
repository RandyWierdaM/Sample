
elegList = [(u'C-040', 4, 0, u'19/12/17'),
            (u'B-001', 1, 0, u'10/4/2017'),
            (u'C-002', 4, 1, u'10/4/2017'),
            (u'C-008', 3, 0, u'11/4/2017')]

#Method 1, no imports needed
#elegList.sort(key=lambda x:x[0]) # (0) is the tuple index to use for the sort

#Method 2, import itemgetter
from operator import itemgetter
sorted(elegList, key=itemgetter(0)) # (0) is the tuple index to use for the sort

for e in elegList:
    print e
#print elegList

