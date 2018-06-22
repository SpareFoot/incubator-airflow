from datetime import datetime
from jinja2 import Markup
import pendulum
import six
from airflow.utils.timezone import utc

class momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp
        if not isinstance(timestamp, pendulum.Pendulum):
            if isinstance(timestamp, datetime):
                self.timestamp = pendulum.instance(timestamp)
            elif isinstance(timestamp, six.string_types):
                self.timestamp = pendulum.parse(timestamp)

    def _render(self, format):
        if not self.timestamp:
            return None
        return Markup("<script>document.write(\"<span class='localtime' title='localized time from %s UTC'>\" + dateFns.format(dateFns.parse('%s'), '%s') + \"</span>\" );</script>" % (self.timestamp.in_tz(utc).to_iso8601_string(), self.timestamp.to_iso8601_string(), format))

    def format(self, fmt=''):
        return self._render(fmt)

