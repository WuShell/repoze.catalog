
from builtins import object
class RangeValue(object):
    """ Use in fieldindex query above to indicate a range search for a term """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def as_tuple(self):
        return (self.start, self.end)

Range = RangeValue # deprecated BBB
