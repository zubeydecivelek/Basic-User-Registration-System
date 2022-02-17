users=open("users.txt","r")
userslist=[i.strip("\n").split(";") for i in users]
usernamelist=[i[0] for i in userslist]
passwordslist=[i[1] for i in userslist]
friendslist=[i[2:] for i in userslist]
users.close()


def controlusername(username):
    for i in username:
        if i in "0123456789abcdefghijklmnopqrstuvwxyz":
            return True
        else:
            return False

def controlpassword(password):
    if len(password) not in range(4,9):
        return False
    numbercounter=0
    lettercounter=0
    for i in password:
        if i in "0123456789":
            numbercounter+=1
        elif i in "abcdefghijklmnopqrstuvwxyz":
            lettercounter+=1
    if numbercounter==0 or lettercounter==0:
        return False
    else:
        return True

loggedincounter=0
def option1(username):
    global loggedincounter
    if username in usernamelist:
        n=usernamelist.index(username)
        password=input("Please enter password:\n")
        if password == passwordslist[n]:
            print("Logged in\n")
            loggedincounter+=1
    else:
        print("Wrong password or user name.\n")

def option2():
    global usernamelist,passwordslist,friendslist
    newusername=input("Please enter username:\n")
    if newusername not in usernamelist and controlusername(newusername)==True:
        newpassword=input("Please enter password:\n")
        if controlpassword(newpassword)==True:
            usernamelist.append(newusername)
            passwordslist.append(newpassword)
            friendslist.append([])
            print()
        else:
            print("Password not valid\n")
    else:
        print("Username not valid\n")

def option3():
    global friendslist
    if loggedincounter!=0:
        friendname=input("Please enter the name of your new friend:\n")
        n=usernamelist.index(username)
        if friendname in usernamelist:
            if friendslist[n]!=[] and friendslist[n]!=['']:
                friendslist[n][0]=friendslist[n][0]+","+friendname
            else:
                friendslist[n].clear()
                friendslist[n].append(friendname)
            print()
        else:
            print("Friend not found\n")
    else:
        print("You need to log in first\n")


def option4():
    if loggedincounter!=0:
        n=usernamelist.index(username)
        print(*friendslist[n])
        print()
    else:
        print("You need to log in first\n")


def option5():
    output=open("users.txt","w")
    for i in range(len(usernamelist)):
        print(usernamelist[i],passwordslist[i],*friendslist[i],sep=";",file=output)
    output.close()

while True:
    print("1. Log in / change user","2. Create new user","3. Add friend","4. Show my friends","5. Save and exit", sep="\n")
    secim = int(input())
    if secim==1:
        username=input("Please enter username:\n")
        option1(username)
        continue
    elif secim==2:
        option2()
        continue
    elif secim==3:
        option3()
        continue
    elif secim==4:
        option4()
        continue
    elif secim==5:
        option5()
        break
    else:
        print("Invalid option\n")
        continue
