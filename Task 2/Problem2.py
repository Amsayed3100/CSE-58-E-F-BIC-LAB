txt=input()
k=int(input())

frq={}

for i in range(len(txt)- k+1):
    kmer=txt[i:i+k]
    frq[kmer]=frq.get(kmer,0)+1
  

mx=max(frq.values())
        
for kmer in frq:
    if frq[kmer] == mx:
        print(kmer,end=" ")
