from unittest import TestCase, main

from project.hero import Hero

class TestHero(TestCase):
    username='Test'
    level=5
    health=25.5
    damage=14.5

    def setUp(self):
        self.hero= Hero(self.username,self.level,self.health,self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attributes(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_check_username(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_check_hero_health(self):
        self.hero.health = 0
        enemy = Hero('Enemy', self.level, 30, 10.8)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_check_enemy_health(self):
        enemy = Hero('Enemy', self.level, 0, 10.8)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ex.exception))

        enemy = Hero('Enemy', self.level, -10, 10.8)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ex.exception))

    def test_draw_from_battle(self):
        enemy=Hero('Enemy', self.level, self.health, self.damage)
        result= self.hero.battle(enemy)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(-47.0, self.hero.health)
        self.assertEqual(14.5, self.hero.damage)
        self.assertEqual("Draw", result)

    def test_hero_win(self):
        enemy=Hero('Enemy', 1,1,1)
        result = self.hero.battle(enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(29.5, self.hero.health)
        self.assertEqual(19.5, self.hero.damage)
        self.assertEqual("You win", result)

    def test_hero_lose(self):
        enemy = Hero('Enemy', 20, 100, 101)
        result = self.hero.battle(enemy)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(-1994.5, self.hero.health)
        self.assertEqual(14.5, self.hero.damage)
        self.assertEqual("You lose", result)

        self.assertEqual(32.5, enemy.health)
        self.assertEqual(21, enemy.level)
        self.assertEqual(106, enemy.damage)

    def test_magic_method_str(self):
        expected=f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected, self.hero.__str__())


if __name__ == '__main__':
    main()