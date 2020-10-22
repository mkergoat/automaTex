titlepagetemplate = (r"""
\begin{titlepage}
\begin{center}

\vfill
{\Large \bfseries ${title}}

${author}

${date}
\vfill 
\end{center}
\end{titlepage}
""")

class LaTeXReport:
    def __init__(self, filename, title, author, date, sty=None, custom_commands=None):
        """
        Constructor
        """
        self._filename = filename
        self.title = title
        self._author = author
        self._date = date
        if sty = None:
            style = 'plain'
        else:
            style = sty
        self.titlepage = ''
        if custom_commands=None:
            custom = ''
        else:
            custom = custom_commands

    def titlepage(self):
        """
        Creates the titlepage of the document
        """
        elements = {'title': self.title, 'author': self.author, 
        titlepage = titlepagetemplate.safesubstitute(elements)
        return titlepage

class LaTeXSectionning:
    """
    This class represents a level of sectionning in LaTeX
    """
    def __init__(level, text, label):
        self._level = level
        self._label = label
        self.text = text
    
    def write(self):
        levelstr = r'\ ' + self._level + r'{'+ self.text + r'}' + r'\\' + r'\label{' + self._label + r'}'
        return levelstr.replace(' ', '')
    
    def insert_sectionning(self, elements):
    elements.append(self.write())

class LaTeXFloat:
    """
    This class representents any kind of float (table, figure)
    """
    def __init__(self, type, caption, label, positionning):
        self._type = _type
        self._caption = caption
        self._label = label
        self.pos = positionning
        
    def insert_float(self, elements):
        """
        Adds the float to the list of elements in the document
        """
        elements.append(self.write())

class LaTeXFigure(LaTeXFloat):
    def __init__(self, type, caption, label, positionning, figure_filename, scalefactor, cropfactors=['', '']):
        LaTeXFloat.__init__(self, type, caption, label, positionning)
        self.scale = scalefactor
        self._cropx = cropfactors[0]
        self._cropy = cropfactors[1]
        self._filename = figure_filename
        
class LaTeXTable(LaTeXFloat):

