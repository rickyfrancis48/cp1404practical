class Band:
    def __init__(self, name):
        self.name = name
        self.bands = []

    def __str__(self):
        return f"{self.name} ({self.bands[0]})"

    def add(self, band):
        self.bands.append(band)

    def play(self):
        """Return a string showing the instrument playing their first (or no) instrument."""
        if not self.bands:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.bands[0]}"
