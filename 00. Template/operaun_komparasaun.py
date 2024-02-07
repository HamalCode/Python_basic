
# setiap hasil dari  operasi adalah bool

# >,<,>=, <=,==,!=,is,is not
a=4
b=2
# maior do que >
print('======Maior do que (>)')
resultadu = a>3
print (a, '>',3,'=',resultadu)
resultadu = b>3
print (b, '>',3,'=',resultadu)
resultadu = b>2
print (b, '>',2,'=',resultadu)


# menor do que<
print('======Menor do que (<)')
resultadu = a<3
print (a, '<',3,'=',resultadu)
resultadu = b<3
print (b, '<',3,'=',resultadu)
resultadu = b<2
print (b, '<',2,'=',resultadu)

# maior do que igual>=
print('======maior do que iguak (>=)')
resultadu = a <= 3
print (a, '>=',3,'=',resultadu)
resultadu = b >= 3
print (b, '>=',3, '=', resultadu)
resultadu = b >=2
print (b, '>=',2, '=', resultadu)

# menor do que igual 
print ('============Menor do Que Igual========(<=)')
resultadu = a <= 3
print (a, '<=',3,'=',resultadu)
resultadu = b <= 3
print (b, '<=',3, '=', resultadu)
resultadu = b <=2
print (b, '<=',2, '=', resultadu)

print ('============ Igual/sama dengan(==)')

resultadu = a == 4
print (a, '==',4, '=', resultadu)

resultadu = b == 4
print (b, '==',4, '=', resultadu)

print ('============ Igual/sama dengan(!=)')
resultadu = a !=4
print (a, '!=',4, '=', resultadu)
resultadu = b !=4
print (b, '!=',4, '=', resultadu)

print ('============ Object identity (is)')
# is sebagai komparasi objek identity
x=5 #ini adalah assignment membuat object
y=5
print ('valor x=',x, ',id=', hex(id(x)))
print ('valor y=',y, ',id=', hex(id(x)))

resultadu = x is y
print('x is y', resultadu)

x=5 #ini adalah assignment membuat object
y=6
print ('valor x=',x, ',id=', hex(id(x)))
print ('valor y=',y, ',id=', hex(id(x)))

resultadu = x is y
print('x is y', resultadu)

print ('============ Object identity (is not)')
# is sebagai komparasi objek identity
x=5 #ini adalah assignment membuat object
y=5
print ('valor x=',x, ',id=', hex(id(x)))
print ('valor y=',y, ',id=', hex(id(x)))

resultadu = x is not y
print('x is y', resultadu)

x=5 #ini adalah assignment membuat object
y=6
print ('valor x=',x, ',id=', hex(id(x)))
print ('valor y=',y, ',id=', hex(id(x)))

resultadu = x is not y
print('x is y', resultadu)