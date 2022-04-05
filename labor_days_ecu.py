from datetime import date, timedelta

# (1) January 1st
# (2) Carnival
# (1) Holy Friday
# (1) Day of Workers
# (1) Battle Of Pichincha
# (1) Independence Day
# (1) Independence of Guayaquil
# (1) Day of the Dead
# (1) Independence of Cuenca
# (1) Christmas
# -----------------------------
NUM_HOLIDAYS = 11  # TOTAL

start_date = date.fromisoformat('2000-01-01')
end_date = date.fromisoformat('2021-12-31')
labor_days = {}

print("AMOUNT OF LABOR DAYS PER YEAR, IN ECUADOR")
print(70*"-")
while start_date != end_date:
    # Is date saturday or sunday?
    if not ((start_date.weekday() == 5) | (start_date.weekday() == 6)):
        if start_date.year not in labor_days:
            labor_days[start_date.year] = 0
        labor_days[start_date.year] += 1

    start_date += timedelta(days=1)

for k, v in labor_days.items():
    labor_days[k] = v - NUM_HOLIDAYS
    print("Year {}: {} labor days".format(k, labor_days[k]))
