import pytest

def test_easy():
  x = 1
  assert x == 1

import deathadder
def test_deathadder():
  assert deathadder.deathadder(1,2) == 669
  assert deathadder.deathadder(333,1) == 1000

import greeting