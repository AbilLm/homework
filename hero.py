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
               f'{self.hp_x2()}'


    def __len__(self):
        return len(f'{self.catchphrase}')

hero = SuperHero('Amir', 'Allmight', 'fire', 100 , 'i love tacoo')
print(hero)
print(len(hero))
print(hero.heronamme())
print(hero.hp_x2())
print(hero.nick())
