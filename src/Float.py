from abc import abstractmethod, ABCMeta
from string import Template

env = Template(r"""
        \begin{${kind}}
        \centering
            ${float}
        \caption{${caption}}
        \label{${label}}
        \end{${kind}}
        """)


class LaTeXFloat(metaclass=ABCMeta):
    """
    This class representents any kind of float (table, figure)
    """

    def __init__(self, kind, caption, label, positionning):
        self._kind = kind
        self._caption = caption
        self._label = label
        self.pos = positionning

    def set__kind(self, kind):
        """
        Setter
        """
        if isinstance(kind, str):
            self._kind = kind
        else:
            raise TypeError

    def get_kind(self):
        """
        Getter
        """
        return self._kind

    @abstractmethod
    def write_float(self):
        pass

    def insert_float(self, document):
        """
        Adds the float to the list of elements in the document
        """
        setup = {'kind': self._kind, 'caption': self._caption, 'label': self._label, 'float': self.write_float()}
        document.append(env.safe_substitute(setup))


class LaTeXFigure(LaTeXFloat):
    """
    This class specifically represents a figure (image, tikzfigure...)
    """

    def __init__(self, kind, caption, label, positionning, figure_filename, scalefactor, cropfactors=['', '']):
        """
        Constructor of subclass
        """
        LaTeXFloat.__init__(self, kind, caption, label, positionning)
        self.scale = scalefactor
        self._cropx = cropfactors[0]
        self._cropy = cropfactors[1]
        self._filename = figure_filename

    def get__filename(self):
        """
        Getter
        """
        return self._filename

    def write_float(self):
        """
        Writes the figure environment
        """
        file = self.get__filename()
        figure = r"\includegraphics[scale={0}]{{1}}".format(self.scale, file)
        return figure

class LaTeXTable(LaTeXFloat):
    """
    This class specifically represents a table.
    """

    tab_env = Template(r"""
    \begin{tabular}{${align}
    ${table}
    \end{tabular}
    """)

    def __init__(self, kind, caption, label, positionning, style, file=None, column_alignements='c'):
        """
        Constructor of subclass
        """
        LaTeXFloat.__init__(self, kind, caption, label, positionning)
        self.style = style
        self._file = file
        self.column_alignement = column_alignements
        self.lines = []

    def add_line_to_table(self, line, colsep=','):
        """
        Transforms a line into a str with '&' between columns
        """
        self.lines.append('&'.join(line.split(colsep)))

    def fit_to_table_style(self):
        """
        Formats the list of lines in order to conform to the chosen style
        """
        if self.style == 'standard':
            for line in self.lines:
                line += r' \hline'
        elif self.style == 'booktabs':
            self.lines = [r'\toprule'] + [self.lines[0]] + [r'\midrule'] + self.lines[1:] + ['r\bottomrule']
        else:
            print('Style unavailable in this version of automaTeX')

    def table_from_file(self, file):
        """
        Table automatically generated from a file
        """
        f = open(file, 'r')
        header = f.readline()
        number_of_columns = len(header)
        self.add_line_to_table(header)
        for line in f.readlines():
            self.add_line_to_table(line)
        if len(self.column_alignement) == 1:
            self.column_alignement = number_of_columns * self.column_alignement
        else:
            pass

    def write_float(self):
        """
        Writes the table environment
        """

