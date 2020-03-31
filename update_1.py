"""updating all data"""
import pandas as pd
import random
def update_score(df_data):#function written for updating the score by 10%
    '''update score'''
    for i in range(len(df_data)):
        df_data.loc[i, "runs_scored"] = (df_data.loc[i, 'runs_scored']+(df_data.loc[i, 'runs_scored']/10))
    print("\nData with Updated Score:\n")
    print(df_data)
    return df_data
def add_row(df_data, a_n, t_te, ip_f, pl_c, inn_pl, ru_sc, st_r, fo_r, si_x, f_ms):#add row
    '''add rows'''
    x_data = df_data.append({"Name":a_n,
                             "Team":t_te,
                             "IPL4_Franchise":ip_f,
                             "Player_cost":pl_c,
                             "innings _played":inn_pl,
                             "runs_scored":ru_sc,
                             "Strike_rate":st_r,
                             "Fours":fo_r,
                             "Sixes":si_x,
                             "First_match":f_ms}, ignore_index=True)
    print(x_data)
    return x_data
def add_col(df_data):#function written for adding column
    '''add columns for 1st match score'''
    co_l = []
    cl_m = ['First_match']
    for i in range( len(df_data)):
        co_l.append(random.randint(0,200))
    d_frame = pd.DataFrame(co_l, columns=cl_m)
    o_data = df_data.join(d_frame)
    print(o_data)
    return o_data
def sortby_name(df_data):#function written for sorting by name
    '''Sort By player name'''
    df_data = df_data.sort_values(by='Name')
    print("\nsorted Data for name :\n")
    print(df_data)
    return df_data
    