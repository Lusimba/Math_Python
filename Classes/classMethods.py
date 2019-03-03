import datetime

class Weekday:
    @staticmethod
    def is_weekday(day):

        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True
my_date=datetime.date(2019, 2, 23)

print(Weekday.is_weekday(my_date))