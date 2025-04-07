print("Bank_System")
print("What would you like to do?")
print("1.Register\n2.Login\n3.Send_Money\n4.Check_Balance\n5.Exit")
users={"Name":[],"Account":[],"Pin":[],"Balance":[]}

while True:
    try:
        n=int(input("Enter your choice: "))
        if n==5:
            print("Exit is success")
            break
        if 0<n<=4:
            if n==1:
                print("Lets register you to our app!!")
                users["Name"].append(input("Enter your full name: "))
                users["Account"].append(int(input("Enter your Account number: ")))
                users["Pin"].append(int(input("Keep a strong password: ")))
                print("You have registered successfully,now go to login section")
            elif n==2:
                a=str(input("Enter your name: "))
                b=int(input("Enter your account number: "))
                c=int(input("Enter your pin: "))
                if a in users["Name"] and b in users["Account"] and c in users["Pin"]:
                    print("Logged in successfully")
                else:
                    print("Incorrect inputs,try again or you have not registered")
            
            elif n==3:
                print("You are in send money section")
                d=int(input("Enter account number you want to send money: "))
                if d in users["Account"]:
                    e=int(input("Enter amount you want to send: "))
                    f=int(input("Enter your pin to confirm payment: "))
                    if f in users["Pin"]:
                        users["Balance"].add(e)
                        print(f"Amount sent successfully to account number: {d}")
                    else:
                        print("Incorrect inputs,try again")
                else:
                    print("Entered account number does not exist,Recheck account number and try again")
            elif n==4:
                g=str(input("Do you want to check amount balance in your account? yes/no: "))
                if g=="yes":
                    h=int(input("Enter your account number: "))
                    j=int(input("Enter your pin: "))
                    if h in users["Account"] and j in users["Pin"]:
                        print("You account balance is: ",users["Balance"])
                    else:
                        print("Inputs are incorrent or not yet registered")
                else:
                    print("ok,we won't show your balance amount")
        else:
            print("Your choice should be between 1-5,to proceeed")
    except ValueError:
        print("Only int values are expected,try again!")
        
