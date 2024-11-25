from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES={"ArcticClimber":ArcticClimber, "SummitClimber":SummitClimber}
    PEAK_TYPES = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
    def __init__(self):
        self.climbers=[]
        self.peaks=[]

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."
        climber=next((c for c in self.climbers if c.name==climber_name), None)
        if climber is not None:
            return f"{climber_name} has been already registered."
        new_climber=self.CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."
        peak=self.PEAK_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: [str]):
        peak = [p for p in self.peaks if p.name == peak_name][0]
        rec_gears=peak.get_recommended_gear()
        climber= [c for c in self.climbers if c.name==climber_name][0]
        missing=[]
        for g in rec_gears:
            if g not in gear:
                missing.append(g)
        if missing:
            climber.is_prepared= False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing))}."
        else:
            return f"{climber_name} is prepared to climb {peak_name}."



    def perform_climbing(self, climber_name: str, peak_name: str):
        climber=next((c for c in self.climbers if c.name==climber_name), None)
        peak=next((p for p in self.peaks if p.name==peak_name), None)
        if climber is None:
            return f"Climber {climber_name} is not registered yet."
        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."
        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.calculate_difficulty_level()}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        elif not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."


    def get_statistics(self):
        result=f"Total climbed peaks: {len(self.peaks)}\n**Climber's statistics:**"
        sorted_climbers=sorted([c for c in self.climbers if c.conquered_peaks], key=lambda c: (-len(c.conquered_peaks), c.name))
        for climber in sorted_climbers:
            result += f"\n{climber.__str__()}"

        return result
