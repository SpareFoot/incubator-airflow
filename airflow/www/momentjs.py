from jinja2 import Markup


class momentjs(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp

    def _render(self, format):
        return Markup("<script>\ndocument.write(moment(\"%s\").%s);\n</script>" % (self.timestamp.strftime("%Y-%m-%dT%H:%M:%S Z"), format))

    def format(self, fmt=''):
        if fmt:
            return self._render("format('{}')".format(fmt))
        return self._render("format()")

    def calendar(self):
        return self._render("calendar()")

    def fromNow(self):
        return self._render("fromNow()")
