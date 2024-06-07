MAX_ENERGY = 100
MIN_ENERGY = 0

class Player:
    def __init__(self, id_player, nick_name):
        self.__idPlayer = id_player
        self.__nickName = nick_name
        self.__energy = (MAX_ENERGY - MIN_ENERGY) // 2

    def getIdPlayer(self):
        return self.__idPlayer

    def setIdPlayer(self, id_player):
        self.__idPlayer = id_player

    def getNickName(self):
        return self.__nickName

    def setNickName(self, nick_name):
        self.__nickName = nick_name

    def getEnergy(self):
        return self.__energy

    def __setEnergy(self, energy):
        if MIN_ENERGY <= energy <= MAX_ENERGY:
            self.__energy = energy
        else:
            raise ValueError("Energía fuera del rango permitido")

    def toString(self):
        return f'[{self.__idPlayer}, {self.__nickName}, {self.__energy}]'

    def boost(self, charge):
        if not isinstance(charge, int):
            charge = 0
        new_energy = self.__energy + charge
        if new_energy < MIN_ENERGY:
            new_energy = MIN_ENERGY
        elif new_energy > MAX_ENERGY:
            new_energy = MAX_ENERGY
        self.__setEnergy(new_energy)
        return charge, self.__energy
