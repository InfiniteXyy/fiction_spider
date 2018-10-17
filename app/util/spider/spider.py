from abc import abstractmethod


class Spider:
    book_name = ""
    book_url = ""

    @classmethod
    @abstractmethod
    def get_article_list(cls):
        pass

    @classmethod
    @abstractmethod
    def get_content(cls, url):
        pass
