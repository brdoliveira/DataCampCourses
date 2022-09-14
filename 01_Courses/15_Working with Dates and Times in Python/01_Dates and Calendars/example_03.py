from datetime import date

# Example date
d = date(2017,1,5)

# ISO format: YYYY-MM-DD
print(d)

# Express the date in ISO 8601  format and put it in a list
print([d.isoformat()])

# A few date that computers once had trouble with
some_dates = ['2000-01-01','1999-12-31']

# Print them in order
print(sorted(some_dates))

print(d.strftime("%Y"))

# Format string with more text in it
print(d.strftime("Year is %Y"))

# Format: YYYY/MM/DD
print(d.strftime("%Y/%m/%d"))

print(d.strftime("%Y-%m")) # Print the date in the format 'YYYY-MM
print(d.strftime("%B (%Y)")) # Print the date in the format 'MONTH (YYYY)' - May (2017)
print(d.strftime("%Y-%j")) # where d is the day of the year - (365 - d.day)