"""This module is a library management system."""
import datetime
from uuid import uuid4


class Library:
    """This is a class for library features."""

    def __init__(self, name, address):
        """This is the library class constructor."""
        self.name = name
        self.address = address
        self.book_count = 0
        self.book_list = []

    def greetings(self):
        """This will print a welcome message on screen."""
        print(f"Welcome to {self.name} library.")

    def add_book(self, name, isbn):
        """This will add a new book to the library"""
        if name not in self.book_list:
            new_book = {
                'book_id': uuid4(),
                'name': name,
                'title': "Tales by Moon Light",
                'ISBN': isbn
            }
        self.book_list.append(new_book)

    def lease_book(self, book):
        """This will reduce book count by a user specified number"""
        self.book_count -= book

    def return_book(self, book):
        """This will increase book count by a user specified number"""
        self.book_count += book

    def get_name(self):
        """This will display the name of the library"""
        return self.name

    def remove_book(self, book):
        """This will remove a specific book if it exists in the library"""
        if book in self.book_list:
            self.book_list.remove(book)
        else:
            print("Sorry, we don't have such a book.")
        print(f"{book} removed successfully.")
    
    def display_shelf(self):
        """This will display all books in the library"""
        return self.book_list

    def update(self, book_id):
        """This will effect an update to specific profiles of the book"""
        pass
