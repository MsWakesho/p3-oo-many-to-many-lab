class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)


class Author:
    def __init__(self, name):
        self.name = name
        self.contracts_list = []

    def contracts(self):
        return self.contracts_list

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Contract must be associated with an Author object")
        if not isinstance(book, Book):
            raise Exception("Contract must be associated with a Book object")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
