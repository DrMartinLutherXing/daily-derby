from cantools import db

class Race(db.ModelBase):
  draw_num  = db.Integer()
  draw_date = db.DateTime()
  win_num = db.Integer()
  win_name = db.String()
  place_num = db.Integer()
  place_name = db.String()
  show_num = db.Integer()
  show_name = db.String()
  race_time = db.String()

  def data(self):
    return {
      "key": self.key.urlsafe(),
      "draw_num": self.draw_num,
      "win_num": self.win_num,
      "win_name": self.win_name,
      "place_num": self.place_num,
      "place_name": self.place_name,
      "show_num": self.show_num,
      "show_name": self.show_name,
      "race_time": self.race_time
    }
