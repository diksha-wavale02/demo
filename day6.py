#nested list
x=[[1,"car",5000],
   [2,"doll",1000],
   [3,"grocery",2000],
   [4,"sunglasses",5000]
   ]
print(x,type(x))
for ids in x:
    print(ids[2])
#adding 
n=int(input("enter how many elements to be added:"))
for i in range(n):
    id=int(input("enter new id:"))
    name=input("enter a name:")
    price=int(input("enter a price:"))
    x.append([id,name,price])
print("updated list")
for item in x:
    
    print(item)
#updating

    
    
    
    
    