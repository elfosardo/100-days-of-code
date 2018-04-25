
class GoodreadsBook:
    def __init__(self, book_elem_xml, book_id='', book_title='',
                 book_owned_id='', book_authors=None):
        self._book_elem_xml = book_elem_xml
        self.id = book_id
        self.title = book_title
        self.owned_id = book_owned_id
        self._authors = book_authors

    @property
    def book_elem_xml(self):
        return self._book_elem_xml

    def get_book_id(self):
        book_id = self.get_book_info('id')
        return book_id

    def get_book_title(self):
        book_title = self.get_book_info('title')
        return book_title

    def get_book_info(self, info):
        book_info_xml = self.book_elem_xml.getElementsByTagName(info)[0]
        book_info = book_info_xml.firstChild.nodeValue
        return book_info

    @property
    def authors(self):
        if self._authors is None:
            self.set_book_authors()
        return self._authors

    def set_book_authors(self):
        book_authors = []
        authors_section = self.book_elem_xml.getElementsByTagName('authors')
        for author in authors_section:
            author_elem_xml = author.getElementsByTagName('author')[0]
            author_name_xml = author_elem_xml.getElementsByTagName('name')[0]
            author_name = author_name_xml.firstChild.nodeValue
            book_authors.append(author_name)
        self._authors = book_authors
