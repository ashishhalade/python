"""displaying all data"""
def displayby_team(df_data, j_d):#displaying by team
    '''displaying by team'''
    te_am = df_data[df_data.Team == j_d]
    print(te_am)
def trackby_playercost(df_data, y_d):#track by player cost and it will be displayed
    '''track by player cost'''
    track_s = df_data[df_data.Player_cost == y_d]
    print(track_s)
    