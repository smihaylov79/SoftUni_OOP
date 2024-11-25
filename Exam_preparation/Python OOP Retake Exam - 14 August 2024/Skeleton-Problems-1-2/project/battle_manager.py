from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    zone_types = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    ship_types = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

    def __init__(self):
        self.zones = []
        self.ships = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.zone_types:
            raise Exception("Invalid zone type!")
        for zone in self.zones:
            if zone.code == zone_code:
                raise Exception("Zone already exists!")
        current_zone=self.zone_types[zone_type](zone_code)
        self.zones.append(current_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.ship_types:
            raise Exception(f"{ship_type} is an invalid type of ship!")
        current_ship = self.ship_types[ship_type](name, health, hit_strength)
        self.ships.append(current_ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        if zone.volume==0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health<=0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if ship.ship_type == zone.zone_type:
            ship.is_attacking=True
        else:
            ship.is_attacking=False

        zone.ships.append(ship)
        ship.is_available=False
        zone.volume-=1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        curr_ship=next((s for s in self.ships if s.name==ship_name), None)
        if curr_ship is None:
            return f"No ship with this name!"
        if not curr_ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"
        self.ships.remove(curr_ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):
        attackers=[s for s in zone.ships if s.is_attacking]
        targets=[s for s in zone.ships if not s.is_attacking]
        if not attackers or not targets:
            return f"Not enough participants. The battle is canceled."
        attacker=max(attackers, key=lambda s: s.hit_strength)
        target=max(targets, key=lambda s: s.health)
        attacker.attack()
        target.take_damage(attacker)
        if target.health<=0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."
        if attacker.ammunition<=0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."
        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships=[ship for ship in self.ships if ship.is_available]
        zones=sorted(self.zones, key=lambda z: z.code)
        zones_info='\n'.join(zone.zone_info() for zone in zones)

        result=f'Available Battleships: {len(available_ships)}\n'
        if available_ships:
            result += f"#{', '.join(s.name for s in available_ships)}#\n"
        # else:
        #     result += ""
        result+=f'***Zones Statistics:***\nTotal Zones: {len(zones)}'
        result+=f'\n{zones_info}'

        return result








