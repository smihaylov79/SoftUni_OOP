from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    valid_divers={"FreeDiver":FreeDiver, "ScubaDiver":ScubaDiver}
    valid_fish={"PredatoryFish":PredatoryFish, "DeepSeaFish":DeepSeaFish}

    def __init__(self):
        self.divers=[]
        self.fish_list=[]

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.valid_divers:
            return f"{diver_type} is not allowed in our competition."
        cur_diver_check=next((d for d in self.divers if d.name==diver_name),None)
        if cur_diver_check:
            return f"{diver_name} is already a participant."
        cur_diver=self.valid_divers[diver_type](diver_name)
        self.divers.append(cur_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.valid_fish:
            return f"{fish_type} is forbidden for chasing in our competition."
        cur_fish_check = next((f for f in self.fish_list if f.name == fish_name), None)
        if cur_fish_check:
            return f"{fish_name} is already permitted."
        cur_fish = self.valid_fish[fish_type](fish_name, points)
        self.fish_list.append(cur_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        cur_diver=next((d for d in self.divers if d.name==diver_name), None)
        if cur_diver is None:
            return f"{diver_name} is not registered for the competition."
        cur_fish=next((f for f in self.fish_list if f.name==fish_name), None)
        if cur_fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if cur_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        if cur_diver.oxygen_level < cur_fish.time_to_catch:
            cur_diver.miss(cur_fish.time_to_catch)
            if cur_diver.oxygen_level == 0:
                cur_diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        elif cur_diver.oxygen_level == cur_fish.time_to_catch:
            if is_lucky:
                cur_diver.hit(cur_fish)
                if cur_diver.oxygen_level == 0:
                    cur_diver.update_health_status()
                return f"{diver_name} hits a {cur_fish.points}pt. {fish_name}."
            else:
                cur_diver.miss(cur_fish.time_to_catch)
                if cur_diver.oxygen_level == 0:
                    cur_diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."
        else:
            cur_diver.hit(cur_fish)
            if cur_diver.oxygen_level == 0:
                cur_diver.update_health_status()
            return f"{diver_name} hits a {cur_fish.points}pt. {fish_name}."

    def health_recovery(self):
        counter=0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.renew_oxy()
                diver.update_health_status()
                counter+=1
        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        cur_diver=next(d for d in self.divers if d.name==diver_name)
        result=f"**{diver_name} Catch Report**"
        for f in cur_diver.catch:
            result+=f"\n{f.fish_details()}"
        return result

    def competition_statistics(self):
        divers=[d for d in self.divers if not d.has_health_issue]
        sorted_divers=sorted(divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result="**Nautical Catch Challenge Statistics**"
        for diver in sorted_divers:
            result+=f"\n{diver.__str__()}"
        return result
