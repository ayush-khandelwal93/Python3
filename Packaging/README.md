-Folder structure earlier was:

├── print_helpers
│   ├── bprint.py
│   ├── __init__.py
│   └── sprint.py
└── setup.py

-Then run
python3 setup.py bdist_wheel

This will form the present directory structure 

Use .whl to do pip install
pip install ./print_helpers-0.1-py3-none-any.whl

Ref:
https://hackernoon.com/pip-install-abra-cadabra-or-python-packages-for-beginners-33a989834975
