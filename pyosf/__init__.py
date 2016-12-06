__version__ = '1.0.4'
__license__ = 'MIT'
__author__ = 'Jonathan Peirce'
__author_email__ = 'jon@peirce.org.uk'
__maintainer_email__ = 'jon@peirce.org.uk'
__url__ = 'https://github.com/psychopy/pyosf'
__downloadUrl__ = 'https://github.com/psychopy/pyosf/releases/'

from . import constants
from .remote import Session, TokenStorage
from .exceptions import AuthError, HTTPSError, OSFError, OSFDeleted
from .project import Project
from .logging import logfile, set_psychopy_logging