from EventManager import event_manager
from enemy_factory import SpawnManager

class Player:
    health = 10
    power_of_attack = 3

    def attack(self):
        event_manager.publish('attack_enemy')

def show_print():
    print('Alex')

# callback = show_print

# event_manager.subscribe('show_print', callback)
# event_manager.publish('show_print')
spawn_manager = SpawnManager()
spawn_manager.generate_zombies(10)
# b = boss.spawn_zombie('Boss')
