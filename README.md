# Design_Patterns
## Lab_Nr_1
Long story short. Three creational design patterns which were used: **Object Pool**, **Factory Method**, **Singleton** and also the pattern I always use in my projects **Publisher Subscriber Pattern**. \
As a field I choosed a game, where we have our player and zombies as enemies.
### Singleton and PubSub
Why this 2 patterns are going together? Because usually In the project only one Publisher Subscriber Object which is responsable for event emmitting and for event subscribing.\
**Singleton** - is a pattern used for instantating an instance of the class only one time, so at the end we will have only one object of this class in the project.
In this project I can create only one time *EventManager*\
**Publisher-Subscriber** - used for indirect communication between the objects. In my case I use for notifying my *SpawnManager* that the enemy is dead and that I need to spawn another enemy. So here comes *Pooling Manager*\
**Pooling Manager** in my case is responsable for respawning the enemies of the same type. For user it feels like these are different objects, but in fact with the help of Pooling Manager these are same objects only with restored health. So I don't need to spend resources of my device on creating and destroying same type of objects.\
**Factory Method** - I use this to have different types of Enemies. So I have the main class *Enemy* with abstract methods. I inherit that class to the *BossEnemy* and *SimpleEnemy* classes. To make my life easier I created class *EnemyFactory* to create instances of Enemies.
## Lab_Nr_2
**Facade**
Facade in game dev usually uses a special class called GameManager which manages all the interactions in game. It hides the complex structure of the game and in the main program is only called method start_game() from  game_mananger object.
    
    class GameManager:  
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
**Proxy**
Proxy is used as intermediate object between real player and enemies which attack the player.

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
**Flyweight**
Used for creating 2 types of enemies 'Boss_Enemy' and 'Simple Enemy'

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
