import pandas as pd
import sqlite3


# load data
female_lfp = pd.read_csv('data/female-labor-force-participation-rates.csv')

#save to csv
female_lfp.to_csv("data/analysis.csv")

#create connection to sql database
conn = sqlite3.connect('workforce.db')