## lets import mysql connector
import mysql.connector;

cur = None;

def connect_to_database():
    ## connect to our database ( i hate python )
    data_base = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "nicknick",
    ); 

    cur = data_base.cursor();
    cur.execute("create database if not exists bank_app");
    cur.execute("use bank_app")
    cur.execute("CREATE TABLE if not exists person (account_number int primary key auto_increment, name varchar(50), balance int(6))"); ## table for personal info
    cur.execute("CREATE TABLE if not exists bank (account_number int, amount int(6), type_of_transation char(1), foreign key (account_number) references person(account_number))"); ## table for transation info

