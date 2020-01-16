# Methodology Assignment 2

## Data Ingestion

### Due Friday Jan 24 11:59 PM

The methodology assignments are small assignments (doable within the
scope of lab hours) that introduce you to a tool or concept through a
simple `hello world` example.

In this assignment will you will write code to download and process
tables from the web using methods discussed in lecture. In particular,
you are going to keep separate:
1. The metadata that specificies which instances of the data to ingest
   (configuration), and
2. The code that actually retrieves, parses, and saves the data.

You will use `pd.read_html` to download [NFL football team
schedules](https://www.pro-football-reference.com/) from various
years, saving the tables to file. The table of interest is the
'Schedule & Game Results' table. For example, the table of interest is the second table on [this
page](https://www.pro-football-reference.com/teams/sdg/2016.htm)

### Outline

If the goal of the investigation is looking at game statistics for
each NFL team, over multiple years, then we would separate
configuration from code in the following way:

1. Decide what data would be reasonably useful to collect to conduct
   the investigation and specify this information as parameters in a
   configuration file. For example, in `data-params.json`, specify the
   years and different teams to download statistics about.
2. In a file `get-data.py` write a function `get_table` that takes in a team and a
   year, retrieves the data from the webpage, and writes the table to
   file in a directory called `data` in the same location. Write a
   second function `get_data` that reads in the desired data in
   `data-params.json` and uses the configuration to download all the
   tables.

For example, to download tables for the San Diego Chargers in 2014,
2015, 2016, your configuration file may look like:

```
{
    "teams": ["sdg"],
    "years": [2014, 2015, 2016],
    "outpath": "projectdir/data"
}
```

Running the function `get_data(**cfg)` on the loaded configuration
`cfg = json.load(open('data-params.json'))` would create 3 files with
the following names:
```
data/sdg_2014.csv
data/sdg_2015.csv
data/sdg_2016.csv
```

<!-- #region -->
### To Turn In

Write a configuration file `data-params.json` and python code in the
file `get-data.py` to download and save all 'Schedule and Game
Results' tables for the 49ers and Packers between 2012 and 2019 inclusive, using
the configuration file. Follow the example above for guidance.

Running the function should result in 16 csv files.

*Notes:*
* Your configuration files might have different structures (what if
  you wanted different years for different teams). Anything that works
  for this problem is fine, but this is something to think about for
  your own work.
* You may find the following functions useful:
  - `json.load` for loading json files into python objects,
  - `os.mkdir` for creating directories,
  - `os.path.exists` for checking if a given directory exists,
  - `pd.read_html` for scraping tables off of webpages.
  
  
You will not be getting starter code for this HW, however, the Gradescope assignments will run visible tests to check the basics of your work.
