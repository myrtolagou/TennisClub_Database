import sqlite3,os,time
from datetime import datetime,timedelta


def createDatabase():
    import TennisClub_Sql
    print("Η Βάση Δεδομένων Tennis Club δημιουργήθηκε με επιτυχία!\n")


def loadDataInDatabase():
    import TennisClub_Data
    print("Τα δεδομένα φορτώθηκαν με επιτυχία\n")


def insertData():
    global conn,cursor
    conn=sqlite3.connect("TennisClub.db")
    os.system('cls')  
    cursor=conn.cursor()
    ch=input("""\n1.Εισαγωγή νέου μέλους
2.Εισαγωγή νέου προπονητή
3.Εισαγωγή κράτησης
4.Εισαγωγή ενοικίασης εξοπλισμού
5.Εισαγωγή παίκτη σε αγωνιστική ομάδα
6.Εισαγωγή εγγραφής παίκτη σε τουρνουά
7.Εισαγωγή νέου τουρνουά
8.Εισαγωγή νέου αγώνα
Πατήστε Enter για να επιστρέψετε στο αρχικό μενού\n\n""")
    
    if (ch=="1"):
        try:
            os.system('cls')

            print("\nΕισάγετε τα στοιχεία του μέλους.\n\n")
            member_first_name = input("Όνομα:")
            member_last_name = input("\nΕπώνυμο:")
            birthdate = input("\nΗμερομηνία γέννησης(YYYY-MM-DD):")
            birthdate=datetime.strptime(birthdate,"%Y-%m-%d")
            identity_number = input("\nΑριθμός ταυτότητας:")
            member_phone_number = int(input("\nΑριθμός τηλεφώνου:"))
            address = input("\nΔιεύθυνση κατοικίας:")
            gender = input("\nΦύλο ('Θ' για θηλυκό και 'Α' για αρσενικό):")
            while True:
                if(gender!="Θ" and gender!="Α"):
                    gender = input("\nΜη έγκυρο, εισάγετε ξανά.\nΦύλο ('Θ' για θηλυκό και 'Α' για αρσενικό)\n")
                else:
                    break
        
            conn.execute("INSERT INTO Member (id_member,first_name,last_name,birthdate,identity_number,phone_number,address,gender) VALUES(?,?,?,?,?,?,?,?)",(None,member_first_name,member_last_name,birthdate.strftime("%Y-%m-%d"),identity_number,member_phone_number,address,gender))
            conn.commit()
            cursor.execute("SELECT id_member FROM Member WHERE first_name='"+member_first_name+"' AND last_name='"+member_last_name+"';")
            res=cursor.fetchone()
            player_id=res[0]
            print(player_id)
            conn.execute("INSERT INTO Player (id_player) VALUES(?)",(player_id,))
            conn.commit()

            print("\nΕπιτυχής εισαγωγή δεδομένων!")
            time.sleep(2)
              
        except:
            print("\nΛάθος τιμές!\n")
            time.sleep(1)

    elif (ch=="2"):
        try:
            os.system('cls')
            print("\nΕισάγετε τα στοιχεία του προπονητή.\n\n")
            coach_first_name = input("Όνομα:")
            coach_last_name = input("\nΕπώνυμο:")
            coach_phone_number = int(input("\nΑριθμός τηλεφώνου:"))
            birthdate = input("\nΗμερομηνία γέννησης(YYYY-MM-DD):")
            birthdate=datetime.strptime(birthdate,"%Y-%m-%d")
            
            conn.execute("INSERT INTO Coach (id_coach,first_name,last_name,phone_number,birthdate) VALUES(?,?,?,?,?)",(None,coach_first_name,coach_last_name,coach_phone_number,birthdate.strftime("%Y-%m-%d")))
            conn.commit()

            print("\nΕπιτυχής εισαγωγή δεδομένων!")
            time.sleep(2)
        except:
            print("\nΛάθος τιμές!\n")
            time.sleep(1)

    elif (ch=="3"):
        try:
            os.system('cls')
            print("\nΕισάγετε τα στοιχεία της κράτησης.\n\n")
            while True:
                member_name = input("Εισάγετε το ονοματεπώνυμο του μέλους:")
                cursor.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+member_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΤο μέλος που εισάγατε δεν υπάρχει")
                else:
                    res_id_member = sel[0]
                    break
          
            while True:
                coach_name = input("\nΕισάγετε το ονοματεπώνυμο του προπονητή:")
                cursor.execute("SELECT id_coach FROM Coach WHERE first_name||' '||last_name='"+coach_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΟ προπονητής που εισάγατε δεν υπάρχει")
                else:
                    res_id_coach = sel[0]
                    break

            while True:
                res_court_number = input("\nΕπιλέξτε ένα γήπεδο από τα παρακάτω.\n  1.Χωμάτινο Γήπεδο\n  2.Χωμάτινο Γήπεδο\n  3.Χωμάτινο Γήπεδο\n  4.Γήπεδο με γρασίδι\n  5.Γήπεδο με γρασίδι\n  6.Σκληρό γήπεδο\n\nΑριθμός γηπέδου:")
                cursor.execute("SELECT court_number from Court WHERE court_number="+res_court_number+";")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΤο γήπεδο που εισάγατε δεν υπάρχει")
                else:
                    res_court_number = sel[0]
                    break
                
            res_date = input("\nΗμερομηνία κράτησης(YYYY-MM-DD):")
            res_date=datetime.strptime(res_date,"%Y-%m-%d")
            start_time=input("\nΏρα έναρξης(HH):")
            res_start_time = datetime.strptime(start_time,"%H")
            res_ending_time = res_start_time + timedelta(hours=1,minutes=30)
            res_number_of_members = int(input("\nΑριθμός μελών που θα αθληθούν:"))
            
            conn.execute("INSERT into Reserves (id_member,id_coach,court_number,reservation_date,start_time,ending_time,number_of_members) VALUES(?,?,?,?,?,?,?)",(res_id_member,res_id_coach,res_court_number,res_date.strftime("%Y-%m-%d"),res_start_time.strftime("%H:%M:%S"),res_ending_time.strftime("%H:%M:%S"),res_number_of_members))
            conn.commit()
            print("\nΕπιτυχής εισαγωγή δεδομένων!")
            time.sleep(2)
        except:
            print("\nΛάθος τιμές!\n")
            time.sleep(1)

    elif (ch=="4"):
        try:
            os.system('cls')
            print("\nΕισάγετε τα στοιχεία της ενοικίασης.")
            while True:
                member_name = input("\nΕισάγετε το ονοματεπώνυμο του μέλους:")
                cursor.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+member_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΤο μέλος που εισάγατε δεν υπάρχει")
                else:
                    r_id_member = sel[0]
                    break
                
            while True:   
                r_id_racket = input("\nΚωδικός ρακέτας(1-20):")
                cursor.execute("SELECT id_eq FROM Equipment WHERE id_eq="+r_id_racket+";")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΟ κωδικός εξοπλισμού που εισάγατε δεν υπάρχει")
                else:
                    r_id_racket = sel[0]
                    break
                
            while True:
                r_id_balls = input("\nΚωδικός για σετ μπαλάκια(x3)(21-34):")
                cursor.execute("SELECT id_eq FROM Equipment WHERE id_eq="+r_id_balls+";")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΟ κωδικός εξοπλισμού που εισάγατε δεν υπάρχει")
                else:
                    r_id_balls = sel[0]
                    break
    
            res_date = input("\nΗμερομηνία κράτησης(YYYY-MM-DD):")
            res_date=datetime.strptime(res_date,"%Y-%m-%d")
            start_time=input("\nΏρα έναρξης(HH):")
            res_start_time = datetime.strptime(start_time,"%H")
            res_ending_time = res_start_time + timedelta(hours=1,minutes=30)
            conn.execute("INSERT into Rents (id_member,id_racket,id_balls,reservation_date,start_time,ending_time) VALUES(?,?,?,?,?,?)",(r_id_member,r_id_racket,r_id_balls,res_date.strftime("%Y-%m-%d"),res_start_time.strftime("%H:%M:%S"),res_ending_time.strftime("%H:%M:%S")))
            conn.commit()
            print("\nΕπιτυχής εισαγωγή δεδομένων!")
            time.sleep(2)
            
          
        except:
            print("\nΛάθος τιμές!\n")
            time.sleep(1)


    elif (ch=="5"):
        try:
            while True:
                member_name = input("\nΕισάγετε ονοματεπώνυμο μέλους:")
                cursor.execute("SELECT id_member FROM Member  WHERE first_name||' '||last_name='"+member_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΤο μέλος που εισάγατε δεν υπάρχει")
                else:
                    t_id_member = sel[0]
                    break

            t_team_name = input("\nΕισάγετε όνομα ομάδας:")
            cursor.execute("SELECT id_team FROM Team WHERE team_name='"+t_team_name+"';")
            sel = cursor.fetchone()
            if(sel==None):
                conn.execute("INSERT into Team (id_team,team_name) VALUES(?,?)",(None,t_team_name))
                conn.commit()
                cursor.execute("SELECT id_team FROM Team WHERE team_name='"+t_team_name+"';")
                sel = cursor.fetchone()
            t_id_team = sel[0]
            conn.execute("INSERT INTO Player (id_player) VALUES(?)",(t_id_team,))
            conn.commit()
            cursor.execute("SELECT team_name, COUNT(id_team) FROM Participates natural join Team WHERE id_team="+str(t_id_team)+" group by id_team;")
            sel2 = cursor.fetchone()
            if (sel2==None):
                conn.execute("INSERT into Participates (id_team,id_member) VALUES(?,?)",(t_id_team,t_id_member))
                conn.commit()
                print("\nΕπιτυχής εισαγωγή δεδομένων!")
                time.sleep(2)
            else:
                plithos=sel2[1]
                if(plithos<2):
                    conn.execute("INSERT into Participates (id_team,id_member) VALUES(?,?)",(t_id_team,t_id_member))
                    conn.commit()
                    print("\nΕπιτυχής εισαγωγή δεδομένων!")
                    time.sleep(2)
                else:
                    print("\nΗ ομάδα είναι πλήρης!")
            
        except:
              print("\nΛάθος τιμές!\n")
              time.sleep(1)

          

    elif (ch=="6"): 
        try:
            os.system('cls')
            print("\nΔήλωση συμμετοχής παίκτη σε τουρνουά.")
            while True:
                s_tournament_name = input("\nΕισάγετε όνομα τουρνουά:")
                cursor.execute("SELECT tournament_name FROM Tournament WHERE tournament_name='"+s_tournament_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΤο όνομα τουρνουά που εισάγατε δεν υπάρχει")
                else:
                    s_tournament_name = sel[0]
                    break

            cursor.execute("SELECT category FROM Tournament WHERE tournament_name='"+s_tournament_name+"';")
            sel2 = cursor.fetchone()
            s_category = sel2[0]
            if(s_category=="Διπλό"):
                while True:
                    team_name = input("\nTο τουρνουά είναι διπλό.\nΔήλωση ονόματος ομάδας:")
                    cursor.execute("SELECT id_player FROM Player join Team on id_player=id_team WHERE team_name='"+team_name+"';")
                    sel3 = cursor.fetchone()
                    if(sel3==None):
                        print("\nH ομάδα που εισάγατε δεν υπάρχει")
                    else:
                        s_id_player = sel3[0]
                        break

                cursor.execute("SELECT id_player FROM SignsUp WHERE id_player="+str(s_id_player)+" AND tournament_name='"+s_tournament_name+"';")
                sel4 = cursor.fetchone()
                if(sel4==None):
                    conn.execute("INSERT into SignsUp (id_player,tournament_name) VALUES(?,?)",(s_id_player,s_tournament_name))
                    conn.commit()
                else:
                    print("\nΗ ομάδα είναι ήδη εγγεγραμμένη στο τουρνουά!")
                    
                
            elif(s_category=="Μονό"):
                member_name = input("\nΤο τουρνουά είναι μονό.\nΔήλωση ονοματεπώνυμο μέλους:")
                cursor.execute("SELECT id_player FROM Player join Member on id_player=id_member WHERE first_name||' '||last_name='"+member_name+"';")
                sel3 = cursor.fetchone()
                if(sel3==None):
                    print("\nΤο μέλος που εισάγατε δεν υπάρχει")
                else:
                    s_id_player = sel3[0]

                cursor.execute("SELECT id_player FROM SignsUp WHERE id_player="+str(s_id_player)+" AND tournament_name='"+s_tournament_name+"';")
                sel4 = cursor.fetchone()
                if(sel4==None):
                    conn.execute("INSERT into SignsUp (id_player,tournament_name) VALUES(?,?)",(s_id_player,s_tournament_name))
                    conn.commit()
    
                else:
                    print("\nΟ παίκτης είναι ήδη εγγεγραμμένος στο τουρνουά!")
          
        except:
            print("\n Λάθος τιμές \n")


          

    elif (ch=="7"):
        try:
            os.system('cls')
            print("\nΕισάγετε τα στοιχεία του τουρνουά.")
            t_tournament_name = input("\nΌνομα τουρνουά:")
            t_category = input("\nΤύπος τουρνουά (Διπλό/Μονό):")
            t_start_date = input("\nΗμερομηνία έναρξης(YYYY-MM-DD):")
            t_start_date=datetime.strptime(t_start_date,"%Y-%m-%d")
            t_ending_date = input("\nΗμερομηνία λήξης(YYYY-MM-DD):")
            t_ending_date =datetime.strptime(t_ending_date,"%Y-%m-%d")
            t_participants = int(input("\nΑριθμός συμμετοχών:"))
            t_prize = input("\nΈπαθλο:")
            while True:
                male_winner=input("\nΕισάγεται το νικητή αντρών.")
                female_winner=input("\nΕισάγεται το νικητή γυναικών.")
                if(male_winner=='' and female_winner==''):
                    male_winner=None
                    female_winner=None
                else:
                    if(t_category=="Μονό"):
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Member on id_member=id_player where tournament_name=? AND first_name||' '||last_name=?;",(t_tournament_name,male_winner))
                        sel1=fetchone()
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Member on id_member=id_player where tournament_name=? AND first_name||' '||last_name=?;",(t_tournament_name,female_winner))
                        sel2=fetchone()
                        if(sel1==None):
                            print("\nΟ παίκτης δεν είναι εγγεγραμένος στο τουρνουά")
                        else:
                            male_id=sel1[0]
                            female_id=sel2[0]
                            break
                    elif(t_category=="Διπλό"):
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Team on id_team=id_player where tournament_name=? AND team_name=?;",(t_tournament_name,male_winner))
                        sel1=fetchone()
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Team on id_team=id_player where tournament_name=? AND team_name=?;",(t_tournament_name,female_winner))
                        sel2=fetchone()
                        if(sel1==None):
                            print("\nΗ ομάδα δεν είναι εγγεγραμένη στο τουρνουά")
                        else:
                            male_id=sel1[0]
                            female_id=sel2[0]
                            break
                    
                
            conn.execute("INSERT into Tournament (tournament_name,category,start_date,ending_date,participants,prize,winner_female,winner_male) VALUES(?,?,?,?,?,?,?,?)",(t_tournament_name,t_category,t_start_date.strftime("%Y-%m-%d"),t_ending_date.strftime("%Y-%m-%d"),t_participants,t_prize,female_id,male_id))
            conn.commit()

        except:
            print("\nΛάθος τιμές!\n")

    elif (ch=="8"):
        try:
            os.system('cls')
            print("\nΕισάγετε τα στοιχεία του αγώνα.\n\n")
            while True:
                g_tournament_name = input("\nΌνομα Τουρνουά:")
                cursor.execute("SELECT tournament_name FROM Tournament WHERE tournament_name='"+g_tournament_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΤο τουρνουά που εισάγατε δεν υπάρχει")
                else:
                    g_tournament_name = sel[0]
                    break
                
            cursor.execute("SELECT category FROM Tournament WHERE tournament_name='"+g_tournament_name+"';")
            sel2 = cursor.fetchone()
            s_category = sel2[0]
            if(s_category=="Διπλό"):
                while True:
                    home_name = input("\nTο τουρνουά είναι διπλό.\nΔήλωση ονόματος  γηπεδούχου ομάδας:")
                    cursor.execute("SELECT id_player FROM SignsUp natural join Player join Team on id_player=id_team WHERE team_name='"+home_name+"';")
                    sel3 = cursor.fetchone()
                    if(sel3==None):
                        print("\nH ομάδα που εισάγατε δεν υπάρχει")
                    else:
                        s_id_home = sel3[0]
                        break
                while True:
                    away_name = input("Δήλωση ονόματος φιλοξενούμενης ομάδας:")
                    cursor.execute("SELECT id_player FROM SignsUp natural join Player join Team on id_player=id_team WHERE team_name='"+away_name+"';")
                    sel4 = cursor.fetchone()
                    if(sel4==None):
                        print("\nH ομάδα που εισάγατε δεν υπάρχει")
                    else:
                        s_id_away = sel4[0]
                        break
                    
            elif(s_category=="Μονό"):
                while True:
                    home_name = input("\nTο τουρνουά είναι μονό.\nΔήλωση ονόματος  γηπεδούχου:")
                    cursor.execute("SELECT id_player FROM SignsUp natural join Player join Member on id_player=id_member WHERE first_name||' '||last_name='"+home_name+"';")
                    sel3 = cursor.fetchone()
                    if(sel3==None):
                        print("\nΤο μέλος που εισάγατε δεν υπάρχει")
                    else:
                        s_id_home = sel3[0]
                        break
                while True:
                    away_name = input("Δήλωση ονόματος φιλοξενούμενου:")
                    cursor.execute("SELECT id_player FROM SignsUp natural join Player join Member on id_player=id_member WHERE first_name||' '||last_name='"+away_name+"';")
                    sel4 = cursor.fetchone()
                    if(sel4==None):
                        print("\nΤο μέλος που εισάγατε δεν υπάρχει")
                    else:
                        s_id_away = sel4[0]
                        break
            
            while True:
                g_court_number = input("\nΚωδικός γηπέδου:")
                cursor.execute("SELECT court_number FROM Court WHERE court_number="+g_court_number+";")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nΤο γήπεδο που εισάγατε δεν υπάρχει")
                else:
                    g_court_number = sel[0]
                    break
            
            g_gamedate = input("\nΗμερομηνία:")
            g_gamedate=datetime.strptime(g_gamedate,"%Y-%m-%d")
            g_start_time = input("\nΏρα έναρξης:")
            g_start_time=datetime.strptime(g_start_time,"%H")
            g_ending_time = input("\nΏρα λήξης:")
            if(g_ending_time==''):
                g_ending_time=None
            else:
                g_ending_time=datetime.strptime(g_start_time,"%H:%M")
                g_ending_time= g_ending_time.strftime("%H:%M:%S")
            g_final_score = input("\nΤελικό σκορ:")
            if(g_final_score==''):
                g_final_score=None
            while True:
                g_winner_id = input("\nΕισάγετε 1 αν κέρδισε ο γηπεδούχος ή 2 αν κέρδισε ο φιλοξενούμενος:")
                if(g_winner_id==''):
                    g_winner_id=None
                    break
                elif(g_winner_id=="1"):
                    g_winner_id=int(g_winner_id)
                    g_winner_id = s_id_home
                    break
                elif(g_winner_id=="2"):
                    g_winner_id=int(g_winner_id)
                    g_winner_id = s_id_away
                    break
                else:
                    print("Λάθος εισαγωγή")


            conn.execute("INSERT INTO Game(id_match,tournament_name,home_id,away_id,court_number,gamedate,start_time,ending_time,final_score,winner_id) VALUES(?,?,?,?,?,?,?,?,?,?)",(None,g_tournament_name,s_id_home,s_id_away,g_court_number,g_gamedate.strftime("%Y-%m-%d"),g_start_time.strftime("%H:%M:%S"),g_ending_time.strftime("%H:%M:%S"),g_final_score,g_winner_id))
            conn.commit()
          
        except:
             print("\nΛάθος τιμές!\n")


def updateData():
    global conn,curr
    conn=sqlite3.connect("TennisClub.db")
    curr=conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")
    x=input("""1.Ενημερώστε στοιχεία Μέλους
2.Ενημερώστε στοιχεία Προπονητή
3.Ενημερώστε στοιχεία κράτησης
4.Ενημερώστε στοιχεία ενοικίασης εξοπλισμού
5.Ενημερώστε στοιχεία αγώνα
6.Ενημερώστε στοιχεία τουρνουά
Πατήστε Enter για να επιστρέψετε στο αρχικό μενού\n""")
    
    
    if(x=="1"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το Ονοματεπώνυμο μέλους που επιθυμείτε να ενημερώσετε:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+y+"';")
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει μέλος με αυτό το όνομα")
            else:
                id_memb=sel[0]
                break
        print("Εισάγετε τα νέα στοιχεία αλλιώς ξαναγράψτε τα παλιά")
        identity_number = input("\nΑριθμός ταυτότητας:")
        member_phone_number = int(input("\nΑριθμός τηλεφώνου:"))
        address = input("\nΔιεύθυνση κατοικίας:")
        try:
            conn.execute("UPDATE Member SET identity_number=?, phone_number=?, address=? WHERE id_member=?;",(identity_number,member_phone_number,address,id_memb))
            conn.commit()
        except:
            print("Λάθος τιμές")

    
    elif(x=="2"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το ονοματεπώνυμο προπονητή που θέλετε να ενημερώσετε:\n")
            curr.execute("SELECT id_coach FROM Coach WHERE first_name||' '||last_name='"+y+"';")
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει προπονητής με αυτό το όνομα")
            else:
                id_coach=sel[0]
                break
        print("Εισάγετε τα νέα στοιχεία αλλιώς ξαναγράψτε τα παλιά")
        coach_phone_number = int(input("\nΑριθμός τηλεφώνου:"))
        try:
            curr.execute("UPDATE Coach SET phone_number=? WHERE id_coach=?;",(coach_phone_number,id_coach))
            conn.commit()
        except:
            print("Λάθος τιμές")

    elif(x=="3"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το Ονοματεπώνυμο μέλους που πραγματοποιεί τη κράτηση:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+y+"';" )
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει μέλος με αυτό το όνομα")
            else:
                id_memb=sel[0]
                break
        res_date=input("Εισάγετε την ημερομηνία της κράτησης που θέλετε να ενημερώσετε:\n")
        res_date=datetime.strptime(res_date,"%Y-%m-%d")
        curr.execute("SELECT id_member, reservation_date FROM Reserves WHERE id_member=? AND reservation_date=?;",(id_memb,res_date.strftime("%Y-%m-%d")))
        sel2=curr.fetchone()
        if(sel==None):
            print("Δεν υπάρχει κράτηση με αυτό το όνομα και αυτή την ημερομηνία κράτησης")
        else:
            res_date=sel2[1]
            res_date=datetime.strptime(res_date,"%Y-%m-%d")

        print("Εισάγετε τα νέα στοιχεία αλλιώς ξαναγράψτε τα παλιά")
        y=input("Εισάγετε το ονοματεπώνυμο προπονητή που θέλετε να ενημερώσετε:\n")
        curr.execute("SELECT id_coach FROM Coach WHERE first_name||' '||last_name='"+y+"';")
        sel=curr.fetchone()
        if(sel==None):
            print("Δεν υπάρχει προπονητής με αυτό το όνομα")
        else:
            id_coach=sel[0]
        start_time=input("\nΏρα έναρξης(HH):")
        res_start_time = datetime.strptime(start_time,"%H")
        res_ending_time = res_start_time + timedelta(hours=1,minutes=30)
        res_number_of_members = int(input("\nΑριθμός μελών που θα αθληθούν:"))
        try:
            curr.execute("UPDATE Reserves SET id_coach=?, start_time=?, ending_time=?, number_of_members=? WHERE id_member = ? AND reservation_date =?;",(id_coach,res_start_time.strftime("%H:%M:%S"),res_ending_time.strftime("%H:%M:%S"),res_number_of_members,id_memb,res_date.strftime("%Y-%m-%d")))
            conn.commit()
        except:
            print("Λάθος εισαγωγή στοιχείων")

    elif(x=="4"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το Ονοματεπώνυμο μέλους που πραγματοποιεί την ενοικίαση:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+y+"';" )
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει μέλος με αυτό το όνομα")
            else:
                id_memb=sel[0]
                break
        res_date=input("Εισάγετε την ημερομηνία της ενοικίασης που θέλετε να ενημερώσετε:\n")
        res_date=datetime.strptime(res_date,"%Y-%m-%d")
        curr.execute("SELECT id_member, reservation_date FROM Rents WHERE id_member=? AND reservation_date=?;",(id_memb,res_date.strftime("%Y-%m-%d")))
        sel2=curr.fetchone()
        if(sel==None):
            print("Δεν υπάρχει ενοικίαση με αυτό το όνομα και αυτή την ημερομηνία κράτησης")
        else:
            res_date=sel2[1]
            res_date=datetime.strptime(res_date,"%Y-%m-%d")
        print("Εισάγετε τα νέα στοιχεία αλλιώς ξαναγράψτε τα παλιά")
        start_time=input("\nΏρα έναρξης(HH):")
        res_start_time = datetime.strptime(start_time,"%H")
        res_ending_time = res_start_time + timedelta(hours=1,minutes=30)
        try:
            curr.execute("UPDATE Rents SET start_time=?, ending_time=? WHERE id_member = ? AND reservation_date =?;",(res_start_time.strftime("%H:%M:%S"),res_ending_time.strftime("%H:%M:%S"),id_memb,res_date.strftime("%Y-%m-%d")))
            conn.commit()
        except:
            print("Λάθος εισαγωγή στοιχείων")

    elif(x=="5"):
        os.system('cls')
        while True:
            y=int(input("Εισάγετε το κωδικό αγώνα που θέλετε να ενημερώσετε:\n"))
            curr.execute("SELECT id_match,home_id,away_id from Game where id_match = ?;",(y,))
            sel=curr.fetchone()
            if(sel==None):
                print("Ο κωδικός δεν υπάρχει")
            else:
                id_match=sel[0]
                break
        print("Εισάγετε τα νέα στοιχεία αλλιώς ξαναγράψτε τα παλιά")
        g_gamedate = input("\nΗμερομηνία:")
        g_gamedate=datetime.strptime(g_gamedate,"%Y-%m-%d")
        g_start_time = input("\nΏρα έναρξης:")
        g_start_time=datetime.strptime(g_start_time,"%H")
        g_ending_time = input("\nΏρα λήξης:")
        if(g_ending_time==''):
            g_ending_time=None
        else:
            g_ending_time=datetime.strptime(g_ending_time,"%H:%M")

        g_final_score = input("\nΤελικό σκορ:")
        if(g_final_score==''):
            g_final_score=None
        while True:
            g_winner_id = input("\nΕισάγετε 1 αν κέρδισε ο γηπεδούχος ή 2 αν κέρδισε ο φιλοξενούμενος:")
            if(g_winner_id==''):
                g_winner_id=None
                break
            elif(g_winner_id=="1"):
                g_winner_id=int(g_winner_id)
                g_winner_id =sel[1]
                break
            elif(g_winner_id=="2"):
                g_winner_id=int(g_winner_id)
                g_winner_id =sel[2]
                break
            else:
                print("Λάθος εισαγωγή")

        try:
            conn.execute("UPDATE Game SET gamedate=?,start_time=?,ending_time=?,final_score=?,winner_id=? WHERE id_match=?;",(g_gamedate.strftime("%Y-%m-%d"),g_start_time.strftime("%H:%M:%S"),g_ending_time.strftime("%H:%M:%S"),g_final_score,g_winner_id,id_match))
            conn.commit()
        except:
            print("\nΛάθος τιμές!\n")

    elif (x=="6"):
        try:
            os.system('cls')
            while True:
                y=input("Εισάγετε το όνομα του τουρνουά που επιθυμείτε να ενημερώσετε:\n")
                curr.execute("SELECT tournament_name from Tournament where tournament_name = ?;",(y,))
                sel=curr.fetchone()
                if(sel==None):
                    print("Το τουρνουά δεν υπάρχει")
                else:
                    break
            print("Εισάγετε τα νέα στοιχεία αλλιώς ξαναγράψτε τα παλιά")
            t_start_date = input("\nΗμερομηνία έναρξης:")
            t_start_date=datetime.strptime(t_start_date,"%Y-%m-%d")
            t_ending_date = input("\nΗμερομηνία λήξης:")
            t_ending_date =datetime.strptime(t_ending_date,"%Y-%m-%d")
            t_participants = int(input("\nΑριθμός συμμετοχών:"))
            t_prize = input("\nΈπαθλο:")

            while True:
                male_winner=input("\nΕισάγεται το νικητή αντρών:")
                female_winner=input("\nΕισάγεται το νικητή γυναικών:")
                if(male_winner=='' and female_winner==''):
                    male_id=None
                    female_id=None
                    break
                else:
                    if(t_category=="Μονό"):
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Member on id_member=id_player where tournament_name=? AND first_name||' '||last_name=?;",(y,male_winner))
                        sel1=fetchone()
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Member on id_member=id_player where tournament_name=? AND first_name||' '||last_name=?;",(y,female_winner))
                        sel2=fetchone()
                        if(sel1==None):
                            print("\nΟ παίκτης δεν είναι εγγεγραμένος στο τουρνουά")
                        else:
                            male_id=sel1[0]
                            female_id=sel2[0]
                            break
                    elif(t_category=="Διπλό"):
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Team on id_team=id_player where tournament_name=? AND team_name=?;",(y,male_winner))
                        sel1=fetchone()
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Team on id_team=id_player where tournament_name=? AND team_name=?;",(y,female_winner))
                        sel2=fetchone()
                        if(sel1==None):
                            print("\nΗ ομάδα δεν είναι εγγεγραμένη στο τουρνουά")
                        else:
                            male_id=sel1[0]
                            female_id=sel2[0]
                            break
                    
                
            conn.execute("UPDATE Tournament SET start_date=?,ending_date=?,participants=?,prize=?,winner_female=?,winner_male=? where tournament_name=? ;",(t_start_date.strftime("%Y-%m-%d"),t_ending_date.strftime("%Y-%m-%d"),t_participants,t_prize,female_id,male_id,y))
            conn.commit()
            
        except:
            print("\nΛάθος τιμές!\n")
             
        

def deleteData():
    global conn,curr
    conn=sqlite3.connect("TennisClub.db")
    curr=conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")
    x=input("""1.Διαγράψτε Μέλος
2.Διαγράψτε προπονητή
3.Διαγράψτε ομάδα
4.Διαγράψτε κράτηση
5.Διαγράψτε ενοικίαση εξοπλισμού
6.Διαγράψτε αγώνα
7.Διαγράψτε τουρνουά
8.Διαγράψτε συμμετοχή παίκτη σε τουρνουά
Πατήστε Enter για να επιστρέψετε στο αρχικό μενού\n""")
    
    if(x=="1"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το Ονοματεπώνυμο μέλους που επιθυμείτε να διαγραφεί:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+y+"';")
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει μέλος με αυτό το όνομα")
            else:
                id_memb=sel[0]
                break
        curr.execute("DELETE FROM Player WHERE id_player=?;",(id_memb,))
        conn.commit()
    
            
    elif(x=="2"):
        os.system('cls')
        y=input("Εισάγετε το ονοματεπώνυμο προπονητή που θέλετε να διαγραφεί:\n")
        try:
            curr.execute("Delete from Coach WHERE first_name||' '||last_name='"+y+"';")
            conn.commit()
        except:
            print("Ο προπονητής δεν υπάρχει")

            
            
    elif(x=="3"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το Όνομα Ομάδας που επιθυμείτε να διαγραφεί:\n")
            curr.execute("SELECT id_team FROM Team WHERE team_name=?;" ,(y,))
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει ομάδα με αυτό το όνομα")
            else:
                id_team=sel[0]
                break
        conn.execute("DELETE FROM Player WHERE id_player=?;",(id_team,))
        conn.commit()
            
            
    elif(x=="4"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το Ονοματεπώνυμο μέλους που πραγματοποιεί τη κράτηση:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+y+"';" )
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει μέλος με αυτό το όνομα")
            else:
                id_memb=sel[0]
                break
        c=input("Εισάγετε την ημερομηνία της κράτησης που θέλετε να διαγραφεί:\n")
        try:
            curr.execute("Delete from Reserves where id_member = ? AND reservation_date =?;",(id_memb,c,))
            conn.commit()
        except:
            print("Λάθος εισαγωγή στοιχείων")
            
            
    elif(x=="5"):
        os.system('cls')
        while True:
            y=input("Εισάγετε το Ονοματεπώνυμο μέλους που πραγματοποιεί την ενοικίαση:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+y+"';" )
            sel=curr.fetchone()
            if(sel==None):
                print("Δεν υπάρχει μέλος με αυτό το όνομα")
            else:
                id_memb=sel[0]
                break
        c=(input("Εισάγετε την ημερομηνία της ενοικίασης που θέλετε να διαγραφεί:\n"))
        try:
            curr.execute("Delete from Rents where id_member = ? AND reservation_date =?;",(id_memb,c,))
            conn.commit()
        except:
            print("Λάθος εισαγωγή στοιχείων")
            
    elif(x=="6"):
        os.system('cls')
        y=int(input("Εισάγετε το κωδικό αγώνα που θέλετε να διαγραφεί:\n"))
        try:
            curr.execute("Delete from Game where id_match = ?;",(y,))
            conn.commit()
        except:
            print("Ο κωδικός δεν υπάρχει")
            
    elif(x=="7"):
        os.system('cls')
        y=(input("Εισάγετε το όνομα τουρνουά που θέλετε να διαγραφεί:\n"))
        try:
            curr.execute("Delete from Tournament where tournament_name = ?;",(y,))
            conn.commit()
        except:
            print("Το τουρνουά δεν υπάρχει")
            
    elif(x=="8"):
        os.system('cls')
        while True:
            ch=input("Αν προκείται για μέλος επιλέξτε 1\nΑν πρόκειται για ομάδα επιλέξτε 2\n")
            if(ch=="1"):
                y=input("Εισάγετε το Ονοματεπώνυμο μέλους που πραγματοποιεί την εγγραφή:\n")
                curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+y+"';" )
                sel=curr.fetchone()
                if(sel==None):
                    print("Δεν υπάρχει μέλος με αυτό το όνομα")
                else:
                    id_memb=sel[0]
                    break
            elif(ch=="2"):
                y=input("Εισάγετε το Όνομα Ομάδας που πραγματοποιεί την εγγραφή:\n")
                curr.execute("SELECT id_team FROM Team WHERE team_name='"+y+"';" )
                sel=curr.fetchone()
                if(sel==None):
                    print("Δεν υπάρχει ομάδα με αυτό το όνομα")
                else:
                    id_memb=sel[0]
                    break

            
        z=(input("Εισάγετε το όνομα τουρνουά στο οποίο έχει δηλώσει συμμετοχή:\n"))
        try:
            curr.execute("Delete from SignsUp where id_player = ? AND tournament_name = ?;",(id_memb,z,))
            conn.commit()
        except:
            print("Το τουρνουά δεν υπάρχει")
    
            


def menu():
    global conn
    conn=sqlite3.connect("TennisClub.db")
    input("Πάτηστε Enter για να συνεχίσετε")
    while True:
        os.system('cls')
        x=input("""\nΕπιλέξτε 1 για να εισάγετε νέα δεδομένα
Επιλέξτε 2 για να ενημερώσετε δεδομένα
Επιλέξτε 3 για να διαγράψετε δεδομένα
Επιλέξτε 4 για έξοδο\n\n""")

        if(x=="1"):
            os.system('cls')
            insertData()
        elif(x=="2"):
            os.system('cls')
            updateData()
        elif(x=="3"):
            os.system('cls')
            deleteData()
        elif(x=="4"):
            os.system('cls')
            print("Καλή συνέχεια!")
            time.sleep(2)
            conn.close()
            break
        else:
            print("Λάθος είσοδος! Προσπαθήστε ξανά\n")


try:
    createDatabase()
except:
    print("Η βάση έχει δημιουργηθεί")
try:
    loadDataInDatabase()
except:
    print("Τα δεδομένα έχουν φορτωθεί στη βάση\n")   
menu()
