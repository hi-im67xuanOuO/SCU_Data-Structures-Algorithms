def centuryFromYear(year):
    # For year = 1905, the output should be centuryFromYear(year) = 20;
    # For year = 1700, the output should be centuryFromYear(year) = 17.
    if (year%100==0):
        return int(year/100)
    else:
        return int((year/100)+1)

year = 1905
year = 1700
