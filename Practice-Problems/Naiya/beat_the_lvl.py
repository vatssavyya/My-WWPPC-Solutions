lvlLength = int(input("lvl length: "))
lvl = input("lvl string: ")
prevSpikes = 0

for i in range(lvlLength-1):
    if lvl[i] == "S":
        prevSpikes = prevSpikes + 1
    else:
        prevSpikes = 0
    
    if prevSpikes > 3:
        print("DIE")
        break
    
    if i == lvlLength-1:
        print("BEAT")



        

