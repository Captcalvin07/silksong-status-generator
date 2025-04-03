from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
print(str(365-day_of_year) + " days remain")
