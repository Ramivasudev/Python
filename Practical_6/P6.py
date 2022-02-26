# D21CS104
# Rami Vasudev

"""You are given n words. Some words may repeat. For each word, output its
number of occurrences. The output order should correspond with the input order
of appearance of the word. See the sample input/output for clarification.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3
2 1 1
Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input
at the first and last positions. The other words appear once each. The order of the
first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the
output."""

from collections import Counter
l=[]
for i in range(int(input())):
    l.append(input())

c=Counter(l)
print(len(c))
for i in c:
    print(c.get(i),end=' ')
print()
