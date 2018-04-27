
class GoodreadsBook:
    def __init__(self, book_elem_xml, book_id='', book_title='',
                 book_authors=None, book_owned_id=''):
        self._book_elem_xml = book_elem_xml
        self._id = book_id
        self._title = book_title
        self._authors = book_authors
        self.owned_id = book_owned_id

    @property
    def book_elem_xml(self):
        return self._book_elem_xml

    @property
    def id(self):
        if self._id == '':
            self._id = self._set_book_info('id')
        return self._id

    @property
    def title(self):
        if self._title == '':
            self._title = self._set_book_info('title')
        return self._title

    def _set_book_info(self, info):
        book_info_xml = self.book_elem_xml.getElementsByTagName(info)[0]
        book_info = book_info_xml.firstChild.nodeValue
        return book_info

    @property
    def authors(self):
        if self._authors is None:
            self._set_book_authors()
        return self._authors

    def _set_book_authors(self):
        book_authors = []
        authors_section = self.book_elem_xml.getElementsByTagName('authors')
        for author in authors_section:
            author_elem_xml = author.getElementsByTagName('author')[0]
            author_name_xml = author_elem_xml.getElementsByTagName('name')[0]
            author_name = author_name_xml.firstChild.nodeValue
            book_authors.append(author_name)
        self._authors = book_authors
