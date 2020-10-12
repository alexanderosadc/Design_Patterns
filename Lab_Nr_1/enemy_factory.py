import abc
from abc import ABC
from random import randint

from EventManager import event_manager


class Enemy(metaclass=abc.ABCMeta):
    def __init__(self):
        self._zombie_name = ''
        self._health = 10
        self._is_enemy_dead = False
        self._attack_power = 1
    def get_health(self):
        return self._health

    def get_strength(self):
        return self._attack_power

    def verify_if_enemy_dead(self):
        return self._is_enemy_dead

    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def get_hit(self, hit_point):
        pass


class BossZombie(Enemy, ABC):

    def attack(self):
        event_manager.publish('attack_player', self._attack_power * 2)

    def get_hit(self, hit_point):
        self._health -= hit_point / 2
        if self._health <= 0:
            self._is_enemy_dead = True
            event_manager.publish('enemy_dead', 'Boss')


class SimpleZombie(Enemy, ABC):

    def attack(self):
        event_manager.publish('attack_player', self._attack_power)

    def get_hit(self, hit_point):
        self._health -= hit_point
        if self._health <= 0:
            self._is_enemy_dead = True
            event_manager.publish('enemy_dead', 'Simple')


class EnemyPool:
    def __init__(self):
        self._pool_of_simple_zombies = []
        self._pool_of_boss_zombies = []

    def add_zombie_to_pool(self, enemy, type_of_enemy):
        if type_of_enemy == 'Boss':
            self._pool_of_boss_zombies.append(enemy)
        elif type_of_enemy == 'Simple':
            self._pool_of_simple_zombies.append(enemy)

    def find_dead_zombie(self, type_of_enemy):
        if type_of_enemy == 'Boss':
            return self.scroll_all_zombies(self._pool_of_boss_zombies)
        elif type_of_enemy == 'Simple':
            return self.scroll_all_zombies(self._pool_of_simple_zombies)

    def scroll_all_zombies(self, array_of_zombies):
        for element in array_of_zombies:
            if element.verify_if_enemy_dead() is False:
                return element

    def delete_zombie_from_pool(self, enemy, type_of_enemy):
        if type_of_enemy == 'Boss':
            self._pool_of_boss_zombies.pop(enemy)
        elif type_of_enemy == 'Simple':
            self._pool_of_simple_zombies.pop(enemy)

class EnemyFactory:

    def spawn_zombie(self, name_of_enemy):
        if name_of_enemy == 'Boss':
            print('Boss')
            return BossZombie
        elif name_of_enemy == 'Simple':
            print('Simple')
            return SimpleZombie

class SpawnManager:
    def __init__(self):
        self.pool_manager = EnemyPool()
        self.enemy_factory = EnemyFactory()
        event_manager.subscribe('enemy_dead', self.update_zombie_states)

    def generate_zombies(self, number_of_enemies):
        type_of_zombies = ['Boss', 'Simple']

        while number_of_enemies > 0:
            type_of_zombie = type_of_zombies[randint(0, 1)]
            enemy = self.enemy_factory.spawn_zombie(type_of_zombie)
            self.pool_manager.add_zombie_to_pool(enemy)
            number_of_enemies -= 1

    def update_zombie_states(self, type_of_enemy):
        self.pool_manager.find_dead_zombie()

