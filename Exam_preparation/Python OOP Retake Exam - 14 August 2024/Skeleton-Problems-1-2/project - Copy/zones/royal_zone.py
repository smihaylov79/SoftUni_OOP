from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    VOLUME=10
    def __init__(self, code:str):
        super().__init__(code, self.VOLUME)

        self.zone_type='RoyalZone'

    def zone_info(self):
        # all_ships=self.get_ships()
        pirate_ships=[s for s in self.ships if s.ship_type =='PirateBattleship']
        ship_names=[s.name for s in self.get_ships()]
        result=(f"@Royal Zone Statistics@\nCode: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the Royal Zone: {len(self.ships)}, {len(pirate_ships)} out of them are Pirate Battleships.)\n")
        if ship_names:
            result+=f'#{", ".join(ship_names)}#'
        return result


