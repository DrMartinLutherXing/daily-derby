import os, re
from datetime import datetime
from cantools.util import log, getcsvmod
from model import db, Race

races = {}

def parse():
    ifile = open(os.path.join('scrapers', 'data', 'DownloadAllNumbers.txt'))
    ofile = open(os.path.join('scrapers', 'data', 'DerbyData.csv'), 'w')

    ofile.writelines('draw_num,draw_date,win_num,win_name,place_num,place_name,show_num,show_name,race_time\n')
    for i in range(5): ifile.next()
    for line in ifile:
        line = re.sub(r'\s{2,15}', r',', line)
        line = re.sub(r'(\w{3}\.\s\w{3}\s\d{2},\s\d{4})',r'"\1"',line)
        ofile.writelines(line[:-1] + '\n')

def scrape():
    dp = os.path.join("scrapers", "data", "DerbyData.csv")
    log("scraping %s"%(dp,))
    csv = getcsvmod(dp)
    keys = csv[0]
    log("keys: %s"%(keys,), 1)
    for row in csv[1:]:
        draw = row[0]
        if draw not in races:
            log("can't find %s -- querying db"%(draw,), 2)
            race = Race.query(Race.draw_num == draw).get()
            if not race:
                log("no record of %s -- creating one"%(draw,), 3)
                race = Race(draw_num=draw)
                log("data: %s"%(row,), 4)
                for index, data in enumerate(row[1:]):
                    k = keys[index + 1]
                    if k == "draw_date":
                      data = datetime.strptime(data, "%a. %b %d, %Y")
                    setattr(race, k, data)
                races[draw] = race
    puts = races.values()
    log("putting %s races"%(len(puts),), 1)
    db.put_multi(puts)
    log("finished!", 1)

