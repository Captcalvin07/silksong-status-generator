from datetime import datetime

def generate_status():
  day_of_year = datetime.now().timetuple().tm_yday
  days_remaining = 365-day_of_year
  percentage_chance = "{:.4f}".format(100/days_remaining)
  return percentage_chance + "% chance Silksong tommorow. " + str(days_remaining) + " days remain in 2025"
