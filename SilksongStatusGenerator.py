from datetime import datetime, timedelta, date
import calendar

def generate_status():
  day_of_year = datetime.now().timetuple().tm_yday
  current_month = datetime.now().strftime("%B")
  days_remaining = 365-day_of_year-1
  percentage_chance = "{:.4f}".format(100/days_remaining)

  today = date.today()
  last_day = calendar.monthrange(today.year, today.month)[1]
  days_remaining_month = last_day - today.day

  month_chance = "{:.4f}".format(100/(days_remaining/days_remaining_month))

  return percentage_chance + "% chance of Silksong tomorrow. " + month_chance + "% chance of Silksong in " + current_month + "."
