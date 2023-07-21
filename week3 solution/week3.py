#Write a python script to perform CRUD operation on following table of "ESM.db" database.

import sqlite3

con=sqlite3.connect("ESM.db")
q="Create table IF NOT EXISTS employee \
                            (eid int primary key,\
                            name text,\
                            dept text,\
                            basic int,\
                            branch text)"
c=con.cursor()
c.execute(q)
con.commit()

#insert through user

q1="insert into employee values (?,?,?,?,?)"
l=[]
for i in range(5):
    a=int(input("Enter id:"))
    name=input("Enter name:")
    dept=input("Enter dept:")
    basic=int(input("Enter basic salary:"))
    branch=input("Enter branch:")
    t=(a,name,dept,basic,branch)
    l.append(t)
c.executemany(q1,l)
con.commit()

#insert directly

q2="insert into employee values (6,'Kusum','It',80000,'Daman'),\
                                (7,'Anuj','Inventory',50000,'Valasad'),\
                                (8,'Prerna','Account',16000,'Bombay'),\
                                (9,'Salma','HR',10000,'Delhi'),\
                                (10,'Duggu','It',1800,'Navvsari')"
c.execute(q2)
con.commit()

#insert through tuple

tupl=[(11,'krish','IT',10000,'vapi'),
      (12,'pooja','HR',12000,'vapi'),
      (13,'priya','HR',9000,'chalthan'),
      (14,'krishna','Account',8000,'Bardoli'),
      (15,'divya','Inventory',5000,'vadodara')]
c.executemany(q1,tupl)
con.commit()

#3 Update records who are from "Surat" branch with increment in salary 10%.

q3="update employee set basic=basic+(basic*10)/100 where branch='surat'"
c.execute(q3)
con.commit()
#4 Print All records.
q4="select*from employee"
c.execute(q4)
print("\n\nOUTPUT:-4\n")
print(c.fetchall())
con.commit()
#5Print records where dept is "HR" and "IT".

q5="select*from employee where dept='HR' or dept='IT'"
c.execute(q5)
print("\n\nOUTPUT:-5\n")
print(c.fetchall())
con.commit()

#6 Print records in sorting order of department.

q6="select*from employee order by dept"
c.execute(q6)
print("\n\nOUTPUT:-6\n")
print(c.fetchall())
con.commit()

#7 Print records where basic is >6000.

q7="select*from employee where basic>6000"
c.execute(q7)
print("\n\nOUTPUT:-7\n")
print(c.fetchall())
con.commit()

#8 Print records whrere employee name second character is "r".

q8="select*from employee where name like '_r%'"
c.execute(q8)
print("\n\nOUTPUT:-8\n")
print(c.fetchall())
con.commit()

#9 Grouping record of employee who are from "Account" and "Inventory".

q9="select dept,count(*) from employee group by dept having dept in('Inventory','Account')"
c.execute(q9)
print("\n\nOUTPUT:-9\n")
print(c.fetchall())
con.commit()

#10Print all records based on branch name in descending order.

q10="select*from employee order by branch desc"
c.execute(q10)
print("\n\nOUTPUT:-10\n")
print(c.fetchall())
con.commit()
con.close()
