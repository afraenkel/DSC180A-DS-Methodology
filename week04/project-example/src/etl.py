
import pandas as pd
import os


def get_season_http(team, year):
    '''
    return a table of season statistics for a
    given team and year.
    '''
    url = 'https://www.pro-football-reference.com/teams/%s/%d.htm' % (team, year)
    table_num = 1
    df = pd.read_html(url)[table_num]
    df = df.T.reset_index(level=0, drop=True).T
    return df


def get_season_local(inpath):
    '''
    return a table of season statistics for a given 
    team and year, from a location on local disk.
    '''
    df = pd.read_csv(inpath, skiprows=1)
    return df


def get_season(team, year, inpath=None):
    '''
    return a table of season statistics for a
    given team and year.
    '''

    if not inpath:
        return get_season_http(team, year)
    else:
        return get_season_local(inpath)


def get_clean_season(df):
    '''
    cleans an output dataframe from `get_season`.
    Takes only the Regular Season and deletes the Bye Week.
    '''

    return df.iloc[:17].dropna(subset=['Date'])


# ---------------------------------------------------------------------
# Driver Function
# ---------------------------------------------------------------------

def get_data(years, teams, outdir, **kwargs):
    '''
    downloads and saves tables at the specified output directory
    for the given years and teams.

    :param: years: a list of seasons to collect
    :param: teams: a list of teams to collect
    :param: outpath: the directory to which to save the data.
    '''

    if not os.path.exists(outdir):
        os.mkdir(outdir)
    
    for team in teams:
        for year in years:
            tab = get_season(team, year, **kwargs)
            cleaned = get_clean_season(tab)
            filename = '%s_%s.csv' % (team, year)
            cleaned.to_csv(os.path.join(outdir, filename))
            
    return
