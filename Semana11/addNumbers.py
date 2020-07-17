import re
hand=open('regex_sum_716662.txt')
print(hand)
numlist=list()
for line in hand:
    x=line.split()
    if re.search('[0-9]', line):
        numbers=re.findall('[0-9]+',line)
        for number in numbers:
            n=int(number)
            numlist.append(n)
print(sum(numlist))
