from enemy_factory import EnemySpawnManager
from player import RealPlayer, ProxyPlayer


class GameManager:  # Facade class in games usually serves GameManager. It controls entire game, and gives some sort
    # of hiding the hard structure of the game
    def __init__(self):
        self._spawn_manager = EnemySpawnManager()
        self._real_player = RealPlayer(10, 5)
        self.proxy_player = ProxyPlayer(self._real_player)

    def start_game(self, number_of_enemies, number_of_turns):
        self._spawn_manager.generate_zombies(number_of_enemies)
        self.proxy_player.attack()
        for i in range(0, 10):
            zombie = self._spawn_manager.get_random_zombie()
            if zombie:
                zombie.attack()
