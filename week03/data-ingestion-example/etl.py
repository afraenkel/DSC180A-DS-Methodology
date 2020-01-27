
import pandas as pd
import os


def get_season(team, year):
    '''
    return a table of season statistics for a
    given team and year.
    '''
    url = 'https://www.pro-football-reference.com/teams/%s/%d.htm' % (team, year)
    table_num = 1
    return pd.read_html(url)[table_num]


def get_data(years, teams, outdir):
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
            tab = get_season(team, year)
            filename = '%s_%s.csv' % (team, year)
            tab.to_csv(os.path.join(outdir, filename))
            
    return
