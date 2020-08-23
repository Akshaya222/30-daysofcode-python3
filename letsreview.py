t=int(input())
for i in range(t):
    n=input()
    odd_list=list()
    even_list=list()
    for j in range(len(n)):
       if(j%2==0):
            even_list.append(n[j])
       else:
             odd_list.append(n[j])
    odd_index="".join(odd_list)
    even_index="".join(even_list)
    print(even_index,odd_index)  
