'''
#dictionary
x={}

print(x,type(x))
#add
x["name"]="ram"
print(x)
print(x["name"])
#update
x["name"]="sita"
print(x)
x[101]="stud data"
print(x)
#del or pop
del x[101] #none return
print(x)
print(x.pop("name"))#return key-> value

#key=input("enter key:")
#value=input("enter value")
x.update({"name":"ram"})

stud={
    "name":"ram",
    "age":20,
    "div":"a",
    "marks":[100,78,67],
    "sub":["math","eng"],
    "rollno":909
}

print(stud.keys())
print(stud.values())
print(stud.items())
for key,values in stud.items():
   print(key,values)


#dictionary ->list

for values in stud.values():
    if type(values)==list:
        for i in values:
            print(i)
        continue
print(values)  


product={
    101:
{
    "productname":"car",
    "price":1000,
    "colour":"black",
    "qty":10,
    "models":[101,503]
}
}
print(product[101]["colour"])
#key
for v in product.values():
    for k,v in v.items():
        print(k,v)


#set
x=set()
print(type(x))
x.add(30)
x.add(10)
x.add(40)
xl=list(x)
xl[2]=90
print(xl)
x=set(xl)
print(x,type(x))


A={1,2,3}
B={3,4,5}
print(A|B)
print(A&B)
print(A-B)
print(A^B)

#frozen set
x=frozenset([10,20,30])
print(x,type(x))
#x.add(90)
#print(x)
for i in x:
    print(i)
print(20 in x)    
x=frozenset((910,20,30))
print(x,type(x))
x=frozenset("hello")
print(x,type(x))
'''

stud={
    101:{
        "name":"ram",
        "age":18,
        "subject":["python","java","mern"],
        "marks":[50,89,78]
    },
    102:{
        "name":"sita",
        "age":19,
        "subject":["python","java","mern"],
        "marks":[70,80,90]
    },
    103:{
        "name":"rahul",
        "age":20,
        "subject":["python","java","mern"],
        "marks":[58,79,100]
    },
    104:{
        "name":"gita",
        "age":21,
        "subject":["python","java","mern"],
        "marks":[88,97,100]
    }

}
#total sum of marks

print("total marks of ram:")
for s in stud:
    if s["name"]=="ram":
        total=sum(s["marks"])
        print(s["name"],"total:",total)

print("total marks of rahul:")
for m in stud:
    if m["name"]=="rahul":
        total=sum(m["marks"])
        print(m["name"],"total:",total) 

print("total marks of sita")
for j in stud:
    if j["name"]=="sita":
        total=sum(j["marks"])
        print(j["name"],"total:",total)   

print("total marks of gita:")
for k in stud:
    if k["name"]=="gita":
        total=sum(k["marks"])
        print(k["name"],"total:",total)

    


