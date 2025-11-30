from random import randint
from classes import Player, Enemy
import pytest


def test_heal():
    p = Player("test",100,1,0.7,"Pinne",0)
    p.dmg_verden(20)
    assert p.liv_igjenn() == 80
