class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def heronamme(self):
        return f'my name is {self.name}'
    def hp_x2(self):

        return f'health: {self.health_points * 2}'

    def nick(self):
        return f'my nickname is {self.nickname}'

    def __str__(self):
        return f'{self.nick()}\n' \
               f'my superpower is {self.superpower}\n' \
               f'{self.health_points}'


    def __len__(self):
        return len(f'{self.catchphrase}')

class Earth_hero(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage
    def hp_x2(self):
        self.fly = True
        return f'health: {self.health_points ** 2}'

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


class Cosmic_hero(SuperHero):
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, fly=False, damage=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly = fly
        self.damage = damage
    def hp_x2(self):
        self.fly = True
        return f'health: {self.health_points ** 2}'

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


class Villian(Cosmic_hero):
    SuperHero.people = 'monster'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_x(self): ...

    def crit(self, hero):
        return hero.damage ** 2

    def __str__(self):
        return f'{self.damage}'

thor = Cosmic_hero('thor', 'God', 'Thunder', 200, 'Im thor odinson!', damage=300)
Toni = Earth_hero('cap', 'pon', 'Mind', 150, 'Jarviz', damage=100)
thor.hp_x2()
thor.fly_sky()
Toni.hp_x2()
Toni.fly_sky()
tanos = Villian('tanos', 'Conquerer', 'Gauntlet', 900, 'Try me bitch')
print(Villian.crit(tanos, thor))
print(Villian.crit(tanos, Toni))