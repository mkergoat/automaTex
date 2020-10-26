from string import Template

titlepagetemplate = Template("""Ce rapport a été généré automatiquement par automaTex""")


class LaTeXReport:
    def __init__(self, filename, title, author, date, sty=None):
        """
        Constructor
        """
        self._filename = filename
        self.title = title
        self._author = author
        self._date = date
        if sty is None:
            style = 'plain'
        else:
            style = sty
        self.titlepage = ''
        self.elements = []

    def title_page(self):
        """
        Creates the titlepage of the document
        """
        elements = {'title': self.title, 'author': self._author, 'date': self._date}
        self.titlepage = titlepagetemplate.safe_substitute(elements)

    def report_from_ctr(self, ctr_file):
        ctr
