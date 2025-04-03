from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
print(365-day_of_year + " days remain")
