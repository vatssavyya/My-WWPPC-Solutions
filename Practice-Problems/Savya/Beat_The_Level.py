n = int(input("Level length: "))
s = input("string repping the level: ") #s has length n

maxCounter = 0;
counter = 0
for i in range(n):
    if s[i] == "S":
        counter += 1
    else:
        maxCounter = max(maxCounter, counter)
        counter = 0
if (maxCounter > 3):
    print("DIE")
else:
    print("BEAT")