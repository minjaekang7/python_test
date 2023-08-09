from logging import getLogger, StreamHandler, DEBUG, WARN, INFO, ERROR, CRITICAL, Formatter, FileHandler
import datetime
import os

logFolder = 'log'

formatter = Formatter('[%(asctime)s %(levelname)s %(filename)s] %(message)s')
handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(formatter)

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
logname = now.strftime('RSI_%Y%m%d_%H%M%S.log')

logpath = os.path.join(logFolder, logname)
fhandler = FileHandler(logpath)
fhandler.setLevel(INFO)
fhandler.setFormatter(formatter)

logger = getLogger(__name__)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.addHandler(fhandler)

# DEBUG < WARN < INFO < ERROR < CRITICAL

logger.warn('This is warn')
logger.info('This is info')

fnames = sorted(os.listdir(logFolder), reverse=True)
logger.info(f'fnames in log folder:{fnames}')
for fname in fnames[3:]:
    fpath = os.path.join(logFolder, fname)
    try:
        logger.info(f'{fpath} is removed')
        os.remove(fpath)
    except:
        pass
