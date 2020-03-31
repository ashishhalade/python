
"""Cricket data analysis"""
import getpass
import compute_1 as c
import excel_f as e
import display_f as d
import update_1 as u
USER = getpass.getuser()
while True:#condition written for enterring the user name if correct it will ask for password
    PWD = getpass.getpass("User Name : ")
    if PWD == 'ashish01':#username
        break
    else:
        print("The username you entered is incorrect.")
USER = getpass.getuser()
while True:#condition written for enterrung the password if correct further operation will be performed
    P = getpass.getpass('enter password? ')
    if P.lower() == 'icecream':#password
        print("Welcome")
        print()
        DF_DATA = e.read_excel()
        KE_Z = input("enter the specific team : ")#enter input for specific team to be displayed
        d.displayby_team(DF_DATA, KE_Z)
        KE_Y = int(input("enter score above which is to be displayed : "))#enter score
        c.scoreabove_fifty(DF_DATA, KE_Y)
        c.minin_runsscored(DF_DATA)
        KE_X = int(input("enter cost of player which you want : "))#enter cost of player
        d.trackby_playercost(DF_DATA, KE_X)
        c.averageof_playerscost(DF_DATA)
        c.max_cost(DF_DATA)
        DF_DATA = u.update_score(DF_DATA)
        #DF_DATA = u.add_col(DF_DATA)
        DF2_DATA = u.add_col(DF_DATA)
        A_NAME = input('enter player name : ')
        T_TEAM = input('team : ')
        IPL_FRAN = input('ipl franchise : ')
        PLAYER_COST = int(input('enter player cost : '))
        INNING_PLAYED = int(input('enter innings played : '))
        RUNS_SCORED = int(input('enter runs scored : '))
        STRIKE_RATE = float(input('enter strike rate : '))
        FOU_R = int(input('enter no of fours : '))
        SIX_S = int(input('enter no of sixes : '))
        F_M = int(input('enter no of runs in First match : '))
        DF1_DATA = u.add_row(DF2_DATA, A_NAME, T_TEAM, IPL_FRAN, PLAYER_COST, INNING_PLAYED, RUNS_SCORED, STRIKE_RATE, FOU_R, SIX_S, F_M)
        DF3_DATA = u.sortby_name(DF1_DATA)
        e.writeto_excel(DF3_DATA)
        break
    else:
        print('The answer entered by you is incorrect..!!!')#if password not correct this statement will display
        
