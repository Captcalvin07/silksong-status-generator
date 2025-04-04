from datetime import datetime, timedelta

def generate_status():
  day_of_year = datetime.now().timetuple().tm_yday
  days_remaining = 365-day_of_year-1
  percentage_chance = "{:.4f}".format(100/days_remaining)
 
  chance = 1
  temp_days = days_remaining+1
  while chance > 0.5:
    temp_days -=1
    chance *= (temp_days-1)/temp_days
  guess_date = datetime(datetime.now().year, 1, 1) + timedelta(days=365-temp_days - 1)
 
  guess_day_of_month = int(guess_date.strftime("%d"))
  if 4 <= guess_day_of_month <= 20 or 24 <= guess_day_of_month <= 30:
    suffix = "th"
  else:
    suffix = ["st", "nd", "rd"][guess_day_of_month % 10 - 1]
 
  return percentage_chance + "% chance of Silksong tomorrow. 50% Chance by " + guess_date.strftime("%Y %B %d") + suffix
