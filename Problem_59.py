        # Problem 59: XOR decryption

        # Key1 candidates: 102, 103 ?
        # Key2 candidates: 108, 110, 111 ?
        # Key3 = 100 (d) ?

f = open("cipher1.txt")

message = f.read()
message = message.split(",")

key1 = []
key2 = []
key3 = []
trans1 = []
trans2 = []
trans3 = []
text = ""
answer = 0

for index, x in enumerate(message):
    if index % 3 == 0:
        key1.append(x)
    elif index % 3 == 1:
        key2.append(x)
    else:
        key3.append(x)

for i in range(61, 123):
    candidates = []
    for j in set(key1):                 # Populate candidates
        candidates.append(i^int(j))
    candidates = sorted(set(candidates))
    if int(candidates[0]) < 32 or int(candidates[-1]) > 122:
        pass
    else:
        pass # print(i, " could be a candidate for key1.")

for a in key1:
    trans1.append(chr(int(a)^103))

for b in key2:
    trans2.append(chr(int(b)^111))

for c in key3:
    trans3.append(chr(int(c)^100))

temp = zip(trans1, trans2, trans3)
for item in temp:
    for thing in item:
        text += thing

print(text)
for item in trans1:
    answer += ord(item)
for item in trans2:
    answer += ord(item)
for item in trans3:
    answer += ord(item)

print(answer)

