
t = int(input("num of test cases: "))


dict1 = {"N": 0, "S": 0, "E": 0, "W": 0 }

print(dict1["NE"])

for i in range(t):
    a,b,c,d, dir1 = input("input: ").split()
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
        print("YES")
    else:
        print("NO")
        



    


    
    
    
    

    