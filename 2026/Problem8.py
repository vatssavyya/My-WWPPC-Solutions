t = int(input())

for i in range(t):
    N, M, S = map(int, input().split())
    bi = list(map(int, input().split()))
    movement = []

    for ii in range(M-1):
        movement.append((1/(S + bi[ii]))*(bi[ii]/S))
    

    

