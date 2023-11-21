class Pokemon:
    def __init__(self, name, abilities, poke_id):
        self._name = name
        self._abilities = abilities
        self._id = poke_id

    def get_name(self):
        return self._name
    
    def get_abilities(self):
        return self._abilities
    
    def get_id(self):
        return self._id
