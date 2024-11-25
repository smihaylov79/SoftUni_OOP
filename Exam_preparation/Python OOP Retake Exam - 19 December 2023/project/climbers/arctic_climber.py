from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    STRENGTH=200
    MIN_STRENGHT=100
    def __init__(self, name):
        super().__init__(name, strength=self.STRENGTH)

    def climb(self, peak: BasePeak):
        self.conquered_peaks.append(peak.name)
        self.strength -=20*(2 if peak.difficulty_level=='Extreme' else 1.5)

    def can_climb(self):
        return  self.strength>=self.MIN_STRENGHT
