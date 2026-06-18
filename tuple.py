#tuple

x=(10,20,50,["hello","bye"])
for i in x:
    if type(i)==tuple or type(i)==list:
        for item in i:
            print(item)
    else:
        print(i)        
