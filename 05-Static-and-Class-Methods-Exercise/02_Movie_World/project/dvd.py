import calendar

class DVD:

    def __init__(self, name, did, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = did
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented=False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _, month, year = [int(dt) for dt in date.split('.')]
        month_name=calendar.month_name[month]
        return cls(name, id, year, month_name, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
