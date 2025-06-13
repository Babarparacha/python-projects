from calendar import TextCalendar

print("Let's build a calendar")

year = int(input("Enter year: "))
cal = TextCalendar()

# formatyear(self, theyear, w=2, l=1, c=6, m=3)
# Arguments:
#   theyear: year to display
#   w: width of date columns
#   l: number of lines per week
#   c: spacing between months
#   m: months per row

print(cal.formatyear(year, w=2, l=1, c=8, m=3))
