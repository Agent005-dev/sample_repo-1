# n = input().split()
# n.sort()

# if len(n) % 2 == 0:
      
#       print(n[len(n)//2-1], n[len(n//2)], end='')
# else:
#     print(n[len(n) // 2])


a = [3, 4, 5, 6, 8, 9]
for i in range(len(a)):
     if a[i] % 2 == 0:
          a[i] = i
     else:
          say = 0
          for j in range(1, i+1):
               if i % j == 0:
                    say +=1
               i[j] = say
        
                  
     