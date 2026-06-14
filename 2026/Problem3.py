t = int(input())
answers = []

for i in range(t):
    a,b,x,y, dir1 = input().split()
    x = int(x) - int(a)
    y = int(y) - int(b)
    a = 0
    b = 0

    if dir1 == "N":
        var1 = ((y >= 0) and (abs(x) <= y))  
    elif dir1 == "S":
        var1 = ((y <= 0) and (abs(x) <= -y))
    elif dir1 == "E":
        var1 = ((x >= 0) and (abs(y) <= x))
    elif dir1 == "W":
        var1 = ((x <= 0) and (abs(y) <= -x))
    elif dir1 == "NE":
        var1 = ((y >= 0) and (x >= 0))
    elif dir1 == "NW":
        var1 = ((y >= 0) and (x <= 0))
    elif dir1 == "SE":
        var1 = ((y <= 0) and (x >= 0))
    elif dir1 == "SW":
        var1 = ((y <= 0) and (x <= 0))
    
    
    if var1:
        answers.append("YES")
    else:
        answers.append("NO")

for stringAnswer in answers:
    print(stringAnswer)
        



    


    
    
    
    

    