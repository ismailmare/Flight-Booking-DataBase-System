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
            dest = input("Enter the destination: ")
            departure = input("Enter the departure date as 'YYYY-MM-DD': ")
       
            if len(source)==3:
                source = source.upper()
                select="SELECT acode FROM airports WHERE (acode = :source)"
                curs.execute(select,{'source':source})
                rows = curs.fetchall()
		
                if len(rows)>0:
                        continue
                else:
                        print("\nCould not find any flights")
                        return
            else:
                source = '{0:<20}'.format(source)
                source = source.title()
                select="SELECT acode FROM airports WHERE (city = :source)"
                curs.execute(select,{'source':source})

                rows = curs.fetchall()
                if len(rows)>0:
                        print(rows)
                        source = input("\nPlease enter the airport code")
                        source = source.upper()
                        continue
                else:
                    print("\nCould not find any flights")
                    return
                            
            
                
            if len(dest)==3:
                        dest = dest.upper()
                        select = "SELECT acode FROM flights airports WHERE (acode=:dest)"
                        curs.execute(select, {'dest':dest})
                        rows = curs.fetchall()
                
                        if len(rows)>0:
                	        continue
                        else:
                                print("\nCould not find any flights")
                                return
            else:
                        dest = '{0:<20}'.format(source)
                        dest = source.title()
                        select="SELECT acode FROM airports WHERE city = :dest"
                        curs.execute(select,{'dest':dest})

                        rows = curs.fetchall()
                        if len(rows)>0:
                                print(rows)    
                                dest=input("\nPlease enter the airport code")
                                dest = dest.upper()
                                continue
                        else:
                 	        print("\nCould not find any flights")
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
               query="SELECT t.tno, t.name, s.dep_date, t.paid_price FROM tickets t, bookings b, passengers p, sch_flights s WHERE t.email=:email and t.tno=b.tno"
               curs.execute(query, {"email":email})
               rows=curs.fetchall()
               if rows == "[]":
                       print("No Bookings Find, Please Book a Flight, Returning to Main Menu")
                       break
               else:
                       for r in range(0,len(rows)):
                               print (r,rows[r:-3])
                        choice=input("Please select a Booking You would like to know more about")
                        if (choice>0):
                                rows=curs.fetchone()
                                print(rows)
                                
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
        print("WELCOME\n")
 
        print("1. Enter 1 to log in\n")
        print("2. Enter 2 to register\n")
        print("3. Enter 3 to exit\n")
        key = input("Please choose an option: ")
        
        if (key =='3'):
                return key
        elif (key =='1'):
                
                while True:
                        global email1
                        global password
                        email1 = input("\nPlease enter your email: ")
                        password = input("\nPlease enter your password: ")
                        email1='{0: <20}'.format(email1)
                        password='{0: <4}'.format(password)
                        select="SELECT email FROM users WHERE (email=:email1) and (pass=:password)"
                        curs.execute(select, {'email1': email1, 'password':password})
			
                        rows = curs.fetchall()
                        if len(rows)>0:
                                print("\nWelcome ", email1)
                                select="select email FROM airline_agents WHERE (email=:email1)"
                                curs.execute(select,{'email1':email1})
                                rows=curs.fetchall()
                                if len(rows)>0:
                                        return 0
                                else:
                                        return key
                        else:
                                print("\n Invalid email or password")
                                do = input("To quit enter Q or any other key to try again: ")
                                if (do =='q') or (do =='Q'):
                                        return '3'
                        
        elif (key =='2'):
                email1 = input("\nPlease enter your email: ")
                password = input("\nPlease enter your password: ") 
                
                insert="insert into users(email,pass,last_login) VALUES(:email1,:password,SYSDATE)"
                cursInsert.execute(insert, {'email1': email1, 'password': password})
                connection.commit()
                print("\nWelcome ", email1)
                
        return key
        
        




#Will connect to dbms
#and login/logout is implemented
def main(): 
        key = login() # 0 is stored in user if user is not an airline agent
        			   # 1 is stored in the user if the user IS an airline agent

        if (key =='3'):
                print("\nHave a nice day, Goodbye")
                curs.close()
                cursInsert.close()
                return

	#if user == 0:
        key=int(key)       	 
        while key>0:
                print("\n1. Search for flights")
                print("2. List existing bookings")
                print("3. Logout")
        
                choice = input("Pick a choice between 1-3: ")
       
                choice=int(choice) 
                if choice==3:
                        curs.prepare("UPDATE users SET last_login=SYSDATE where email=:email1")
                        curs.execute(None, {'email1': email1})
                                      
                        print("Have a nice day, Goodbye")
                        break
                if choice ==2:
                       list_(email1, username)

                if choice ==1:
                	search()

                if (choice>3) or (choice<1):
                        print("\nYour input is out of range! Enter a choice between 1 to 3")
                   
        while key==0:
                print("\n1. Search for flights")
                print("2. List existing bookings")
                print("3. Logout")
                print("4. Record a flight departure")
                print("5. Record a fligh arrival")
                choice = input("Pick a choice between 1-5: ")

                choice=int(choice)
                if choice==3:
                        curs.prepare("UPDATE users SET last_login=SYSDATE where email=:email1")
                        curs.execute(None, {'email1': email1})

                        print("Have a nice day, Goodbye")
                        break
                elif choice ==2:
                       list_(email1, username)

                elif choice ==1:
                        search()

                elif choice==4:
                        record_dep()

                elif choice==5:
                        record_arr()
			
			
                elif (choice>5) or (choice<1):
                        print("\nYour input is out of range! Enter a choice between 1 to 5")

     		
         
        curs.close()
        cursInsert.close()	

try:
	username = input("\n\nEnter the username for sql: ")
	password = input("Ener the password for sql: ")
	connection = cx_Oracle.connect('' +username+ '/' +password+'@gwynne.cs.ualberta.ca:1521/CRS')
	curs = connection.cursor()
	cursInsert = connection.cursor()
	main()
except cx_Oracle.DatabaseError as exc:
	error, =exc.args
	print( sys.stderr, "Oracle code:", error.code)
	print( sys.stderr, "Oracle code:", error.message) 

