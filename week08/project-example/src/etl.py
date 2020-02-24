
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

def get_seasons(years, teams, outdir=None, indir=None):
    '''
    downloads and saves tables at the specified output directory
    for the given years and teams.

    :param: years: a list of seasons to collect
    :param: teams: a list of teams to collect
    :param: outpath: the directory to which to save the data.
    '''

    if outdir and not os.path.exists(outdir):
        os.makedirs(outdir)

    for team in teams:
        for year in years:

            # read raw files from disk, or pulll from http
            if indir:
                inpath = os.path.join(indir, '%s_%s.csv' % (team, year))
            else:
                inpath = None

            # read/get data
            tab = get_season(team, year, inpath)
            
            # write clean to files, or as dataframes
            filename = '%s_%s.csv' % (team, year)
            if outdir:
                tab.to_csv(os.path.join(outdir, filename))
                yield None
            else:
                yield filename, tab

    return


def clean_seasons(df_iter=(), outdir=None, indir=None):

    if outdir and not os.path.exists(outdir):
        os.makedirs(outdir)

    if not df_iter:
        df_iter = ((p, pd.read_csv(os.path.join(indir, p))) for p in os.listdir(indir))

    for pth, df in df_iter:
        cleaned = get_clean_season(df)
        if outdir:
            cleaned.to_csv(os.path.join(outdir, pth))
            yield None
        else:
            yield pth, clean_seasons(df)

    
