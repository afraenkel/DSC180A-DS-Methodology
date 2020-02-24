
from dependency import return_hello

import logging

# logging.basicConfig(level=logging.INFO)

logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log', 
    filemode='w', 
    format='%(name)s - %(levelname)s - %(message)s'
)


def test():

    logging.debug('calling return_hello')

    return return_hello()


if __name__ == '__main__':
    
    test()
