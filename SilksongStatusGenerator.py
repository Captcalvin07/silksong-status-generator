import datetime

def generate_status():
  today = datetime.date.today()
  #today = datetime.date(2025,9,16)
  last_day = datetime.date(2025,9,18)
  first_day = datetime.date(2025,6,5)
  diff = first_day - today

  days_remaining = (last_day - today).days
  percent = 100/days_remaining
  precision = 5-len(str(int(percent)))
  if precision == 4:
    chance = "{:.4f}".format(percent)
  elif precision == 3:
    chance = "{:.3f}".format(percent)
  elif precision == 2:
    chance = "{:.2f}".format(percent)
  
  if diff.days > 0:
    word = " day" if diff.days == 1 else " days"
    return str(diff.days) + word + " until possible Silksong. If it could release now, we'd have a " + chance + "% chance Silksong tommorow!"

  if diff.days <= 0:
    words = " day remains!" if precision == 2 else " days remains!"
    return chance + "% chance Silksong tommorow, " + str(days_remaining) + " possible" + words
print (generate_status())
