from custom_classes import MediaItem, Book, DVD, LibraryCollection   # Imports classes from custom_classes.py

library = LibraryCollection()   # Creates a library collection object

book1 = Book("Her Temas Iz Birakir", "Emrah Serbes", "320")   # Creates the first book object
book2 = Book("Dogu Ekspresinde Cinayet", "Agatha Christie", "234")   # Creates the second book object
dvd1 = DVD("GORA", "Cem Yilmaz", "127")   # Creates the first DVD object
dvd2 = DVD("AROG", "Cem Yilmaz", "115")   # Creates the second DVD object

library.add_item(book1)   # Adds the first book to the library
library.add_item(book2)   # Adds the second book to the library
library.add_item(dvd1)   # Adds the first DVD to the library
library.add_item(dvd2)   # Adds the second DVD to the library

print(book1)   # Prints the information of book1
print(book2)   # Prints the information of book2
print(dvd1)   # Prints the information of dvd1
print(dvd2)   # Prints the information of dvd2

print(library.list_available())   # Prints the list of available item titles

dvd1.checkout()   # Checks out the first DVD
book2.checkout()   # Checks out the second book

print(library.list_available())   # Prints the list of available item titles

print(book1)   # Prints the information of book1
print(book2)   # Prints the information of book2
print(dvd1)   # Prints the information of dvd1
print(dvd2)   # Prints the information of dvd2