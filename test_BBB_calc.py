import pytest
from BBB_calculator.BBB_score import aro_r_term
from BBB_calculator.BBB_score import ha_term
from BBB_calculator.BBB_score import mwhbn_term
from BBB_calculator.BBB_score import tpsa_term
from BBB_calculator.BBB_score import pka_term
from BBB_calculator import BBB_score


def test_aro_r_term():
    assert aro_r_term(2) == 1


def test_ha_term():
    assert ha_term(10) == pytest.approx(0.645914, 0.001)


def test_mwhbn_term():
    assert mwhbn_term(200, 2, 2) == pytest.approx(0.888784, 0.001)


def test_tpsa_term():
    assert tpsa_term(130) == 0


def test_pka_term():
    assert pka_term(2) == 0


def test_bbb_score():
    assert BBB_score(1, 20, 300.29, 1, 7, 122.46, 2.86) == pytest.approx(1.815645, 0.001)
