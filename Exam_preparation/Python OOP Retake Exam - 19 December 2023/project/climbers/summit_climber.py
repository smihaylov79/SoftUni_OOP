from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    STRENGTH = 150
    MIN_STRENGHT = 75

    def __init__(self, name):
        super().__init__(name, strength=self.STRENGTH)

    def climb(self, peak: BasePeak):
        self.conquered_peaks.append(peak.name)
        self.strength -= 30 * (1.3 if peak.difficulty_level == 'Advanced' else 2.5)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGHT
