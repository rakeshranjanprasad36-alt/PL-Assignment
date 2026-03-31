class Book:
    def __init__(self, title, writer, is_available=True):
        self.title = title
        self.writer = writer
        self.is_available = is_available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' by '{self.writer}' has been checked out.")
        else:
            print(f"Sorry, '{self.title}' is currently not available.")

    def give_back(self):
        if not self.is_available:
            self.is_available = True
            print(f"Book '{self.title}' has been returned and is now available.")
        else:
            print(f"Book '{self.title}' was not checked out.")

    def show_info(self):
        current_status = "Available" if self.is_available else "Checked Out"
        print(f"Book: {self.title}, Author: {self.writer}, Status: {current_status}")


b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("To Kill a Mockingbird", "Harper Lee")
b3 = Book("1984", "George Orwell", False)

b1.show_info()
b2.show_info()
b3.show_info()

print("\nChecking out books...")
b1.borrow()
b2.borrow()
b3.borrow()

print("\nReturning books...")
b1.give_back()
b3.give_back()

print("\nFinal book statuses:")
b1.show_info()
b2.show_info()
b3.show_info()