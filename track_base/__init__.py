from track_base.active_applications import active_applications

from track_base.time_tracker import time_tracker
from track_base.rules_model import rules_model

from track_base.track_common import mins_to_dur
from track_base.track_common import mins_to_date
from track_base.track_common import secs_to_dur
from track_base.track_common import today_int
from track_base.track_common import minute
from track_base.track_common import app_info

from collections import namedtuple

version_info = namedtuple('version_info', ['major', 'minor', 'micro', 'patch'])

version_info = version_info(major=2015, minor=9, micro=27, patch=1)


