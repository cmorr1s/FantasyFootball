# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
# import argparse
# import numpy as np
import urllib2 as url2
from bs4 import BeautifulSoup

def scrape_data(url):
    """
    Scrape user passed website for Player Rankings based on ADP.
    """
    page = url2.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')
    
    table = soup.find_all("table")[0]
    table_list = []
    
    for row in table.find_all("tr"):
        columns = row.find_all('td')
        for col in columns:
            table_list.append(col.get_text())
    
    return table_list


def create_df(table_list):
    chunks = [table_list[x:x+10] for x in range(0, len(table_list), 10)]
    col_names = ['RANK',
                 'NAME',
                 'POS',
                 'ESPN',
                 'MFL',
                 'FFC',
                 'RTSPORTS',
                 'FANTRAX',
                 'DW',
                 'AVG']
    
    adp_players = pd.DataFrame(chunks,
                               columns = col_names)
    
    return adp_players



if __name__ == '__main__':
    url = "https://www.fantasypros.com/nfl/adp/ppr-overall.php"
    # TODO: Ability to pass any url and we pull data
    raw_data = scrape_data(url)
    adp_players = create_df(raw_data)