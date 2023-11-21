class Team:
    def __init__(self, name):
        self._name = name
        self._team_list = []


    def get_name(self):
        return self._name
    

    def get_team(self):
        serialized_list = []
        for pokemon in self._team_list:
            serialized_list.append(pokemon.get_name())
        return serialized_list

    def add_pokemon(self, pokemon):
        if len(self._team_list) < 6:
            self._team_list.append(pokemon)
        else:
            return 'Team already has 6 pokemon in it'
        
        
    # def serialize(self):
        

