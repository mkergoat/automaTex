class LaTeXSectionning:
    """
    This class represents a level of sectionning in LaTeX
    """

    def __init__(self, level, text, label):
        self._level = level
        self._label = label
        self.text = text

    def write(self):
        levelstr = r'\ ' + self._level + r'{' + self.text + r'}' + r'\\' + r'\label{' + self._label + r'}'
        return levelstr.replace(' ', '')

    def insert_sectionning(self, elements):
        elements.append(self.write())
