start_year = 1900
end_year = 2000
shorter_months = [4, 6, 9, 11]
daytick = 1
total = 0
for year in range(start_year, end_year + 1):
    for month in range(1, 12 + 1):
        if month in shorter_months:
            days = 30
        elif month == 2:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        days = 29
                    else:
                        days = 28
                else:
                    days = 29
            else:
                days = 28
        else:
            days = 31
        for day in range(1, days + 1):
            if daytick % 7 == 0:
                if year >= 1901:
                    if day == 1:
                        total += 1
            daytick += 1
print total
