import abc
from abc import ABC
from event_manager import event_manager


class Player(ABC):
    @abc.abstractmethod
    def attack(self):
        pass
    @abc.abstractmethod
    def get_hit(self, power_of_hit):
        pass


class RealPlayer(Player):

    def __init__(self, initial_health, initial_power_of_attack):
        self._health = initial_health
        self._power_of_attack = initial_power_of_attack
        event_manager.subscribe('attack_player', self.get_hit)

    def attack(self):
        event_manager.publish('attack_enemy', self._power_of_attack)

    def get_current_health(self):
        return self._health

    def get_current_power_of_attack(self):
        return self._power_of_attack

    def get_hit(self, power_of_hit):
        self._health = self._health - power_of_hit


class ProxyPlayer(Player):
    def __init__(self, real_player: RealPlayer):
        self.real_player = real_player

    def attack(self):
        if self.check_if_player_is_alive() and self.check_if_has_powers():
            self.real_player.attack()
            print('Player is attacking')
        else:
            print('Player is dead')

    def get_hit(self, power_of_hit):
        if self.check_if_player_survives(power_of_hit):
            self.real_player.get_hit(power_of_hit)

    def check_if_player_survives(self, power_of_hit):
        if self.real_player.get_current_health() - power_of_hit > 0:
            return True
        else:
            return False

    def check_if_player_is_alive(self) -> bool:
        if self.real_player.get_current_health() > 0:
            return True
        else:
            return False

    def check_if_has_powers(self) -> bool:
        if self.real_player.get_current_power_of_attack() > 0:
            return True
        else:
            return False
