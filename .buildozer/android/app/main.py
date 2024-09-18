from kivy.app import App
from kivy.uix.label import Label
from datetime import datetime
import math

class MoonPhaseCalculator:
    @staticmethod
    def calculate_moon_phase():
        # Reference date for a known new moon
        known_new_moon = datetime(2000, 1, 6, 18, 14)
        # Current date and time
        now = datetime.utcnow()

        # Number of days since the known new moon
        diff = now - known_new_moon
        days = diff.total_seconds() / 86400.0

        # Calculate the moon's age (days since new moon)
        moon_age = days % 29.53058867  # Average lunar cycle duration in days

        # Determine the phase based on the moon's age
        if moon_age < 1.84566:
            phase = "New Moon"
        elif moon_age < 5.53699:
            phase = "Waxing Crescent"
        elif moon_age < 9.22831:
            phase = "First Quarter"
        elif moon_age < 12.91963:
            phase = "Waxing Gibbous"
        elif moon_age < 16.61096:
            phase = "Full Moon"
        elif moon_age < 20.30228:
            phase = "Waning Gibbous"
        elif moon_age < 23.99361:
            phase = "Last Quarter"
        elif moon_age < 27.68493:
            phase = "Waning Crescent"
        else:
            phase = "New Moon"

        return phase

class MoonPhaseApp(App):
    def build(self):
        moon_phase = MoonPhaseCalculator.calculate_moon_phase()
        return Label(text=f"Current Moon Phase: {moon_phase}", font_size='20sp')

if __name__ == '__main__':
    MoonPhaseApp().run()