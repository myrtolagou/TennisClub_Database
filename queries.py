import sqlite3,os,time
from datetime import datetime

global conn,cursor
conn=sqlite3.connect("TennisClub.db")
cursor=conn.cursor()
print("\n Επιτυχής σύνδεση στη βάση")


while True:
    os.system('cls')
    ch=input("""\nΕπιλέξτε ένα από τα παρακάτω ερωτήματα!
1.Εύρεση πλήθους προπονήσεων ανά προπονητή,το μήνα που επιθυμεί ο χρήτης.
2.Πρόγραμμα αγώνων.
3.Εμφάνιση συμμετεχόντων ανά ομάδα.
4.Εμφάνιση μελών που προπονεί ο προπονητής που επιθυμεί ο χρήστης.
5.Εύρεση διαθέσιμων προπονητών την ημερομηνία και ώρα που επιθυμεί ο χρήστης.
6.Εύρεση διαθέσιμων γηπέδων την ημερομηνία και ώρα που επιθυμεί ο χρήστης.
7.Εύρεση μέσης διάρκειας αγώνων των νικητών του διπλού Τουρνουά Νοεμβρίου 2022.
8.Εύρεση του πλήθους των ατομικών και των ομαδικών προπονήσεων κάθε μέλους.\n""")

    if(ch=="1"):
        os.system('cls')
        month=input("\nΕισάγετε τον επιθυμητό μήνα(01-12):")
        cursor.execute("""SELECT first_name,last_name,count(id_coach) as ar_prop
FROM Coach natural join Reserves
Where strftime("%m",reservation_date)=?
GROUP by id_coach
ORDER BY ar_prop ASC;""",(month,))
        data=cursor.fetchall()
        style="{:<16}{:<16}{:<2}"
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα για τη δοθείσα τιμή")
        else:
            print(style.format("First_name","Last_name","plithos_proponhsewn"))
            for i in data:
                print(style.format(i[0],i[1],i[2]))
        input("\nΠατήστε Enter για να συνεχίσετε!")
                
    if(ch=="2"):
        os.system('cls')
        cursor.execute("""SELECT gamedate,home.team_name as home_name ,final_score,away.team_name as away_name
FROM Game 
join player as h on home_id=h.id_player
join player as a on away_id=a.id_player
join team as home on h.id_player=home.id_team
join team as away on a.id_player=away.id_team
UNION
SELECT gamedate,home.first_name||' '||home.last_name as home_name,final_score,away.first_name||' '||away.last_name as away_name
FROM Game 
join player as h on home_id=h.id_player
join player as a on away_id=a.id_player
join Member as home on h.id_player=home.id_member
join Member as away on a.id_player=away.id_member
order by gamedate ASC;""")
        data=cursor.fetchall()
        style="{:<12}{:<30}{:<13}{:<25}"
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα ")
        else:
            print(style.format("Gamedate","Home_team","final_score","Away_team"))
            for i in data:
                print(style.format(i[0],i[1],i[2],i[3]))
        input("\nΠατήστε Enter για να συνεχίσετε!")

    if(ch=="3"):
        os.system('cls')
        cursor.execute("""SELECT team_name,first_name, last_name
from Member NATURAL join Participates  
natural join Team
order by team_name;""")
        data=cursor.fetchall()
        style="{:<12}{:<15}{:<15}"
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα")
        else:
            print(style.format("team_name","first_name", "last_name"))
            for i in data:
                print(style.format(i[0],i[1],i[2]))
        input("\nΠατήστε Enter για να συνεχίσετε!")

    if(ch=="4"):
        os.system('cls')
        coach=input("\nΕισάγετε τον επιθυμητό προπονητή(1-6):")
        cursor.execute("""SELECT distinct first_name, last_name
from Member NATURAL join Reserves
where id_coach=?;""",(coach,))
        data=cursor.fetchall()
        style="{:<15}{:<15}"
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα για τη δοθείσα τιμή")
        else:
            print(style.format("first_name", "last_name"))
            for i in data:
                print(style.format(i[0],i[1]))
        input("\nΠατήστε Enter για να συνεχίσετε!")


    if(ch=="5"):
        os.system('cls')
        while True:
            try:
                date=input("\nΕισάγετε την επιθυμητή ημερομηνία(YYYY-MM-DD):")
                date=datetime.strptime(date,"%Y-%m-%d")
                break
            except:
                print("\nΛάθος μορφή ημερομηνίας.Προσπαθήστε ξανά!")
        hour=input("\nΕισάγετε την επιθυμητή ώρα(HH):")
        cursor.execute("""select DISTINCT first_name, last_name 
from Coach
where id_coach not in (
select DISTINCT id_coach
from Reserves natural join Coach
where strftime("%Y-%m-%d",reservation_date)=?
AND (strftime("%H",?) BETWEEN strftime("%H",start_time) and strftime("%H",ending_time))
);""",(date,hour))
        data=cursor.fetchall()
        style="{:<15}{:<15}"
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα για τη δοθείσα τιμή")
        else:
            print(style.format("first_name", "last_name"))
            for i in data:
                print(style.format(i[0],i[1]))
        input("\nΠατήστε Enter για να συνεχίσετε!")

    if(ch=="6"):
        os.system('cls')
        while True:
            try:
                date=input("\nΕισάγετε την επιθυμητή ημερομηνία(YYYY-MM-DD):")
                date=datetime.strptime(date,"%Y-%m-%d")
                break
            except:
                 print("\nΛάθος μορφή ημερομηνίας.Προσπαθήστε ξανά!")
        hour=input("\nΕισάγετε την επιθυμητή ώρα(HH):")
        cursor.execute("""SELECT DISTINCT court_number
FROM Court
WHERE court_number not in (
SELECT DISTINCT court_number
FROM Reserves 
WHERE strftime("%Y-%m-%d",reservation_date)=?
AND (strftime("%H",?) BETWEEN strftime("%H",start_time) and strftime("%H",ending_time))
);""",(date,hour))
        data=cursor.fetchall()
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα για τη δοθείσα τιμή")
        else:
            print("court_number")
            for i in data:
                print(i[0])
        input("\nΠατήστε Enter για να συνεχίσετε!")
    
        
    if(ch=="7"):
        os.system('cls')
        cursor.execute("""SELECT team_name as winner,round( AVG (julianday(ending_time)- julianday(start_time))*24*60,3) as mesh_diarkeia_agwnwn
from Game NATURAL JOIN Tournament
join Player on winner_female=id_player
join Team on id_player=id_team
where home_id=winner_female or away_id=winner_female
UNION
SELECT team_name as winner,round( AVG (julianday(ending_time)- julianday(start_time))*24*60,3) as mesh_diarkeia_agwnwn
from Game NATURAL JOIN Tournament
join Player on winner_male=id_player
join Team on id_player=id_team
where home_id=winner_male or away_id=winner_male;""")
        data=cursor.fetchall()
        style="{:<15}{:<5}"
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα")
        else:
            print(style.format("winner","mesh_diarkeia_agwnwn"))
            for i in data:
                print(style.format(i[0],i[1]))
        input("\nΠατήστε Enter για να συνεχίσετε!")
        
    if(ch=="8"):
        os.system('cls')
        cursor.execute("""SELECT first_name,last_name,
count(CASE WHEN number_of_members=1 THEN 1 ELSE NULL END )as atomikes_prop,
count(CASE when number_of_members!=1 THEN 1 ELSE NULL END ) as omadikes_prop
FROM member natural JOIN Reserves WHERE
id_coach is not NULL GROUP by id_member;""")
        data=cursor.fetchall()
        style="{:<15}{:<18}{:<15}{:<15}"
        if(len(data)==0):
            print("\nΔεν βρέθηκαν αποτελέσματα ")
        else:
            print(style.format("first_name","last_name","atomikes_prop","omadikes_prop"))
            for i in data:
                print(style.format(i[0],i[1],i[2],i[3]))
        input("\nΠατήστε Enter για να συνεχίσετε!")





        
