class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name=name
        self.__sprint=sprint
        self.__dribble=dribble
        self.__passing=passing
        self.__shooting=shooting
        
    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        return f"Player: {self.__name}\nSprint: {self.__sprint}\nDribble: {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}" 
    

class Team:
    def __init__(self, name, rating):
        self.__name=name
        self.__rating=rating
        self.__players=[]
        
    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"
    
    def remove_player(self, player_name):
        player=next((p for p in self.__players if p.name==player_name), None)
        if player:
            self.__players.remove(player)
            return player
        return f"Player {player_name} not found"


p = Player("Pall", 1, 3, 5, 7) 

 

print("Player name:", p.name) 

print("Points sprint:", p._Player__sprint) 

print("Points dribble:", p._Player__dribble) 

print("Points passing:", p._Player__passing) 

print("Points shooting:", p._Player__shooting) 

 

print("\ncalling the __str__ method") 

print(p) 

 

print("\nAbout the team") 

t = Team("Best", 10) 

print("Team name:", t._Team__name) 

print("Teams points:", t._Team__rating) 

print("Teams players:", len(t._Team__players)) 

print(t.add_player(p)) 

print(t.add_player(p)) 

print("Teams players:", len(t._Team__players)) 

print(t.remove_player("Pall")) 

print(t.remove_player("Pall")) 
        