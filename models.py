class QSO:
    def __init__(self, band_id, mode_id, country_id, operator, qso_date, qso_time, frequency, rst_sent, rst_received, grid_square):
        self.band_id = band_id
        self.mode_id = mode_id
        self.country_id = country_id
        self.operator = operator
        self.qso_date = qso_date
        self.qso_time = qso_time
        self.frequency = frequency
        self.rst_sent = rst_sent
        self.rst_received = rst_received
        self.grid_square = grid_square

    def __repr__(self):
        return f"QSO({self.band_id}, {self.mode_id}, {self.country_id}, {self.operator}, {self.qso_date}, {self.qso_time}, {self.frequency}, {self.rst_sent}, {self.rst_received}, {self.grid_square})"
