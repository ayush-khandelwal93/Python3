# this program outputs all logging statement direct to console 
# after running it.

import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

logger.info('Start Reading database')
records = {'john':55, 'tom':66}

logger.info('Records: %s' , records)

logger.debug('Records: ' + str(records))

logger.info('Finish reading database')

#output
#INFO:__main__:Start Reading database
#INFO:__main__:Records: {'john': 55, 'tom': 66}
#INFO:__main__:Finish reading database

#Does not output the debug statement as logger level is INFO
