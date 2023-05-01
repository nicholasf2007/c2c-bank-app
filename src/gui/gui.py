
import mysql.connector;
import src.database.database as database_connector

def show_gui():

    data_base = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "nicknick",
        database = "bank_app" ## already created by database.py so no error :)
    ); 

    cur = data_base.cursor();

    print("Welcome to nick's bank\n")

    while True:
        print("Would you like to open a banking account with us, withdraw money, deposit money, or view your acction details");
        action = input("")
        if action == "Open":
            print("\nOkay, lets get started\n"); ## a little bit of new lines to make it look nice
            account_name = input("Please state your name: ");

            cur.execute("insert into Person(name, balance) values(%s, %s)", (account_name, 0));
            cur.execute("select * from Person where name='" + account_name + "'");
            
            for i in cur:
                print("Thank you, we have created your account under the name: '" + account_name + "' with account number: " + str( i[0]) + "\n")

        
        if action == "deposit":
            print("\nOkay, lets get started\n"); ## a little bit of new lines to make it look nice
            account_number = input("Please state your account number: ");
            deposit_ammount = int(input("Please state the amount u want depositied: "));
            type = "d"
            cur.execute("insert into bank values('" + account_number + "','" + str(deposit_ammount) + "','" + type + "')");
            print('passed\n')
            
            


