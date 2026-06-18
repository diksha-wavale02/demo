#largest among 3 numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))

if(a>=b and a>=c):
    print("a is greater",a)

elif(b>=c and b>=a):
    print("b is greater",b)

else:
    print("c is greater") 

#leap year

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is Leap year")
else:
    print(year, "is Not Leap year")

#calculate marks
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\nTotal =", total)
print("Percentage =", percentage, "%")

# Grade calculation
if percentage >= 90:
    grade = "A Grade"
elif percentage >= 75:
    grade = "B Grade"
elif percentage >= 50:
    grade = "C Grade"
else:
    grade = "Fail"

print("Grade:", grade)

# Distinction/Pass/Fail
if percentage >= 75:
    print("Distinction")
elif percentage >= 50:
    print("Pass")
else:
    print("Fail")

# login page

username="admin"
password=1234
Username=input("enter username:")
if Username==username:
    print("correct username")
    Password=int(input("enter password:"))
    if Password==password:
        print("correct password")
        print("login successfully")
    else:
        print("incorrect password")
        
else:
    print("invalid")  