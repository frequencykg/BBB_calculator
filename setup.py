from distutils.core import setup
setup(
  name = 'BBB_calculator',
  packages = ['BBB_calculator'],
  version = '1.0',
  license='MIT',
  description = 'Implements the blood brain barrier score described in: J. Med. Chem. 2019, 62, 21, 9824-9836',
  author = 'Keira Garland',
  author_email = 'keiragarland@gmail.com',
  url = 'https://github.com/frequencykg/BBB_calculator',
  download_url = 'https://github.com/frequencykg/BBB_calculator/archive/v1.0.tar.gz',
  keywords = ['BBB', 'brain', 'medchem', 'calculator'],
  install_requires=[],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
