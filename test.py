import unittest
from jugador import Player

class TestPlayer(unittest.TestCase):
    def test1(self):
        p = Player(1, 'a')
        self.assertEqual(p.getEnergy(), 50)

    def test2(self):
        p = Player(1, 'a')
        p.boost(-100)
        self.assertEqual(p.getEnergy(), 0)

    def test3(self):
        p = Player(1, 'a')
        p.boost(200)
        self.assertEqual(p.getEnergy(), 100)