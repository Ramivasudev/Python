# Find Captain Room Number
# D21CS104
# Rami Vasudev

k = int(input())
room_number = list(map(int, input().split()))
captain_room_number = (sum(set(room_number)) * k - sum(room_number))  // (k - 1)
print(captain_room_number)