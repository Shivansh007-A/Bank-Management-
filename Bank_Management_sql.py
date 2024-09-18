import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost",user="root",passwd="Shivansh@007",database = "abc")

mycursor = mycon.cursor()

def menu():
    print("*"*20)
    print("Press 1 to Display the table")
    print("Press 2 to Withdrew Money")
    print("Press 3 to Deposit Money")
    print("Press 4 for New Entry")
    print("Press 5 to Leave")
    print("Enter option: ")
    
    ch = input()

    if(ch=="1"):
        mycursor.execute("select * from records")
        data = mycursor.fetchall()
        for i in data:
            print(i)
        print("Press 0 to exit: ")
        c = input()
        if(c == "0"):
            menu()
    elif(ch=="2"):
        i_d = int(input("Enter your id: "))
        mycursor.execute("SELECT id from records")
        id_list = mycursor.fetchall()
        for i in id_list:
            if(i == (i_d,)):
                amt = float(input("Enter amount Withderw: "))
                mycursor.execute("SELECT amount from records WHERE id=%s"%(i_d))
                amt_list = mycursor.fetchall()[0]
                
                if((amt,) > amt_list):
                    print("Sorry your balance is insufficient",amt_list[0])
                else:
                    mycursor.execute("UPDATE records SET amount={} WHERE id={}".format(amt_list[0]-amt,i_d))
                    print("Amount withdrawl successfully")
                    mycon.commit()
        print("Press 0 to exit: ")
        c = input()
        if(c == "0"):
            menu()
    elif(ch=="3"):
        i_d = int(input("Enter your id: "))
        mycursor.execute("SELECT id from records")
        id_list = mycursor.fetchall()
        for i in id_list:
            if(i == (i_d,)):
                amt = float(input("Enter amount to deposit: "))
                mycursor.execute("SELECT amount from records WHERE id=%s"%(i_d))
                amt_list = mycursor.fetchall()[0]
                mycursor.execute("UPDATE records SET amount={} WHERE id={}".format(amt_list[0]+amt,i_d))
                print("Amount deposited successfully")
                mycon.commit()
        print("Press 0 to exit: ")
        c = input()
        if(c == "0"):
            menu()
    elif(ch=="4"):
        mycursor.execute("SELECT id from records")
        id_list = mycursor.fetchall()
        id_no = id_list[len(id_list)-1][0]
        i_d = id_no+1
        name = input("Enter name: ")
        mycursor.execute("SELECT acc_no from records")
        acc_list = mycursor.fetchall()
        acc = acc_list[(len(id_list))-1][0]
        acc_no = acc+1
        amount = float(input("Enter amount: "))
        print("\n")
        ch = input("Press y to confirm your entry: ")
        if(ch.lower()=="y"):
            mycursor.execute("INSERT INTO records(id,Name,acc_no,amount) VALUES({},'{}',{},{})".format(i_d,name,acc_no,amount))
            mycon.commit()
            print("Data entered successfully")
            print("\n")
        print("Press 0 to exit: ")
        c = input()
        if(c == "0"):
            menu()
    elif(ch=="5"):
        print("!!! Thank you !!!")
menu()
    
    
    




















