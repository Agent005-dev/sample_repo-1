a = int(input())
say = 0
for i in range(2,a//2+1):
    if a % i == 0:
         say+=1
         print('sade deyil')
    
if say==0:
     print("sadedir")