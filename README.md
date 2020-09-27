# BBB_calculator

Implements the blood brain barrier score described in the following paper

J. Med. Chem. 2019, 62, 21, 9824-9836

<https://doi.org/10.1021/acs.jmedchem.9b01220>

## Install

```shell
pip install BBB_calculator
```

## Use

```python
from BBB_calculator import BBB_score

score = BBB_score(1, 20, 300.29, 1, 7, 122.46, 2.86)
print(score)
# Prints: 1.815645...
```

For more detailed documentation, see: https://frequencykg.github.io/BBB_calculator/

## Publish

To publish a new version of this package:

```shell
python setup.py sdist

# Install sphinx with: pip install -U sphinx
make html

# Install twine with: pip install twine
twine upload dist/*
```
