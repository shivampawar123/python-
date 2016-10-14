def fullname(fname,lname,gender):
    x=fname+" "+lname
    if gender =="Male":
        x="Hello,Mr "+x
    elif(gender=="Female"):
        x="Hello,Ms "+x
    else:
        x="Invalid gender"
    return x
a=input("Enter your first name")
b=input("Enter your last name")
c=input("Enter your gender")
fn=fullname(a,b,c)
print(fn)
