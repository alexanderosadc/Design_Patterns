from enemy_factory import EnemySpawnManager
from player import RealPlayer, ProxyPlayer
from game_renderer import UIRenderer, ButtonsRenderer, ButtonTextRenderer
# Facade class in games usually serves GameManager. It controls entire game, and gives some sort
    # of hiding the hard structure of the game

class GameManager:
    def __init__(self):
        self._spawn_manager = EnemySpawnManager()
        self._real_player = RealPlayer(10, 5)
        self.proxy_player = ProxyPlayer(self._real_player)

    def start_game(self, number_of_enemies, number_of_turns):
        self.render_ui()
        self._spawn_manager.generate_zombies(number_of_enemies)
        self.proxy_player.attack()

        for i in range(0, 10):
            zombie = self._spawn_manager.get_random_zombie()
            if zombie:
                zombie.attack()
                self.proxy_player.attack()
                self.proxy_player.save_state()
            self.proxy_player.show_history_of_powers()


    def render_ui(self):
        pc_parameters = {
            'screen_resolution': '1920x1080',
            'text': 'Hello',
            'font_family': 'Courier',
            'text_size': 12
        }
        text_renderer = ButtonTextRenderer()
        button_renderer = ButtonsRenderer(text_renderer)
        ui_renderer = UIRenderer(button_renderer)

        ui_renderer.handle(pc_parameters)
