import pymysql as sql
import os


conn=sql.connect(host='localhost',user='root',password='',db='summer_training')
cur=conn.cursor()


li=['ID:',"Sender's Name:","Sender's Ph no.:",'Date Time:',"Reciever's Name:","Reciever's Ph no.:",'Destination Address:']

#BOOKING
def booking():
    details=[].copy()

    #sname
    details.append(input("enter sender's name:"))
    #sphno
    details.append(input("enter sender's phone no.:"))
    #rname
    details.append(input("enter receiver's name:"))
    #rphno
    details.append(input("enter receiver's phone no.:"))
    #raddress
    details.append(input("enter destination address:"))

    cur.execute("""INSERT INTO awb VALUES(NULL,%s,%s,NOW(),%s,%s,%s);""",details)

    conn.commit()
    cur.execute("""SELECT MAX(id) FROM awb;""")
    for i in cur.fetchone():
        print('your booking id is:',i)
    x=input('press enter.....')
#TRACKING
def tracking():
    id1=input('enter your booking id:')
    cur.execute("""SELECT max(id) FROM awb""")
    for i in cur.fetchone():
        max1=i
    cur.execute("""SELECT min(id) FROM awb""")
    for i in cur.fetchone():
        min1=i
    if int(id1)>max1 or int(id1)<min1:
        print('invalid id try again')
        x=input('press enter.....') 
        

    else:
        cur.execute("""SELECT * FROM awb WHERE id=%s;""",id1)
        j=0
        for i in cur.fetchone():
            print(li[j],i)
            j+=1
        x=input('press enter.....')    

#LISTING
def listing():
    n=cur.execute("""SELECT * FROM awb;""")
    print('{0:<5} {1:<20} {2:<10}   {3:<22}   {4:<20} {5:<10}    {6:<100}'.format(li[0],li[1],li[2],li[3],li[4],li[5],li[6]))
    print('-'*135)

    for i in range(n):
        t=cur.fetchone()
        print('{0:<5} {1:<20} {2:<18} {3:<25} {4:<19} {5:<28} {6:<100}'.format(t[0],t[1],t[2],str(t[3]),t[4],t[5],t[6]))
            
    x=input('press enter.....')

#EXIT
def exit1():    
    cur.close()
    conn.close()
    x=input('press enter.....')
    

while(1):
    os.system('cls')
    print('MENU\n1.BOOKING\n2.TRACKING\n3.LISTING\n4.EXIT')
    ch=input('enter your choice(1-4):')
    if ch.isnumeric():
        if int(ch)==1:
            booking()
        elif int(ch)==2:
            tracking()
        elif int(ch)==3:
            listing()
        elif int(ch)==4:
            exit1()
            os.system('cls')
            break
        else:
            print('invalid option -try again')
            x=input('press enter.....')    
        
    else:
        print('invalid option -try again')
        x=input('press enter.....')





#EXTRAS
#for creating the table
#cur.execute("""CREATE TABLE awb(id int(6) AUTO_INCREMENT PRIMARY KEY,s_name varchar(20),s_phno int(10),shipment_datetime datetime,r_name varchar(20),r_phno int(10),r_address varchar(100));""")
