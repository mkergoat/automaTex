from String import Template

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
        if sty == None:
            style = 'plain'
        else:
            style = sty
        self.titlepage = ''
        if custom_commands == None:
            custom = ''
        else:
            custom = custom_commands

    def titlepage(self):
        """
        Creates the titlepage of the document
        """
        elements = {'title': self.title, 'author': self.author, 
        titlepage = titlepagetemplate.safe_substitute(elements)
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
    def __init__(self, kind, caption, label, positionning):
        self._kind = kind
        self._caption = caption
        self._label = label
        self.pos = positionning
        
    def insert_float(self, elements):
        """
        Adds the float to the list of elements in the document
        """
        elements.append(self.write())
                    
    def prepare_env(self):
        """
        Generates a template for the float environnement
        """
        env = Template(r"""
            \begin{${kind}}
            \centering
                ${float}
            \caption{${caption}}
            \label{${label}}
            \end{${kind}}
            """)
        return env

                    
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
   
                    
class LaTeXTable(LaTeXFloat):
    """
    This class specifically represents a table.
    """
    def __init__(self, kind, caption, label, positionning, style, file=None, column_alignements='c'):
        """
        Constructor of subclass
        """
        LaTexFloat.__init__(self, kind, caption, label, positionning)
        self.style = style
        self._file = file
        self.column_alignement = colum_alignments
        self.lines = []
          
    def prepare_tabular(self):
        tab_env = Template("""
        \begin{tabular}{${align}
        ${table}
        \end{tabular}
        """)
        return tab_env
                    
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
                    
    def table_from_file(self):
         """
         Table automatically generated from a file
         """
         f = open(file, 'r')
         header = f.readline()
         number_of_columns = len(header)
         self.add_line_to_table(header)
         for line in f.readlines():
             self.add_line_to_table(line)
         if len(self.column_alignements) == 1:
            self.column_alignement = number_of_columns * self.column_alignement
          else:
              pass
          env = self.prepare_env
          tabular_env = self.prepare_tabular
