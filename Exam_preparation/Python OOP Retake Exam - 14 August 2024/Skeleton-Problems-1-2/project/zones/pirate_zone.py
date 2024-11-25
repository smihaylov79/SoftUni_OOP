from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    VOLUME=8
    def __init__(self, code: str):
        super().__init__(code, volume=self.VOLUME)

        self.zone_type = 'Pirate'

    def zone_info(self):
        # all_ships=self.get_ships()
        royal_ships=[s for s in self.ships if s.ship_type =='Royal']
        ship_names=[s.name for s in self.get_ships()]
        result=(f"@Pirate Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the Pirate Zone: {len(self.ships)}, {len(royal_ships)} out of them are Royal Battleships.\n")
        if ship_names:
            result+=f'#{", ".join(ship_names)}#'
        return result