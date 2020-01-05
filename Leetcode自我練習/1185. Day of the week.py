from datetime import date
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ddate = date(year,month,day)
        week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return week[ddate.weekday()]
