class QSO:
    def __init__(self, band, mode, country, operator, date, signal_report):
        self.band = band
        self.mode = mode
        self.country = country
        self.operator = operator
        self.date = date
        self.signal_report = signal_report

    def __repr__(self):
        return f"QSO({self.band}, {self.mode}, {self.country}, {self.operator}, {self.date}, {self.signal_report})"
