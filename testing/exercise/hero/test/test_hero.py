from unittest import TestCase

from project.hero import Hero


class HeroTests(TestCase):
    ATTACKER_USERNAME = 'Attacker'
    LEVEL = 7
    HEALTH = 100
    DAMAGE = 65

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.attacker = Hero(self.ATTACKER_USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

    def test_hero_init(self):
        self.assertEqual(self.ATTACKER_USERNAME, self.attacker.username)
        self.assertEqual(self.LEVEL, self.attacker.level)
        self.assertEqual(self.HEALTH, self.attacker.health)
        self.assertEqual(self.DAMAGE, self.attacker.damage)

    def test_battle_raises_when_both_are_with_the_same_names(self):
        enemy = Hero(self.ATTACKER_USERNAME, 5, 10, 20)

        with self.assertRaises(Exception) as error:
            self.attacker.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle_raises_when_attacker_health_is_equal_to_zero(self):
        enemy = Hero("Enemy", 5, 10, 20)
        self.attacker.health = 0

        with self.assertRaises(ValueError) as error:
            self.attacker.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle_raises_when_enemy_health_is_equal_to_zero(self):
        enemy_username = "Enemy"
        enemy = Hero(enemy_username, 5, 0, 20)

        with self.assertRaises(ValueError) as error:
            self.attacker.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy_username}. He needs to rest", str(error.exception))

    def test_battle_returns_draw_when_both_heroes_are_dead(self):
        enemy = Hero("Enemy", self.LEVEL, self.HEALTH, self.DAMAGE)

        result = self.attacker.battle(enemy)
        expected_health = self.HEALTH - (self.LEVEL * self.DAMAGE)

        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_returns_win_when_enemy_dies(self):
        enemy_level, enemy_health, enemy_damage = 5, 80, 10
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = self.attacker.battle(enemy)
        enemy_expected_health = enemy_health - (self.LEVEL * self.DAMAGE)
        attacker_expected_level = self.LEVEL + self.BATTLE_LEVEL_INCREMENT
        attacker_expected_damage = self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        attacker_expected_health = self.HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You win", result)
        self.assertEqual(enemy_expected_health, enemy.health)
        self.assertEqual(attacker_expected_level, self.attacker.level)
        self.assertEqual(attacker_expected_damage, self.attacker.damage)
        self.assertEqual(attacker_expected_health, self.attacker.health)

    def test_battle_returns_win_when_attacker_dies(self):
        attacker_level, attacker_health, attacker_damage = 5, 80, 10
        attacker = Hero(self.ATTACKER_USERNAME, attacker_level, attacker_health, attacker_damage)

        enemy = Hero("Enemy", self.LEVEL, self.HEALTH, self.DAMAGE)

        result = attacker.battle(enemy)
        attacker_expected_health = attacker_health - (self.LEVEL * self.DAMAGE)
        enemy_expected_level = self.LEVEL + self.BATTLE_LEVEL_INCREMENT
        enemy_expected_damage = self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        enemy_expected_health = self.HEALTH - (attacker_level * attacker_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You lose", result)
        self.assertEqual(attacker_expected_health, attacker.health)
        self.assertEqual(enemy_expected_level, enemy.level)
        self.assertEqual(enemy_expected_damage, enemy.damage)
        self.assertEqual(enemy_expected_health, enemy.health)

    def test_hero_str_returns_proper_message(self):
        actual_result = str(self.attacker)
        expected_result = f"Hero {self.ATTACKER_USERNAME}: {self.LEVEL} lvl\n" \
                          f"Health: {self.HEALTH}\n" \
                          f"Damage: {self.DAMAGE}\n"

        self.assertEqual(expected_result, actual_result)
