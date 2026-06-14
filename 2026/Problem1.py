n = int(input())
s = input().strip()

SixCount = s.count('6')
SevenCount = n - SixCount

print('6' * SixCount + '7' * SevenCount)


