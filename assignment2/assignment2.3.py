sum=0
i=0
x=list(range(1,20))
while(x[i]!='\0'):
    sum+=sum+x[i]
    i=i+1
    if(sum>31):
        break

print(sum)






