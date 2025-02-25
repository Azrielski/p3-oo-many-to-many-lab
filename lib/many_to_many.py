class Author:
    all = []
    def __init__(self, name):
        self._name = None
        self.name = name
        Author.all.append(self)

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not  value.strip():
            raise Exception("Name must be a non empty string")
        self._name = value.strip()
        
    def contracts(self):
        #returns a list of contract objects related to this aurthor
        return[contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        #returns a list of book objects related to this aurthor, excluding duplicates
        return list(set(contract.book for contract in self.contracts()))
    
    def sign_contract(self, book, date, royalties):
        #signs a new contract for the given book, date, and royalties
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    
    def __repr__(self):
        return f"Author({self.name})"
        
    


class Book:
    all = []
    
    def __init__(self, title):
        self._title = None
        self.title = title
        Book.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value.strip()
    
    def contracts(self):
        """Returns a list of contracts related to this book."""
        return [contract for contract in Contract.all if contract._book == self]
    
    def authors(self):
        """Returns a list of unique authors who have contracts for this book."""
        return list(set(contract._author for contract in self.contracts()))


    


class Contract:
    all = [] 
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author class")
            
        if not isinstance(book, Book):
            raise ValueError("book must be an instance of Book class")
        
        if not isinstance(date, str):
            raise ValueError("date must be a string")
        
        if not isinstance(royalties, int) or royalties < 0:
            raise ValueError("royalties must be a non-negative integer")
        
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        
        Contract.all.append(self) 
    
    # Property getters to access private attributes
    @property
    def author(self):
        return self._author
    
    @property
    def book(self):
        return self._book
    
    @property
    def date(self):
        return self._date
    
    @property
    def royalties(self):
        return self._royalties
    
    # Class method to find contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
    # String representation of the Contract object
    def __repr__(self):
        return f"Contract({self.author.name}, {self.book.title}, {self.date}, {self.royalties})"

        
        
        
        