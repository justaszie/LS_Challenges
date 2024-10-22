from datetime import date, timedelta
class Meetup:
    QUANTIFIERS_NUMERIC = {
        'first': 0,
        'second': 1,
        'third': 2,
        'fourth': 3,
        'fifth': 4
    }

    WEEKDAYS_NUMERIC = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7,
    }

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_weekdays(self, weekday):
        days = []

        current_date = date(self.year, self.month, 1)
        while current_date.month == self.month:
            if (current_date.isoweekday() ==
                Meetup.WEEKDAYS_NUMERIC[weekday]):
                days.append(current_date.day)

            current_date += timedelta(days=1)

        return days

    def day(self, weekday, quantifier):
        quantifier = quantifier.lower()
        weekday = weekday.lower()

        candidates = self.get_weekdays(weekday)

        try:
            match quantifier:
                case 'teenth':
                    day = min([day for day in candidates if 13 <= day <= 19])
                case 'last':
                    day = candidates[-1]
                case _:
                    idx = Meetup.QUANTIFIERS_NUMERIC[quantifier]
                    day = candidates[idx]

        except (IndexError, ValueError):
            return None

        return date(self.year, self.month, day)


if __name__ == '__main__':
    print(date(2024, 10, 21).isoweekday())
    meet = Meetup(2024, 10)
    print(meet.day('TUEsday', 'Second'))
    print(meet.day('Friday', 'teenth'))


