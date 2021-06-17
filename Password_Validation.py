
def passval(naresh):#password validation function
    k=0#condition count variable
    a=0#lowercase count variable
    b=0#uppercase count variable
    c=0#digit count variable
    pv=len(naresh)#length of the password

    if pv>=8 and pv<=14:
        k=k+1#length of password should be in between 7 to 15
    
    for i in naresh:
        if i.islower():
            a=a+1
    if a>=3:#password must have atleast 3 lowercase characters
        k=k+1

    for j in naresh:
        if j.isupper():
            b=b+1
    if b>=2:#password must have atleast 2 uppercase characters
        k=k+1
    
    for l in naresh:
        if l.isdigit():
            c=c+1
    if c>=2:#password must have atleast 2 digits
        k=k+1
    
    for m in naresh:
        if (m=='#' or m=='@' or m=='$'):#password must have special characters
            k=k+1
    if k==5:
        return k
def main():
    naresh=input("enter your password...")
    if (passval(naresh)):
        print("password is valid")
    else:
        print("password is not valid")

main()#function calling
       
       
