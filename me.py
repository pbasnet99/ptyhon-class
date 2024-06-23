# print("my name is purushottam")
# x=10
# y=20
# print (x,y)
# x,y,q=10,20,30
# print(x,y,q)
# print('''
# my name is purushottam
#       i am from goli solukhimbu
#       now i am live in kathmandu''')
# print("\"Nepal\"")
# print ('mother\'s')
# print("mother's")
# print("now i am 28 years old, now i am in it sector",end="!")
# course= "we are learning python"
# for i in course:
#     print(i,end="-")
# print("i am doing well,\n top in details")
# print("i want to go kathmandu \t \t \t but i need vehical    \n \n \n for the long time")
# name='hari'
# age=23
# print(name,age)
# print('my age is',age)
# name='sita'
# age=28
# address='ktm'
# email='ram@gmail.com'
# print("\n neme:{} age:{} address:{} email:{}".format(name,age,address,email))
# print(f'\n name: {name}, address: {address}, email: {email}, age: {age}')
# s,d,a,w=23,45,64,45
# print(s,d,a,w)
# d,*e= 3,4,5,6,2,1,3,4
# print(d,e)
# print("\n \n for eval space")
# # a=eval(input("Enter the value1:-"))
# # b=eval(input("Enter the value2:-"))
# # print(a+b)
# s='''
#    the most popular 
#    song is rrrr'''
# print(s)
# x=7+6j
# print(x,type(x))
# w={10,20,30,10,20}
# print(w,type(w))
# p='hi@123456'
# print(p,type(p))
# k=[10,'gh',20,3.4]
# k[3]=10
# print(k,type(k))
# t=(5,10,'pte')
# print(t,type(t))

#dictionary
# d={
#     'course_name':'python',
#     'course_duration': '2 month',
#     'address': 'putalisadak',
#     'contact No': {
#     'office': +9770176738,
#     'mobile': 9842967179}}
# print(d['course_name'])
# print(d,type(d))

# my_set={2,3,4,2,3} # dose not allow dublicates deta through set
# print(my_set,type(my_set))
# name='bro'
# print('hello '+ name)
# first_name='raju'
# last_name='basnet'
# full_name=first_name +" "+ last_name
# print(full_name)
# age=23
# age+=1
# print("your age is: "+ str(age)+' years old')####
# name, age, attractive = 'roshan', 23, True
# print(name)
# print(age)
# print(attractive)
# print(name,age,attractive)
# a=20
# b=20
# c=20
# d=20
# a=b=c=d=30 #value is same 
# print(a)
# print(b)
# print(c)
# print(d)
# names=['ram','sita', 'hari']
# user=['roman','gaurab']
# names.extend(user) # can add value with matchable 
# # names.clear #clear everything 
# print(names)
# names[0]='raju' #changeable variable 
# names.append('pradip') #add value, (only one eliment can add)
# names.insert(0,'anil') # elment can add/ insert anywhere
# # names.remove('sita') # value can remove 
# print(names.pop(1)) #pop also can remove through index
# print(names, type(names))
# print(names[0])
# print(names[2])
# print(dir(names)) #found inner object 
#index, sort, reserve,count,copy 
# title=['math','nepali', 'english',]
# title=['math','nepali', 'english'," Shilpa"] # if use upper letter, the word used started from upper leter is print first.
# title.sort() # data can change start and end . 
# # title.sort(reverse=True) #if add reverse data is disending.
# print(title)
# data=[]
# nam=input('Enter your name:') # from input, user can use the name after use append 
# mail=input('Enter your mail:')
# data.append(nam) # user can use them value (name,email,address,etc.)
# data.append(mail) # same as 107
# print(data)
#tuple
#set 
#disctionary
# p=[
#     [56,46,74,846],
#     [75,594,[[500], [600]],87,64]
# ]
# print(p[1][2][1],)
# print(p[1][2][1], type(p))
#tupple is immutable
#dictionary
# data={
#     'name':'ram' ,
#     'age':28,
#     'address': 'ktm'
#     }
# print(data)
# print(data.get('name'))
# print(data.keys())
# print(data.values())

# h=['katel','raut', 'gautam']
# n1,n2,n3=h
# print(h,type(h))
# print(n1,type (n1))
# print(n2)
# print(n3)
# u=[
#     [23,45,56,32,34],
#     [89,89,67,67,464],
#     [546,87,[[93],83],6,67,]
# ]
# print(u,type(u))
# print(u[2][2])
# print(u[2][2][0],type(u))

# m=(34,56,67,89,87) # tupple value dose not change 
# print(m[0])
# print(m)
# m=(34,56,67,89,87)
# m=list(m) # tupple value dose change after change tupple to list. 
# m[0]=500
# m=tuple(m)
# print(m)

#set
# w={'hirs', 'rupak', 'tiwari'}
# print(w,type (w))
# w={23,43,65,6,87,43,23}
# w1={23,34,56}
# w.union(w1)
# print(w)

#dictionary
#operators:
# arithmetic operators: +,-,*,/,%,//,
# comparison operators: ==,!=,<,>,<=,>=
# logical operators: and, or, not
# assignment operators: =,+=,-=,*=,/=,%=,//=,=
# membership operators: in, not in
# identity operators: is, is not
# bitwise operators: &,|,^,~,<<,>>


# print(5**2)
# print(21/5)
# # print(10/0)
# name='hari'
# print('hello' + str(30))
#################################################
 #operators:
# arithmetic operators: +,-,*,/,%,//,
# comparison operators: ==,!=,<,>,<=,>=
# logical operators: and, or, not
# assignment operators: =,+=,-=,*=,/=,%=,//=,=
# membership operators: in, not in
# identity operators: is, is not
# bitwise operators: &,|,^,~,<<,>>
###################################################
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# add=a+b
# sub=a-b
# mult=a*b
# div=a/b
# moddiv=a%b
# floordiv=a//b
# exp=a**b
# print("Addition is",add)
# print("Subtraction is",sub)
# print("Multiplication is",mult)
# print("Division is",div)
# print("Modulus division is",moddiv)
# print("Floor division is",floordiv)
# print("Exponent is",exp)

# print(f"Addition : {add} \n Subtraction : {sub} \n Multiplication : {mult} \n Division : {div} \n ")
# print(f"Addition : {a+b} \n Subtraction : {a-b} \n Multiplication : {a*b} \n Division : {a/b} \n ")
###############################################################3




# c=4
# d=5
# e=c
# print(c is d)
# print(c id e)
# print(c is not d)

# print('s' in 'shilpa')
# print('z' in 'shilpa')
# print ('z' in not 'shilpa')
# print(6&7)
# print(bin(6))
# print(bin(7))

# print(10&7)
# print(bin(10))
# print(bin(7))
# print(6|7)
# print(10|3)
# print(bin(11))
# print(bin(12))
# print(10&3)
# print(bin(3))
# print(bin (10))

###################################################################
# data=[]
# name=input("Enter your name")
# email=input("Enter your email")
# data.append (name)
# data.append (email)
# print (data)
######################################

# Arithmetic operators ## 
# + addition
# - subtraction
# * multiplication 
# / division 
# // flor division 
# % modulo 
# ** exponentiation 
# 0 can't not use 
#################################################
# print(10%3)
# print(4**2)
# print(19/5)
# print(19//5)
# name='rupak'
# print('hello'+name,(20))
# print('hello' + name + str(20))
##########################################
#comparison operators : ==, !=, >,<,>=,<=
# print(10==10)
# print (10!= 10)
# print(10>30)
# print(10<30)
# print(10>=10)
# print(10<=10)
###############################
# logical operators : and, or, not 
# print(10==10 and 10>30)
# print(20==20 and 20>30)
# print(not 10==10)
##########################################
# Assignment operators : =, +=, *=, /=, %=, //=
# a=5
# a+=50
# print(a)
# c=30
# c*=2
# print(c)
##################################
# identity operators : is, is not 
# membership operators : in, not in 
# a=5
# b=6
# c=a 
# print( a is b)
# print(a is c)
# print (a is not b)

# s='sophia'
# z='jivan'
# print('s' in 'sophia')
# print('z' not in 'sophia')
###################################
# if, elif, else, nested if else 
# v=5
# t=6
# print(v>t)
#######################################
# bitwaise operators : &, |, ^, <<,>>, ~
# print(5&6)
# print(bin(5))
# print(bin(6))

