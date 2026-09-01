import sqlite3,os,time
from datetime import datetime,timedelta


def createDatabase():
    import TennisClub_Sql
    print("Tennis Club Database created successfully!\n")


def loadDataInDatabase():
    import TennisClub_Data
    print("Data loaded successfully\n")


def insertData():
    global conn,cursor
    conn=sqlite3.connect("TennisClub.db")
    os.system('cls')  
    cursor=conn.cursor()
    ch=input("""\n1. Add new member
2. Add new coach
3. Add reservation
4. Add equipment rental
5. Add player to team
6. Register player for tournament
7. Add new tournament
8. Add new match
Press Enter to return to the main menu\n\n""")
    
    if (ch=="1"):
        try:
            os.system('cls')

            print("\nEnter member details\n\n")
            member_first_name = input("First name: ")
            member_last_name = input("\nLast name: ")
            birthdate = input("\nDate of birth (YYYY-MM-DD): ")
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
            identity_number = input("\nID number: ")
            member_phone_number = int(input("\nPhone number: "))
            address = input("\nHome address: ")
            gender = input("\nGender ('F' for female, 'M' for male): ")
            while True:
                if gender != "F" and gender != "M":
                    gender = input("\nInvalid input. Please enter again.\nGender ('F' for female, 'M' for male): ")
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

            print("\nData inserted successfully!")
            time.sleep(2)
              
        except:
            print("\nInvalid values!\n")
            time.sleep(1)

    elif (ch=="2"):
        try:
            os.system('cls')
            print("\nEnter coach details.\n\n")
            coach_first_name = input("First name: ")
            coach_last_name = input("\nLast name: ")
            coach_phone_number = int(input("\nPhone number: "))
            birthdate = input("\nDate of birth (YYYY-MM-DD): ")
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
            
            conn.execute("INSERT INTO Coach (id_coach,first_name,last_name,phone_number,birthdate) VALUES(?,?,?,?,?)",(None,coach_first_name,coach_last_name,coach_phone_number,birthdate.strftime("%Y-%m-%d")))
            conn.commit()

            print("\nData inserted successfully!")
            time.sleep(2)
        except:
            print("\nInvalid values!\n")
            time.sleep(1)

    elif (ch=="3"):
        try:
            os.system('cls')
            print("\nEnter reservation details.\n\n")
            while True:
                member_name = input("Enter member full name: ")
                cursor.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='"+member_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nMember not found.")
                else:
                    res_id_member = sel[0]
                    break
          
            while True:
                coach_name = input("\nEnter coach full name: ")
                cursor.execute("SELECT id_coach FROM Coach WHERE first_name||' '||last_name='" + coach_name + "';")
                sel = cursor.fetchone()
                if sel is None:
                    print("\nCoach not found.")
                else:
                    res_id_coach = sel[0]
                    break

            while True:
                res_court_number = input("\nSelect a court:\n  1. Clay Court\n  2. Clay Court\n  3. Clay Court\n  4. Grass Court\n  5. Grass Court\n  6. Hard Court\n\nCourt number: ")
                cursor.execute("SELECT court_number FROM Court WHERE court_number=" + res_court_number + ";")
                sel = cursor.fetchone()
                if sel is None:
                    print("\nCourt not found.")
                else:
                    res_court_number = sel[0]
                    break
                
            res_date = input("\nReservation date (YYYY-MM-DD): ")
            res_date = datetime.strptime(res_date, "%Y-%m-%d")
            start_time = input("\nStart time (HH): ")
            res_start_time = datetime.strptime(start_time, "%H")
            res_ending_time = res_start_time + timedelta(hours=1, minutes=30)
            res_number_of_members = int(input("\nNumber of members training: "))
            
            conn.execute("INSERT into Reserves (id_member,id_coach,court_number,reservation_date,start_time,ending_time,number_of_members) VALUES(?,?,?,?,?,?,?)",(res_id_member,res_id_coach,res_court_number,res_date.strftime("%Y-%m-%d"),res_start_time.strftime("%H:%M:%S"),res_ending_time.strftime("%H:%M:%S"),res_number_of_members))
            conn.commit()
            print("\nData inserted successfully!")
            time.sleep(2)
        except:
            print("\nInvalid values!\n")
            time.sleep(1)

    elif (ch=="4"):
        try:
            os.system('cls')
            print("\nEnter rental details.")
            while True:
                member_name = input("\nEnter member full name: ")
                cursor.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + member_name + "';")
                sel = cursor.fetchone()
                if sel is None:
                    print("\nMember not found.")
                else:
                    r_id_member = sel[0]
                    break
                
            while True:
                r_id_racket = input("\nRacket ID (1-20): ")
                cursor.execute("SELECT id_eq FROM Equipment WHERE id_eq=" + r_id_racket + ";")
                sel = cursor.fetchone()
                if sel is None:
                    print("\nEquipment ID not found.")
                else:
                    r_id_racket = sel[0]
                    break
                
            while True:
                r_id_balls = input("\nBall set ID (x3)(21-34): ")
                cursor.execute("SELECT id_eq FROM Equipment WHERE id_eq=" + r_id_balls + ";")
                sel = cursor.fetchone()
                if sel is None:
                    print("\nEquipment ID not found.")
                else:
                    r_id_balls = sel[0]
                    break
    
            res_date = input("\nReservation date (YYYY-MM-DD): ")
            res_date = datetime.strptime(res_date, "%Y-%m-%d")
            start_time = input("\nStart time (HH): ")
            res_start_time = datetime.strptime(start_time,"%H")
            res_ending_time = res_start_time + timedelta(hours=1,minutes=30)
            conn.execute("INSERT into Rents (id_member,id_racket,id_balls,reservation_date,start_time,ending_time) VALUES(?,?,?,?,?,?)",(r_id_member,r_id_racket,r_id_balls,res_date.strftime("%Y-%m-%d"),res_start_time.strftime("%H:%M:%S"),res_ending_time.strftime("%H:%M:%S")))
            conn.commit()
            print("\nData inserted successfully!")
            time.sleep(2)
            
          
        except:
            print("\nInvalid values!\n")
            time.sleep(1)


    elif (ch=="5"):
        try:
            while True:
                member_name = input("\nEnter member full name: ")
                cursor.execute("SELECT id_member FROM Member  WHERE first_name||' '||last_name='"+member_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nMember not found.")
                else:
                    t_id_member = sel[0]
                    break

            t_team_name = input("\nEnter team name: ")
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
                print("\nData inserted successfully!")
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
            print("\nRegister player for tournament.")
            while True:
                s_tournament_name = input("\nEnter tournament name: "))
                cursor.execute("SELECT tournament_name FROM Tournament WHERE tournament_name='"+s_tournament_name+"';")
                sel = cursor.fetchone()
                if(sel==None):
                    print("\nTournament not found.")
                else:
                    s_tournament_name = sel[0]
                    break

            cursor.execute("SELECT category FROM Tournament WHERE tournament_name='"+s_tournament_name+"';")
            sel2 = cursor.fetchone()
            s_category = sel2[0]
            if(s_category=="Διπλό"):
                while True:
                    team_name = input("\nThis is a doubles tournament.\nEnter team name: ")
                    cursor.execute("SELECT id_player FROM Player join Team on id_player=id_team WHERE team_name='"+team_name+"';")
                    sel3 = cursor.fetchone()
                    if(sel3==None):
                        print("\nTeam not found.")
                    else:
                        s_id_player = sel3[0]
                        break

                cursor.execute("SELECT id_player FROM SignsUp WHERE id_player="+str(s_id_player)+" AND tournament_name='"+s_tournament_name+"';")
                sel4 = cursor.fetchone()
                if(sel4==None):
                    conn.execute("INSERT into SignsUp (id_player,tournament_name) VALUES(?,?)",(s_id_player,s_tournament_name))
                    conn.commit()
                else:
                    print("\nTeam is already registered for this tournament!")
                    
                
            elif(s_category=="Singles"):
                member_name = input("\nThis is a singles tournament.\nEnter member full name: ")
                cursor.execute("SELECT id_player FROM Player JOIN Member ON id_player=id_member WHERE first_name||' '||last_name='" + member_name + "';")
                sel3 = cursor.fetchone()
                if sel3 is None:
                    print("\nMember not found.")
                else:
                    s_id_player = sel3[0]

                cursor.execute("SELECT id_player FROM SignsUp WHERE id_player="+str(s_id_player)+" AND tournament_name='"+s_tournament_name+"';")
                sel4 = cursor.fetchone()
                if(sel4==None):
                    conn.execute("INSERT into SignsUp (id_player,tournament_name) VALUES(?,?)",(s_id_player,s_tournament_name))
                    conn.commit()
    
                else:
                    print("\nPlayer is already registered for this tournament!")
          
        except:
            print("\nInvalid values!\n")


          

    elif (ch=="7"):
        try:
            os.system('cls')
            print("\nEnter tournament details.")
            t_tournament_name = input("\nTournament name: ")
            t_category = input("\nTournament type (Singles/Doubles): ")
            t_start_date = input("\nStart date (YYYY-MM-DD): ")
            t_start_date = datetime.strptime(t_start_date, "%Y-%m-%d")
            t_ending_date = input("\nEnd date (YYYY-MM-DD): ")
            t_ending_date = datetime.strptime(t_ending_date, "%Y-%m-%d")
            t_participants = int(input("\nNumber of participants: "))
            t_prize = input("\nPrize: ")
            while True:
                male_winner = input("\nEnter male winner: ")
                female_winner = input("\nEnter female winner: ")
                if male_winner == '' and female_winner == '':
                    male_winner = None
                    female_winner = None
                else:
                    if t_category == "Singles":
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Member ON id_member=id_player WHERE tournament_name=? AND first_name||' '||last_name=?;", (t_tournament_name, male_winner))
                        sel1 = cursor.fetchone()
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Member ON id_member=id_player WHERE tournament_name=? AND first_name||' '||last_name=?;", (t_tournament_name, female_winner))
                        sel2 = cursor.fetchone()
                        if sel1 is None:
                            print("\nPlayer not registered for this tournament.")
                        else:
                            male_id = sel1[0]
                            female_id = sel2[0]
                            break
                    elif t_category == "Doubles":
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Team on id_team=id_player where tournament_name=? AND team_name=?;",(t_tournament_name,male_winner))
                        sel1=fetchone()
                        cursor.execute("SELECT id_member FROM SignsUp NATURAL JOIN Player JOIN Team on id_team=id_player where tournament_name=? AND team_name=?;",(t_tournament_name,female_winner))
                        sel2=fetchone()
                        if(sel1==None):
                            print("\nTeam not registered for this tournament.")
                        else:
                            male_id=sel1[0]
                            female_id=sel2[0]
                            break
                    
                
            conn.execute("INSERT into Tournament (tournament_name,category,start_date,ending_date,participants,prize,winner_female,winner_male) VALUES(?,?,?,?,?,?,?,?)",(t_tournament_name,t_category,t_start_date.strftime("%Y-%m-%d"),t_ending_date.strftime("%Y-%m-%d"),t_participants,t_prize,female_id,male_id))
            conn.commit()

        except:
            print("\nInvalid values!\n")

    elif (ch=="8"):
        try:
            os.system('cls')
            print("\nEnter match details.\n\n")
            while True:
                g_tournament_name = input("\nTournament name: ")
                cursor.execute("SELECT tournament_name FROM Tournament WHERE tournament_name='" + g_tournament_name + "';")
                sel = cursor.fetchone()
                if sel is None:
                    print("\nTournament not found.")
                else:
                    g_tournament_name = sel[0]
                    break
                
            cursor.execute("SELECT category FROM Tournament WHERE tournament_name='"+g_tournament_name+"';")
            sel2 = cursor.fetchone()
            s_category = sel2[0]
            if(s_category=="Διπλό"):
                while True:
                    home_name = input("\nThis is a doubles tournament.\nEnter home team name: ")
                    cursor.execute("SELECT id_player FROM SignsUp natural join Player join Team on id_player=id_team WHERE team_name='"+home_name+"';")
                    sel3 = cursor.fetchone()
                    if(sel3==None):
                         print("\nTeam not found.")
                    else:
                        s_id_home = sel3[0]
                        break
                while True:
                    away_name = input("Enter away team name: ")
                    cursor.execute("SELECT id_player FROM SignsUp natural join Player join Team on id_player=id_team WHERE team_name='"+away_name+"';")
                    sel4 = cursor.fetchone()
                    if(sel4==None):
                        print("\nTeam not found.")
                    else:
                        s_id_away = sel4[0]
                        break
                    
            elif s_category == "Singles":
                while True:
                    home_name = input("\nThis is a singles tournament.\nEnter home player full name: ")
                    cursor.execute("SELECT id_player FROM SignsUp NATURAL JOIN Player JOIN Member ON id_player=id_member WHERE first_name||' '||last_name='" + home_name + "';")
                    sel3 = cursor.fetchone()
                    if sel3 is None:
                        print("\nMember not found.")
                    else:
                        s_id_home = sel3[0]
                        break
                while True:
                    away_name = input("Enter away player full name: ")
                    cursor.execute("SELECT id_player FROM SignsUp NATURAL JOIN Player JOIN Member ON id_player=id_member WHERE first_name||' '||last_name='" + away_name + "';")
                    sel4 = cursor.fetchone()
                    if sel4 is None:
                        print("\nMember not found.")
                    else:
                        s_id_away = sel4[0]
                        break
            
             while True:
                g_court_number = input("\nCourt number: ")
                cursor.execute("SELECT court_number FROM Court WHERE court_number=" + g_court_number + ";")
                sel = cursor.fetchone()
                if sel is None:
                    print("\nCourt not found.")
                else:
                    g_court_number = sel[0]
                    break
            
            g_gamedate = input("\nMatch date (YYYY-MM-DD): ")
            g_gamedate = datetime.strptime(g_gamedate, "%Y-%m-%d")
            g_start_time = input("\nStart time (HH): ")
            g_start_time = datetime.strptime(g_start_time, "%H")
            g_ending_time = input("\nEnd time: ")
            if(g_ending_time==''):
                g_ending_time=None
            else:
                g_ending_time=datetime.strptime(g_start_time,"%H:%M")
                g_ending_time= g_ending_time.strftime("%H:%M:%S")
            g_final_score = input("\nFinal score: ")
            if(g_final_score==''):
                g_final_score=None
            while True:
                g_winner_id = input("\nEnter 1 if home player/team won, 2 if away player/team won: ")
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
                    print("Invalid input.")


            conn.execute("INSERT INTO Game(id_match,tournament_name,home_id,away_id,court_number,gamedate,start_time,ending_time,final_score,winner_id) VALUES(?,?,?,?,?,?,?,?,?,?)",(None,g_tournament_name,s_id_home,s_id_away,g_court_number,g_gamedate.strftime("%Y-%m-%d"),g_start_time.strftime("%H:%M:%S"),g_ending_time.strftime("%H:%M:%S"),g_final_score,g_winner_id))
            conn.commit()
          
        except:
             print("\nInvalid values!\n")


def updateData():
    global conn, curr
    conn = sqlite3.connect("TennisClub.db")
    curr = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")
    x = input("""1. Update member details
2. Update coach details
3. Update reservation details
4. Update equipment rental details
5. Update match details
6. Update tournament details
Press Enter to return to the main menu\n""")
    
    
    if(x=="1"):
        os.system('cls')
        while True:
            y = input("Enter the full name of the member to update:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + y + "';")
            sel = curr.fetchone()
            if sel is None:
                print("Member not found.")
            else:
                id_memb=sel[0]
                break
        print("Enter new details (or re-enter existing ones to keep them)")
        identity_number = input("\nID number: ")
        member_phone_number = int(input("\nPhone number: "))
        address = input("\nHome address: ")
        try:
            conn.execute("UPDATE Member SET identity_number=?, phone_number=?, address=? WHERE id_member=?;",
                         (identity_number, member_phone_number, address, id_memb))
            conn.commit()
        except:
            print("Invalid values.")

    
    elif(x=="2"):
        os.system('cls')
        while True:
            y = input("Enter the full name of the coach to update:\n")
            curr.execute("SELECT id_coach FROM Coach WHERE first_name||' '||last_name='" + y + "';")
            sel = curr.fetchone()
            if sel is None:
                print("Coach not found.")
            else:
                id_coach = sel[0]
                break
        print("Enter new details (or re-enter existing ones to keep them)")
        coach_phone_number = int(input("\nPhone number: "))
        try:
            curr.execute("UPDATE Coach SET phone_number=? WHERE id_coach=?;", (coach_phone_number, id_coach))
            conn.commit()
        except:
            print("Invalid values.")

    elif(x=="3"):
        os.system('cls')
        while True:
            y = input("Enter the full name of the member who made the reservation:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + y + "';")
            sel = curr.fetchone()
            if sel is None:
                print("Member not found.")
            else:
                id_memb = sel[0]
                break
        res_date = input("Enter the reservation date to update (YYYY-MM-DD):\n")
        res_date = datetime.strptime(res_date, "%Y-%m-%d")
        curr.execute("SELECT id_member, reservation_date FROM Reserves WHERE id_member=? AND reservation_date=?;",
                     (id_memb, res_date.strftime("%Y-%m-%d")))
        sel2=curr.fetchone()
        if(sel==None):
            print("No reservation found for this member and date.")
        else:
            res_date=sel2[1]
            res_date=datetime.strptime(res_date,"%Y-%m-%d")

        print("Enter new details (or re-enter existing ones to keep them)")
        y = input("Enter coach full name: \n")
        curr.execute("SELECT id_coach FROM Coach WHERE first_name||' '||last_name='" + y + "';")
        sel = curr.fetchone()
        if sel is None:
            print("Coach not found.")
        else:
            id_coach = sel[0]
        start_time = input("\nStart time (HH): ")
        res_start_time = datetime.strptime(start_time, "%H")
        res_ending_time = res_start_time + timedelta(hours=1, minutes=30)
        res_number_of_members = int(input("\nNumber of members training: "))
        try:
            curr.execute("UPDATE Reserves SET id_coach=?, start_time=?, ending_time=?, number_of_members=? WHERE id_member=? AND reservation_date=?;",
                         (id_coach, res_start_time.strftime("%H:%M:%S"), res_ending_time.strftime("%H:%M:%S"), res_number_of_members, id_memb, res_date.strftime("%Y-%m-%d")))
            conn.commit()
        except:
            print("Invalid input.")

    elif x == "4":
        os.system('cls')
        while True:
            y = input("Enter the full name of the member who made the rental:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + y + "';")
            sel = curr.fetchone()
            if sel is None:
                print("Member not found.")
            else:
                id_memb = sel[0]
                break
        res_date = input("Enter the rental date to update (YYYY-MM-DD):\n")
        res_date = datetime.strptime(res_date, "%Y-%m-%d")
        curr.execute("SELECT id_member, reservation_date FROM Rents WHERE id_member=? AND reservation_date=?;",
                     (id_memb, res_date.strftime("%Y-%m-%d")))
        sel2 = curr.fetchone()
        if sel2 is None:
            print("No rental found for this member and date.")
        else:
            res_date = datetime.strptime(sel2[1], "%Y-%m-%d")
        print("Enter new details (or re-enter existing ones to keep them)")
        start_time = input("\nStart time (HH): ")
        res_start_time = datetime.strptime(start_time, "%H")
        res_ending_time = res_start_time + timedelta(hours=1, minutes=30)
        try:
            curr.execute("UPDATE Rents SET start_time=?, ending_time=? WHERE id_member=? AND reservation_date=?;",
                         (res_start_time.strftime("%H:%M:%S"), res_ending_time.strftime("%H:%M:%S"), id_memb, res_date.strftime("%Y-%m-%d")))
            conn.commit()
        except:
            print("Invalid input.")

    elif x == "5":
        os.system('cls')
        while True:
            y = int(input("Enter the match ID to update:\n"))
            curr.execute("SELECT id_match, home_id, away_id FROM Game WHERE id_match=?;", (y,))
            sel = curr.fetchone()
            if sel is None:
                print("Match ID not found.")
            else:
                id_match = sel[0]
                break
        print("Enter new details (or re-enter existing ones to keep them)")
        g_gamedate = input("\nMatch date (YYYY-MM-DD): ")
        g_gamedate = datetime.strptime(g_gamedate, "%Y-%m-%d")
        g_start_time = input("\nStart time (HH): ")
        g_start_time = datetime.strptime(g_start_time, "%H")
        g_ending_time = input("\nEnd time: ")
        if g_ending_time == '':
            g_ending_time = None
        else:
            g_ending_time = datetime.strptime(g_ending_time, "%H:%M")
        g_final_score = input("\nFinal score: ")
        if g_final_score == '':
            g_final_score = None
        while True:
            g_winner_id = input("\nEnter 1 if home player/team won, 2 if away: ")
            if g_winner_id == '':
                g_winner_id = None
                break
            elif g_winner_id == "1":
                g_winner_id = sel[1]
                break
            elif g_winner_id == "2":
                g_winner_id = sel[2]
                break
            else:
                print("Invalid input.")
        try:
            conn.execute("UPDATE Game SET gamedate=?, start_time=?, ending_time=?, final_score=?, winner_id=? WHERE id_match=?;",
                         (g_gamedate.strftime("%Y-%m-%d"), g_start_time.strftime("%H:%M:%S"), g_ending_time.strftime("%H:%M:%S") if g_ending_time else None, g_final_score, g_winner_id, id_match))
            conn.commit()
        except:
            print("\nInvalid values!\n")

    elif x == "6":
        try:
            os.system('cls')
            while True:
                y = input("Enter the tournament name to update:\n")
                curr.execute("SELECT tournament_name FROM Tournament WHERE tournament_name=?;", (y,))
                sel = curr.fetchone()
                if sel is None:
                    print("Tournament not found.")
                else:
                    break
            print("Enter new details (or re-enter existing ones to keep them)")
            t_start_date = input("\nStart date (YYYY-MM-DD): ")
            t_start_date = datetime.strptime(t_start_date, "%Y-%m-%d")
            t_ending_date = input("\nEnd date (YYYY-MM-DD): ")
            t_ending_date = datetime.strptime(t_ending_date, "%Y-%m-%d")
            t_participants = int(input("\nNumber of participants: "))
            t_prize = input("\nPrize: ")
            conn.execute("UPDATE Tournament SET start_date=?, ending_date=?, participants=?, prize=? WHERE tournament_name=?;",
                         (t_start_date.strftime("%Y-%m-%d"), t_ending_date.strftime("%Y-%m-%d"), t_participants, t_prize, y))
            conn.commit()
        except:
            print("\nInvalid values!\n")


def deleteData():
    global conn, curr
    conn = sqlite3.connect("TennisClub.db")
    curr = conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")
    x = input("""1. Delete member
2. Delete coach
3. Delete team
4. Delete reservation
5. Delete equipment rental
6. Delete match
7. Delete tournament
8. Delete player tournament registration
Press Enter to return to the main menu\n""")

    if x == "1":
        os.system('cls')
        while True:
            y = input("Enter the full name of the member to delete:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + y + "';")
            sel = curr.fetchone()
            if sel is None:
                print("Member not found.")
            else:
                id_memb = sel[0]
                break
        curr.execute("DELETE FROM Player WHERE id_player=?;", (id_memb,))
        conn.commit()

    elif x == "2":
        os.system('cls')
        y = input("Enter the full name of the coach to delete:\n")
        try:
            curr.execute("DELETE FROM Coach WHERE first_name||' '||last_name='" + y + "';")
            conn.commit()
        except:
            print("Coach not found.")

    elif x == "3":
        os.system('cls')
        while True:
            y = input("Enter the team name to delete:\n")
            curr.execute("SELECT id_team FROM Team WHERE team_name=?;", (y,))
            sel = curr.fetchone()
            if sel is None:
                print("Team not found.")
            else:
                id_team = sel[0]
                break
        conn.execute("DELETE FROM Player WHERE id_player=?;", (id_team,))
        conn.commit()

    elif x == "4":
        os.system('cls')
        while True:
            y = input("Enter the full name of the member who made the reservation:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + y + "';")
            sel = curr.fetchone()
            if sel is None:
                print("Member not found.")
            else:
                id_memb = sel[0]
                break
        c = input("Enter the reservation date to delete (YYYY-MM-DD):\n")
        try:
            curr.execute("DELETE FROM Reserves WHERE id_member=? AND reservation_date=?;", (id_memb, c))
            conn.commit()
        except:
            print("Invalid input.")

    elif x == "5":
        os.system('cls')
        while True:
            y = input("Enter the full name of the member who made the rental:\n")
            curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + y + "';")
            sel = curr.fetchone()
            if sel is None:
                print("Member not found.")
            else:
                id_memb = sel[0]
                break
        c = input("Enter the rental date to delete (YYYY-MM-DD):\n")
        try:
            curr.execute("DELETE FROM Rents WHERE id_member=? AND reservation_date=?;", (id_memb, c))
            conn.commit()
        except:
            print("Invalid input.")

    elif x == "6":
        os.system('cls')
        y = int(input("Enter the match ID to delete:\n"))
        try:
            curr.execute("DELETE FROM Game WHERE id_match=?;", (y,))
            conn.commit()
        except:
            print("Match ID not found.")

    elif x == "7":
        os.system('cls')
        y = input("Enter the tournament name to delete:\n")
        try:
            curr.execute("DELETE FROM Tournament WHERE tournament_name=?;", (y,))
            conn.commit()
        except:
            print("Tournament not found.")

    elif x == "8":
        os.system('cls')
        while True:
            ch = input("Enter 1 for a member, 2 for a team:\n")
            if ch == "1":
                y = input("Enter the full name of the member:\n")
                curr.execute("SELECT id_member FROM Member WHERE first_name||' '||last_name='" + y + "';")
                sel = curr.fetchone()
                if sel is None:
                    print("Member not found.")
                else:
                    id_memb = sel[0]
                    break
            elif ch == "2":
                y = input("Enter the team name:\n")
                curr.execute("SELECT id_team FROM Team WHERE team_name='" + y + "';")
                sel = curr.fetchone()
                if sel is None:
                    print("Team not found.")
                else:
                    id_memb = sel[0]
                    break

        z = input("Enter the tournament name the player is registered for:\n")
        try:
            curr.execute("DELETE FROM SignsUp WHERE id_player=? AND tournament_name=?;", (id_memb, z))
            conn.commit()
        except:
            print("Tournament not found.")


def menu():
    global conn
    conn = sqlite3.connect("TennisClub.db")
    input("Press Enter to continue")
    while True:
        os.system('cls')
        x = input("""\nSelect 1 to insert new data
Select 2 to update data
Select 3 to delete data
Select 4 to exit\n\n""")

        if x == "1":
            os.system('cls')
            insertData()
        elif x == "2":
            os.system('cls')
            updateData()
        elif x == "3":
            os.system('cls')
            deleteData()
        elif x == "4":
            os.system('cls')
            print("Goodbye!")
            time.sleep(2)
            conn.close()
            break
        else:
            print("Invalid input! Please try again.\n")


try:
    createDatabase()
except:
    print("Database already exists.")
try:
    loadDataInDatabase()
except:
    print("Data already loaded.\n")
menu()
