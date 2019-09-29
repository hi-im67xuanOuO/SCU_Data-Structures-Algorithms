class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = int(date.split("-")[0]), int(date.split("-")[1]), int(date.split("-")[2])
        leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        s = sum(days[0:m-1]) + d
        if leap and m > 2: s += 1
        return s
