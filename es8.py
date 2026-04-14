#l=[0,1,2,3,4,5,6,7,8,9]

#l_disp = [n for n in l if n%2 !=0]
#print(l_disp)

#ll=[[1,2,3],[4,5],[6,7,8,9]]
#print([n for x in ll for n in x])

#lista_a=[1,3,5,7]
#lista_b=[2,4,6]
#print([x*y for x in lista_a for y in lista_b if x*y>10])

#def is_terna_pitagorica(a,b,c):
#    return a**2+b**2==c**2 and a!=0 and b!=0 and c!=0
#
#a = [i for i in range(21)]
#b = [i for i in range(21)]
#c = [i for i in range(21)]
#terne_p = [(x,y,z) for x in a for y in a for z in a if is_terna_pitagorica(x,y,z)]
#print(terne_p)

lista_a=[0,1,3,4]
list_b=['a','b','c']
print([(x,y) for x in lista_a for y in list_b if x%2==0 and list_b.index(y)%2!=0])
print([(x,y) for x in lista_a for i,y in enumerate(list_b) if x%2==0 and i%2!=0])