import os
from cantools.util import getcsvmod
from model import db, Race

races = []

def scrape():
  csv = getcsvmod(os.path.join("scrapers", "data", "DerbyData.csv"))
  keys = csv[0]
  for row in csv[1:]:
    draw = row[0]
    if draw not in races:
      race = Race.query(Race.draw_num == draw).get()
      if not race:
        race = Race(draw_num=draw)
        for index, data in enumerate(row[1:]):
          setattr(race, keys[index], data)
        races.append(race)
  db.put_multi(races)
