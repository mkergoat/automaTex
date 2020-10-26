from collections import OrderedDict


class ControlFile:
    def __init__(self, file):
        self._filename = file
        self.contents = OrderedDict()

    def from_ctr(self, file):
        file = open(file, 'r')
        flines = file.readlines()
        for line in flines:
            if line[:11] == ':Sectionning':
                self.contents[line[1:]] = {}



