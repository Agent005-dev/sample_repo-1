n = input().split()
n.sort()

if len(n) % 2 == 0:
      
      print(n[len(n)//2-1], n[len(n//2)], end='')
else:
    print(n[len(n) // 2])
