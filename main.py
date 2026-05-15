
a = int(input())
say = 0
if a != 1:
     for i in range(2,a//2+1):
       if a % i == 0:
            say+=1
if say == 0:
             print('sadedir')
else:
           print('sade deyil ')
    
    
