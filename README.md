# Design_Patterns
## Lab_Nr_1
Long story short. Three creational design patterns which were used: **Object Pool**, **Factory Method**, **Singleton** and also the pattern I always use in my projects **Publisher Subscriber Pattern**. 
As a field I choosed a game, where we have our player and zombies as enemies.
### Singleton and PubSub
Why this 2 patterns are going together? Because usually In the project only one Publisher Subscriber Object which is responsable for event emmitting and for event subscribing.
**Singleton** - is a pattern used for instantating an instance of the class only one time, so at the end we will have only one object of this class in the project.
In this project I can create only one time *EventManager*
**Publisher-Subscriber** - used for indirect communication between the objects. In my case I use for notifying my *SpawnManager* that the enemy is dead and that I need to spawn another enemy. So here comes *Pooling Manager*
**Pooling Manager** in my case is responsable for respawning the enemies of the same type. For user it feels like these are different objects, but in fact with the help of Pooling Manager these are same objects only with restored health. So I don't need to spend resources of my device on creating and destroying same type of objects.
**Factory Method** - I use this to have different types of Enemies. So I have the main class *Enemy* with abstract methods. I inherit that class to the *BossEnemy* and *SimpleEnemy* classes. To make my life easier I created class *EnemyFactory* to create instances of Enemies.
