# operasi logika

# NOT
a = False
c = not a

print('data a =',a)
print('data c =',c)


# OR (jika salah satu true, maka hasilanya)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = False
c = a and b
print(a,'and',b,'=',c)

a = True 
b = False
c = a and b
print(a,'and',b,'=',c)

a = True 
b = True
c = a and b
print(a,'and',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)



