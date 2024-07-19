#if think not work, code below

astr='Hello Bob'
#might be wrong, so insure
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)
