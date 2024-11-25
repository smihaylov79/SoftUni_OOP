from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    valid_equipment={"KneePad":KneePad, "ElbowPad":ElbowPad}
    valid_teams={"OutdoorTeam":OutdoorTeam, "IndoorTeam":IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment:[BaseEquipment]=[]
        self.teams:[BaseTeam]=[]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name=value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.valid_equipment:
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.valid_equipment[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.valid_teams:
            raise Exception("Invalid team type!")
        if self.capacity == 0:
            return f"Not enough tournament capacity."
        cur_team=self.valid_teams[team_type](team_name, country, advantage)
        self.teams.append(cur_team)
        self.capacity-=1
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        cur_team=self.__get_team(team_name)
        cur_eq=self.__get_eq(equipment_type)[-1]
        if cur_team.budget<cur_eq.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(cur_eq)
        cur_team.equipment.append(cur_eq)
        cur_team.budget-=cur_eq.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        cur_team=self.__get_team(team_name)
        if cur_team is None:
            raise Exception("No such team!")
        if cur_team.wins>0:
            raise Exception(f"The team has {cur_team.wins} wins! Removal is impossible!")
        self.teams.remove(cur_team)
        self.capacity+=1
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        eqipments=self.__get_eq(equipment_type)
        for eq in eqipments:
            eq.increase_price()
        return f"Successfully changed {len(eqipments)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        t1=self.__get_team(team_name1)
        t2=self.__get_team(team_name2)
        if not t1.team_type==t2.team_type:
            raise Exception("Game cannot start! Team types mismatch!")
        t1_points=sum([e.protection for e in t1.equipment])+t1.advantage
        t2_points=sum([e.protection for e in t2.equipment])+t2.advantage
        if t1_points>t2_points:
            t1.win()
            return f"The winner is {team_name1}."
        elif t2_points>t1_points:
            t2.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams=sorted(self.teams, key=lambda team: -team.wins)
        result=f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"
        for t in sorted_teams:
            result += f"\n{t.get_statistics()}"
        return result

    def __get_team(self, team_name: str):
        cur_team=next((t for t in self.teams if t.name==team_name), None)
        return cur_team

    def __get_eq(self, equipment_type: str):
        lst_eq=[eq for eq in self.equipment if eq.EQ_TYPE==equipment_type]
        return lst_eq if lst_eq else []

