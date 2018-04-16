
class GoodreadsBook:
    def __init__(self, book_elem_xml):
        self.book_elem_xml = book_elem_xml
        self.id = ''
        self.title = ''
        self.owned_id = ''
        self.authors = []

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

    def get_book_authors(self):
        book_authors = []
        authors_section = self.book_elem_xml.getElementsByTagName('authors')
        for author in authors_section:
            author_elem_xml = author.getElementsByTagName('author')[0]
            author_name_xml = author_elem_xml.getElementsByTagName('name')[0]
            author_name = author_name_xml.firstChild.nodeValue
            book_authors.append(author_name)
        return book_authors
