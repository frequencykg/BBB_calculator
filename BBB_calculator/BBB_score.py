"""Provides a BBB score calculator.

See: BBB_score.
"""


def aro_r_term(aro_r):
    if aro_r == 0:
        return 0.336376
    elif aro_r == 1:
        return 0.816016
    elif aro_r == 2:
        return 1
    elif aro_r == 3:
        return 0.691115
    elif aro_r == 4:
        return 0.199399
    elif aro_r > 4:
        return 0
    else:
        raise ValueError('invalid aro_r input number')


def ha_term(ha):
    if ha > 5 and ha <= 45:
        return 1/0.624231*(0.0000443*ha**3 - 0.004556*ha**2 + 0.12775*ha - 0.463)
    elif ha <= 5 or ha > 45:
        return 0
    else:
        raise ValueError('invalid ha number')


def mwhbn_term(mw, hbd, hba):
    if mw <= 0:
        raise ValueError('invalid mw number')
    if hbd < 0:
        raise ValueError('invalid hbd number')
    if hba < 0:
        raise ValueError('invalid hba number')
    mwhbn = (hbd + hba)/mw**0.5
    if 0.05 <= mwhbn and mwhbn < 0.45:
        return 1/0.72258*(26.733*mwhbn**3 - 31.495*mwhbn**2 + 9.5202*mwhbn - 0.1358)
    elif mwhbn <= 0.05 or mwhbn > 0.45:
        return 0
    else: 
        raise ValueError('invalid mwhbn number')


def tpsa_term(tpsa):
    if tpsa > 0 and tpsa <= 120:
        return 1/0.9598*(-0.0067*tpsa + 0.9598)
    elif tpsa == 0 or tpsa > 120:
        return 0
    else:
        raise ValueError('invalid tpsa number')


def pka_term(pka):
    if pka > 3 and pka < 11:
        return 1/0.597488*(0.00045068*pka**4 - 0.0116331*pka**3 + 0.18618*pka**2 - 0.71043*pka + 0.8579)
    elif pka <= 3 or pka > 11:
        return 0
    else:
        raise ValueError('invalif pka number')


def BBB_score(aro_r, ha, mw, hbd, hba, tpsa, pka):
    """BBB_score does the calculation from the gupta 2019 J Med Chem paper.

    Args:
        aro_r (int): The number of aromatic rings.
        ha (int):  number of heavy atoms.
        mw (float): molecular weight.
        hbd (int): number of hydrogen bond donors.
        hba (int): number of hydrogen bond acceptora.
        tpsa (float): total polar surface area.
        pka (float): pKa value.
    
    Returns:
        float: The bbb score.

    .. J. Med. Chem. 2019, 62, 21, 9824-9836:
        https://doi.org/10.1021/acs.jmedchem.9b01220
    """
    aro_r_term_value = aro_r_term(aro_r)
    ha_term_value = ha_term(ha)
    mwhbn_term_value = mwhbn_term(mw, hbd, hba)
    tpsa_term_value = tpsa_term(tpsa)
    pka_term_value = pka_term(pka)
    return aro_r_term_value + ha_term_value + 1.5*mwhbn_term_value + 2*tpsa_term_value + 0.5*pka_term_value
