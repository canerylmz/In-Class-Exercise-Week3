from custom_classes import MediaItem, Book, DVD, LibraryCollection

library = LibraryCollection()

book1 = Book("Her Temas Iz Birakir", "Emrah Serbes", "320")
book2 = Book("Dogu Ekspresinde Cinayet", "Agatha Christie", "234")
dvd1 = DVD("GORA", "Cem Yilmaz", "127")
dvd2 = DVD("AROG", "Cem Yilmaz", "115")

library.add_item(book1)
library.add_item(book2)
library.add_item(dvd1)
library.add_item(dvd2)

print(book1)
print(book2)
print(dvd1)
print(dvd2)

print(library.list_available())

dvd1.checkout()
book2.checkout()

print(library.list_available())

print(book1)
print(book2)
print(dvd1)
print(dvd2)