#Tuplas não são editaveis!!! Tem q transformar em lista e depois converter pra tupla
t1 = (1,2,3,'Natan', True)
print(t1)

for v in t1:
    print(v)

t2 = 1,
print(type(t2))

t2 = 1, 2, 3, 4
print(type(t2))

t3 = t1 + t2
print(t3)