"""computing data"""
def scoreabove_fifty(df_data, x_d): #enter the score above which you want and display 
    '''displaying score above which you want'''
    run_s = df_data[df_data.runs_scored > x_d]
    print(run_s)
    coun_t = len(run_s['runs_scored'])
    print("\n count is:", coun_t)
    return run_s
def minin_runsscored(df_data):#displaying the minimum runs scored
    '''minimum runs scored is'''
    m_d = df_data['runs_scored']
    df_data = df_data[df_data['runs_scored'] == min(m_d)]
    print("\n minimum score is :d", df_data)
def averageof_playerscost(df_data):#calculating average of players cost
    '''average of players cost'''
    sum_of = sum(df_data['Player_cost'])
    av_g = sum_of/(len(df_data['Player_cost']))
    print("\n average of player cost is", av_g)
def max_cost(df_data):#calculating and displaying the maximum cost of player
    '''maximum amount of player cost'''
    m_a = df_data['Player_cost']
    df_data = df_data[df_data['Player_cost'] == max(m_a)]
    print("\n max score is", df_data)
    