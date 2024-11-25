from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    BUDGET = 500.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.BUDGET)
        self.team_type='IndoorTeam'

    def win(self):
        self.advantage += 145
        self.wins += 1