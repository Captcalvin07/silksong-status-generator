from datetime import datetime, timedelta, date
import calendar

def generate_status():
  day_of_year = datetime.now().timetuple().tm_yday
  current_month = (datetime.now() + timedelta(days=1)).strftime("%B")
  days_remaining = 365-day_of_year-1
  percentage_chance = "{:.4f}".format(100/days_remaining)
  chance_difference = "{:.4f}".format((100/days_remaining)-(100/(days_remaining+1)))

  today = date.today()
  tommorow = today + timedelta(days=1)
  last_day = calendar.monthrange(tommorow.year, tommorow.month)[1]

  if (tommorow.day - today.day) != 1:
    days_remaining_month = last_day - tommorow.day + 1
  else:
    days_remaining_month = last_day - today.day

  month_chance = "{:.4f}".format(100/(days_remaining/days_remaining_month))

  return percentage_chance + "% chance of Silksong tomorrow, " + chance_difference + "% more than yesterday. "+ month_chance + "% chance of Silksong in " + current_month + "."
