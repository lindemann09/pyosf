from __future__ import absolute_import
import os
import logging
from . import constants

# create a logfile for this session
logfile_path = os.path.join(constants.PYOSF_FOLDER, 'last_session.log')
if not os.path.isdir(constants.PYOSF_FOLDER):
    os.makedirs(constants.PYOSF_FOLDER)

# default logging
logfile = logging.FileHandler(logfile_path, mode='w')
info = logging.info
warn = logging.warning
debug = logging.debug
flush = None

def set_psychopy_logging():
    """Using Psychopy logging.

    Call this function to use the Psychopy.logging module instead of
    logging from The Python Standard Library.
    """

    global logfile, info, warn, debug, flush
    from psychopy import logging as psychopy_log
    logfile = psychopy_log.LogFile(logfile_path, level=logging.DEBUG)
    info = psychopy_log.info
    warn = psychopy_log.warning
    debug = psychopy_log.debug
    flush = psychopy_log.flush