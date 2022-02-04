# Find runner-up from given list
# D21CS104
# Rami Vasudev

n = int(input())
score = map(int, input().split())
print(sorted(list(set(score)))[-2])