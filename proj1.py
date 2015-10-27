# Assignment:           Mini Project 1
# Due Date:             October, 27 2015
# Name:                 Ismail Mare, Janice Loo, Preyanshu Kumar
# Unix ID:              imare, jloo, preyansh
# StudentID:            1388973, 1359624, 1395321
# Lecture Section:      B1
# Instructor:           Davood Rafiei
#---------------------------------------------------------------
#

#importing necessary libraries
import cx_Oracle
import sys
import datetime
import math
import random



#----------------------------------------------------
#Ismail Part
#stuff in red is mostly SQL statements

#Search for flights
#got upto searching for valid src and dst codes from user
# not complete
def search():
        while True:
            source = input("Enter the source: ")
       
            if len(source)==3:
                source = source.upper()
                select="SELECT acode FROM airports WHERE (acode = :source)"
                curs.execute(select,{'source':source})
                rows = curs.fetchall()
		
                if len(rows)==0:
                        print("\nCould not find any flights")
                        return
            else:
                source = '{0:<15}'.format(source)
                source = source.title()
                select="SELECT acode,city FROM airports WHERE (city = :source)"
                curs.execute(select,{'source':source})

                rows = curs.fetchall()
                if len(rows)>0:
                        print('\n')
                        print(rows[0][0] + ": " +rows[0][1])
                        source = input("\nPlease enter the source airport code: ")
                        source = source.upper()
                else:
                    print("\nCould not find any flights MAIN MENU")
                    return
                            
            
            dest = input("\nEnter the destination: ")     
            if len(dest)==3:
                        dest = dest.upper()
                        select = "SELECT acode FROM airports WHERE (acode=:dest)"
                        curs.execute(select, {'dest':dest})
                        rows = curs.fetchall()
                
                        if len(rows)>0:
                	        break
                        else:
                                print("\nCould not find any flights")
                                return
            else:
                        dest = '{0:<15}'.format(dest)
                        dest = dest.title()
                        select="SELECT acode,city  FROM airports WHERE (city = :dest)"
                        curs.execute(select,{'dest':dest})

                        rows = curs.fetchall()
                        if len(rows)>0:

                                print('\n')
                                print(rows[0][0] + ": "+ rows[0][1]) 
                              
                                dest=input("\nPlease enter the destination airport code: ")
                                dest = dest.upper()
                                break
                        else:
                                print("\nCould not find any flights, MAIN MENU")
                                return


        dep_time1 = input("Enter the departure date as 'DD/MM/YYYY': ")	
        choice=input("Sort by number of connections? y/n: ")
        select = "SELECT flightno,src,dst,dep_time,arr_time, price, seats,fare from available_flights1 where to_char(dep_time,'DD/MM/YYYY')=:dep_time1 and src=:source and dst=:dest ORDER BY price"
        curs.execute(select,{'source': source, 'dest':dest,'dep_time1':dep_time1})
        rows_direct=curs.fetchall()

        select = "select flightno1, flightno2, src, dst, dep_date, layover,price from good_connections1 where to_char(dep_date,'DD/MM/YYYY')=:dep_time1 and src=:source and dst=:dest ORDER BY price, layover"
        curs.execute(select,{'source':source, 'dest': dest,'dep_time1':dep_time1})
        rows_connect= curs.fetchall()

        x=0
        for i in range(len(rows_direct)):
                print("%s. %s" % (x, rows_direct[i]))
                x=x+1

        for i in range(len(rows_connect)): 
                print("%s. %s" % (x, rows_direct[i]))	
                x=x+1

        choice=input("\nWhich flight would you like to book or Q to return to menu: ")

        try:
                choice=int(choice)
        except:
                return
        


        name=input("\nEnter your Name: ")
        name='{0: <20}'.format(name)
        select = "select * from users, passengers where name=:name and users.email=passengers.email"
        curs.execute(select,{'name':name})
        rows=curs.fetchall()

        if len(rows)==0:
                country=input("Enter your country: ")
                insert="insert into passengers(email,name,country) VALUES(:email,:name,:country)"
                cursInsert.execute(insert,{'email':email1,'name':name,'country':country})
                connection.commit()


        tno=random.randint(1,1000000) 
        tno1=random.randint(1,1000000)
        if choice<=len(rows_direct):
                print(rows_direct[choice])
                dep_date=rows_direct[choice][3]
                flightno = rows_direct[choice][0]
                price=rows_direct[choice][5]
                seat=rows_direct[choice][6]
                fare = rows_direct[choice][7]

                insert="insert into tickets(tno,name,email,paid_price) VALUES(:tno,:name,:email,:price)"
                cursInsert.execute(insert, {'name': name, 'tno': tno, 'email': email1,'price':price})
                connection.commit()

                insert="insert into bookings(tno,flightno,fare,dep_date,seat) VALUES(:tno,:flightno,:fare,TO_DATE(:dep_date,'DD/MM/YYYY'),NULL)"  
                cursInsert.execute(insert,{'tno': tno,'flightno':flightno,'fare':fare,'dep_date':dep_time1})
                connection.commit()

        elif choice>len(rows_direct):
                flightno1= rows_connect[choice][0]
                flightno2= rows_connect[choice][1]
		
                dep_date=rows_direct[choice][4]
                price=rows_direct[choice][6]

                insert="insert into ticket(tno,name,email,paid_price) VALUES(:tno,:name,:email,:price)"
                cursInsert.execute(insert, {'name': name, 'tno': tno, 'email': email,'price':price})
                connection.commit()

                insert="insert into bookings(tno,flightno,fare,dep_date,seat) VALUES(:tno,:flightno1,:fare,:dep_date,:seat"  
                cursInsert.execute(insert,{'tno': tno,'flightno':flightno,'fare':fare,'dep_date':dep_date,'seat':seat})
                connection.commit()
		
                tno=tno+1

                insert="insert into ticket(tno,name,email,paid_price) VALUES(:tno,:name,:email,:price)"
                cursInsert.execute(insert, {'name': name, 'tno': tno, 'email': email,'price':price})
                connection.commit()

                insert="insert into bookings(tno,flightno,fare,dep_date,seat) VALUES(:tno,:flightno1,NULL,:dep_date,NULL"          
                cursInsert.execute(insert,{'tno': tno,'flightno':flightno,'dep_date':dep_date})
                connection.commit()
		
        print("You have sucessfully booked this flight")	
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
#Cancel a booking. The user should be able to select a booking from those listed under "list existing bookings" and cancel it. The proper tables should be updated to reflect the cancelation and the cancelled seat should be returned to the system and is made available for future bookings. Theoretically these can both be done within the same output, you just have to delete that line from the code.

def list_(email, user):
        print("\n"*10)
        while True:
               #get your query of flights for the user and bind the email to the fed email
               curs=connection.cursor()
               query="SELECT t.tno, t.name, s.dep_date, t.paid_price, b.fare, b.seat,  FROM tickets t, bookings b, passengers p, sch_flights s WHERE t.email=:email and t.tno=b.tno"
               curs.execute(query, {"email":email})
               rows=curs.fetchall()
               if rows == "[]":
                       print("No Bookings Find, Please Book a Flight, Returning to Main Menu")
                       return
               else:
                       for r in range(0,len(rows)):
                               print (r,rows[r:-2])
                       choice=input("Please select a Booking You would like to know more about")
                       choice=int(choice)
                       print(rows[choice])
                       print(rows[choice][1])
                       print(rows[choice][2])
                       print(rows[choice][3])
                       print(rows[choice][4])
                       print(rows[choice][5])
                       tno=(rows[choice][0])
                       #rows[choice]
                       if (choice>0):
                               rows=curs.fetchall()
                               print(rows)
                               curs.close()
                               choice2=str(input("Do you wish to cancel this flight? Yes/No?"))
                               if choice2==("Yes"):
                                       curs=connection.cursor()
                                       print ("Flight has been canceled")
                                       query="DELETE from tickets t WHERE tno= '%d'" % (tno)
                                       curs.execute(query)
                                       connection.commit()
                                       curs.close()
                                       curs=connection.cursor()
                                       query="DELETE from bookings, WHERE tno= '%d'" % (tno)
                                       curs.execute(query)
                                       connection.commit()
                                       curs.close()
                                       print("Returning to Main Menu")
                                       return
                               else:
                                       print("Returning to Main Menu")
                                       return
                       else if (choice.isalpha()):
                               print("Invalid Input, Please enter a Number!")
                               break
                       else:
                               print("No bookings chosen, return to main menu")
                               return
        return
        
        
#-------------------------------------------------------

#Janice Part

def rec_departure_arrival(): 
     fno = input("Please enter the flight number: ")
     dd = input("Please enter the departure date: ")     
     updating = input("Would you like to record the departure or arrival? ")
     auto = input("Would you like to auto-update? ")
     if (updating == departure) or (updating == Departure) or (updating == D) or (updating == d):
          if (auto == Yes) or (auto == yes) or (auto == y) or (auto == Y):
               update = "UPDATE sch_flights SET act_dep_time = TO_CHAR(SYSDATE, HH24:MI:SS) WHERE flightno == :fno AND dep_date == :dd"
               curs.execute(update,{'fno':fno, 'dd':dd})
               print("Auto-update successful. ")
               
          else:
               #offer to change time first to reduce chances of errors if departure date was changed first
               change_t = input("Would you like to change the time? ")
               if (change_t == Yes) or (change_t == yes) or (change_t == Y) or (change_t == y):
                    time = input("Please enter the new departure time (HH24:MI:SS): ")
                    update = "UPDATE sch_flights SET act_dep_time = time WHERE flightno == fno AND dep_date == dd"
                    curs.execute(update,{'time':time, 'fno':fno, 'dd':dd})
                    print("Departure time updated. ")
               
               else:
                    change_d = input("Would you like to change the date? ")
                    if (change_d == Yes) or (change_d == yes) or (change_d == Y) or (change_d == y):
                         date = input("Please enter the new departure date (DD/MM/YYYY): ")
                         update = "UPDATE sch_flights SET dep_date = date WHERE flightno == fno AND dep_date == dd"
                         curs.execute(update,{'date':date, 'fno':fno, 'dd':dd})
                         print("Departure date updated. ")
                    else:
                         return
     
     elif (updating == arrival) or (updating == Arrival) or (updating == A) or (updating == a):
          if (auto == Yes) or (auto == yes) or (auto == y) or (auto == Y):
               update = "UPDATE sch_flights SET act_arr_time = TO_CHAR(SYSDATE, HH24:MI:SS) WHERE flightno == fno AND dep_date == dd"
               curs.execute(update,{'fno':fno, 'dd':dd})
               print("Auto-update successful. ")
          
          else:
               atime = input("Please enter the arrival time (HH24:MI:ss): ")
               update = "UPDATE sch_flights SET act_arr_time = atime WHERE flightno == fno AND dep_date == dd"
               curs.execute(update,{'atime':atime, 'fno':fno, 'dd':dd})
               print("Arrival time updated. ")
               
     else:
          print("Invalid, please try again. ")
          return
     
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
        tno=1000
        key = login() # 0 is stored in user if user is not an airline agent
        			   # 1 is stored in the user if the user IS an airline agent

        if (key =='3'):
                print("\nHave a nice day, Goodbye")
                curs.close()
                cursInsert.close()
                return
        curs.execute("drop view available_flights1")
        curs.execute("drop view good_connections1")

        curs.execute("create view available_flights1 (flightno,dep_date, src,dst,dep_time,arr_time,fare,seats,price) as select f.flightno, sf.dep_date, f.src, f.dst, f.dep_time+(trunc(sf.dep_date)-trunc(f.dep_time)), f.dep_time+(trunc(sf.dep_date)-trunc(f.dep_time))+(f.est_dur/60+a2.tzone-a1.tzone)/24,fa.fare, fa.limit-count(tno), fa.price from flights f, flight_fares fa, sch_flights sf, bookings b, airports a1, airports a2 where f.flightno=sf.flightno and f.flightno=fa.flightno and f.src=a1.acode and f.dst=a2.acode and fa.flightno=b.flightno(+) and fa.fare=b.fare(+) and sf.dep_date=b.dep_date(+) group by f.flightno, sf.dep_date, f.src, f.dst, f.dep_time, f.est_dur,a2.tzone,a1.tzone, fa.fare, fa.limit, fa.price having fa.limit-count(tno) > 0")

        curs.execute("create view good_connections1 (src,dst,dep_date,flightno1,flightno2, layover,price) as select a1.src, a2.dst, a1.dep_date, a1.flightno, a2.flightno, a2.dep_time-a1.arr_time,min(a1.price+a2.price) from available_flights1 a1, available_flights1 a2 where a1.dst=a2.src and a1.arr_time +1.5/24 <=a2.dep_time and a1.arr_time +5/24 >=a2.dep_time group by a1.src, a2.dst, a1.dep_date, a1.flightno, a2.flightno, a2.dep_time, a1.arr_time")



	#if user == 0:
        try:
                key=int(key)       	  
        except:
                print("Not a valid option")
                return
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

