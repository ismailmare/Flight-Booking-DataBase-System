# Assignment:           Proj 2
# Due Date:             October, 27 2015
# Name:                 Ismail Mare, Janice Loo, Preyanshu Kumar
# Unix ID:              imare, preyansh --Add your unix ids!--
# StudentID:            1388973, 1395321 --Add your sids!--
# Lecture Section:      B1
# Instructor:           Davood Rafiei
#---------------------------------------------------------------
#

#importing necessary libraries
import cx_Oracle
import sys
import datetime
import math




#----------------------------------------------------
#Ismail Part
#stuff in red is mostly SQL statements

#Search for flights
#got upto searching for valid src and dst codes from user
# not complete
def search():
        print("\n"*10)
        while True:
            source = input("Enter the source: ")
            destination = input("Enter the destination: ")
            departure = input("Enter the departure date: ")
            
            curs.execute("SELECT src from flights where source == src")
            rows = curs.fetchall()
            
            if rows == 0:
                print("Not a valid Source Airport Code")
                curs.execute("SELECT src, from flights,airports where src=acode and (city LIKE source) or (name LIKE source)"
                             "ORDER BY src DESC")
                rows = curs.fetchall()

                if rows>0:
                    print(rows)
                    num = input("Select row of Source Airport or Enter Q to search again: ")
                    if (num > 0):
                        source = rows[num]
                        break
                    else:
                        continue
                else:
                    curs.execute("SELECT src, from flights,airports where src=acode and (city LIKE source[0:len(source)//2] or (name LIKE source[0:len(source)//2]"
                                     "ORDER BY src DESC")
                    rows = curs.fetchall()
                    if rows>0:
                        print(rows)
                        num = input("Select row of Source Airport or Enter Q to search again: ")
                        if (num > 0):
                            source = rows[num]
                            break
                        else:
                            continue
                    else:
                        print("Could not match source airport, please search again")
                        continue
                            
            
            curs.execute("SELECT dst from flights where destination == dst")
            rows = curs.fetchall()
                
            if rows == 0:
                print("Not a valid Destination Airport Code")
                curs.execute("SELECT dst, from flights,airports where dst=acode and (city LIKE destination) or (name LIKE destination)"
                     "ORDER BY dst DESC")
                rows = curs.fetchall()
                
                if rows>0:
                    print(rows)
                    num = input("Select row of Destination Airport or Enter Q to search again: ")
                    if (num > 0):
                        source = rows[num]
                        break
                    else:
                        continue
                else:
                    curs.execute("SELECT dst, from flights,airports where dst=acode and (city LIKE destination[0:len(destination)//2] or (name LIKE destination[0:len(destination)//2]"
                             "ORDER BY dst DESC")
                    rows = curs.fetchall()
                    if rows>0:
                        print(rows)
                        num = input("Select row of Destination Airport or Enter Q to search again: ")
                        if (num > 0):
                            source = rows[num]
                            break
                        else:
                            continue
                    else:
                        print("Could not match source airport, please search again")
                        continue





        return



#Not completed functions
#these print statements will clear 10 lines
#to make console more readable
def bookings():
        print("\n"*10)
        return
        
#----------------------------------------------------------
#Preyanshu Part        
#List existing bookings. A user should be able to list all his/her existing bookings. The result will be given in a list form and will include for each booking, the ticket number, the passCancel a booking. The user should be able to select a booking from those listed under "list existing bookings" and cancel it. The proper tables should be updated to reflect the cancelation and the cancelled seat should be returned to the system and is made available for future bookings.enger name, the departure date and the price. The user should be able to select a row and get more detailed information about the booking.
def list_(email, user):
        print("\n"*10)
        while True:
                curs.execute("select t.tno, t.name, s.dep_date, t.paid_price from tickets t, bookings b, passengers p, sch_flights s where t.email="+email+ "and t.tno=b.tno")
        return

#Cancel a booking. The user should be able to select a booking from those listed under "list existing bookings" and cancel it. The proper tables should be updated to reflect the cancelation and the cancelled seat should be returned to the system and is made available for future bookings.
def cancel():
        print("\n"*10)
        return
        
        
#-------------------------------------------------------

#Janice Part


def rec_departure():
	return
def rec_arrival():
	return

#-------------------------------------------------------

#completly finished 
#will log in registered users and register new users
def login():
        print("\n"*10)
        print("WELCOME\n");
        key = input("Press A to Log in or S to Register Or Press Q to exit \n\n\n\t\t\t\t\t")
        
        if (key =='q') or (key =='Q'):
                return key
        elif (key =='a') or (key =='A'):
                
                while True:
                        email1 = input("\nPlease enter your email: ")
                        password = input("\nPlease enter your password: ")
                        curs.execute("SELECT email, from users where email == email1," 
                             "and pass =password")
                
                        rows = curs.fetchall()
                        if rows==1:
                                print("\nWelcome ", email)
                                return email1,key
                        else:
                                print("\n Invalid email or password")
                                do = input("To quit enter Q or any other key to try again: ")
                                if (do =='q') or (do =='Q'):
                                        return do
                        
        elif (key =='s') or (key =='S'):
                email1 = input("\nPlease enter your email: ")
                password = input("\nPlease enter your password: ") 
                
                curs.execute("INSERT INTO users "
                             "VALUES(email1, password, SYSDATE)")    
                print("\nWelcome ", email)
                
        return email1,key
        
        




#Will connect to dbms
#and login/logout is implemented
def main():
       
 
        
        key = login() # 0 is stored in user if user is not an airline agent
        			   # 1 is stored in the user if the user IS an airline agent

        if (key =='q') or (key =='Q'):
                print("Have a nice day, Goodbye")
                return

	#if user == 0:       	 
        while True:
                print("1. Search for flights")
                print("2. Make a booking")
                print("3. List existing bookings")
                print("4. Cancel a booking")
                print("5. Logout")
        
                choice = input("Pick a choice between 1-5: ")
        
                if choice==5:
                        curs.execute("UPDATE users "
                                      "SET(last_login=SYSDATE) where email=email1 ")
                                      
                        Print("Have a nice day, Goodbye")
                        break
                if choice ==3:
                       list_(email1, username)

                if choice ==1:
                	search()

               	if choice ==2:
               		book()

                if (choice>5) or (choice<1):
                        print("Your input is out of range! Enter a choice between 1 to 5")
                     
        
     		
         
        curs.close()

try:
	username = input("Enter the username for sql: ")
	password = input("Ener the password for sql: ")
	connection = cx_Oracle.connect('' +username+ '/' +password+'@gwynne.cs.ualberta.ca:1521/CRS')
	curs = connection.cursor()
	main()
except cx_Oracle.DatabaseError as exc:
	error, =exc.args
	print( sys.stderr, "Oracle code:", error.code)
	print( sys.stderr, "Oracle code:", error.message) 

