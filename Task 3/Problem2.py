pattern=input().strip()
text=input().strip()
d=int(input())

lst=[]
k=len(pattern)
n=len(text)
for i in range(n- k+1):
    miss=0
    
    for j  in range(k):
        if pattern[j] != text[i+j]:
            miss+=1
          
    if miss<=d:
        lst.append(i)


print(*lst)    
        
