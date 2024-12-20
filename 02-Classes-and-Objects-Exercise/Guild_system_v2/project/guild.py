from project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players:list[Player]=[]

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild !="Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                player.guild="Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result=f"Guild: {self.name}\n"
        for p in self.players:
            result += f"{p.player_info()}\n"
        return result
