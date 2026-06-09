str=input()

lst=''
for i in range(len(str)-1,-1,-1):
    if str[i]=='A':
        lst+='T'
    elif str[i]=='T':
        lst+='A'
    elif str[i]=='C':
        lst+='G'
    elif str[i]=='G':
        lst+='C'

print(lst) 
