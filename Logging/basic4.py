import logging

# Default ROOT logger in python
logging.basicConfig(level = logging.DEBUG,filename='basic4.log', filemode='a',\
format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

name = 'John'
logging.error(f'{name} raised an error')

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info =True)
