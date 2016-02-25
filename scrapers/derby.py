import os
from cantools.util import log, getcsvmod
from model import db, Race

races = {}

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
                for index, data in enumerate(row[1:]):
                    setattr(race, keys[index], data)
                races[draw] = race
    puts = races.values()
    log("putting %s races"%(len(puts),), 1)
    db.put_multi(puts)
    log("finished!", 1)