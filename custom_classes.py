class MediaItem:   # Base class for library items
    def __init__(self,title,author,is_available=True):   # Constructor method
        self.title = title   # Stores the title
        self.author = author   # Stores the author
        self.is_available = is_available   # Stores availability
    
    def checkout(self):   # Method for borrowing the item
        if self.is_available:   # Checks if the item is available
            self.is_available = False   # Marks the item as checked out
            print("Successfull checkout\n")   # Prints success message
        else:   # If the item is not available
            print("Already out\n")   # Prints warning message

    def return_item(self):   # Method for returning the item
        self.is_available = True   # Marks the item as available
        print("Item returned\n")   # Prints return message

    def __str__(self):   # String representation of the object
        if self.is_available:   # Checks availability
            status = "Available"   # Sets status as Available
        else:   # If not available
            status = "Checked out"   # Sets status as Checked out
        
        return self.title + " by " + self.author + " [" + status + "]"   # Returns item info

class Book(MediaItem):   # Subclass for books
    def __init__(self,title,author,page_count,is_available=True):   # Constructor for Book
        self.title = title   # Stores the book title
        self.author = author   # Stores the book author
        self.is_available = is_available   # Stores availability status
        self.page_count = page_count   # Stores the number of pages
    
    def __str__(self):   # String representation of Book
        if self.is_available:   # Checks availability
            status = "Available"   # Sets status as Available
        else:   # If not available
            status = "Checked out"   # Sets status as Checked out
        
        return self.title + " by " + self.author + " " + self.page_count + " pages [" + status + "]"   # Returns book info

class DVD(MediaItem):   # Subclass for DVDs
    def __init__(self,title,author,duration,is_available=True):   # Constructor for DVD
        super().__init__(title,author,is_available)   # Calls parent constructor
        self.duration = duration   # Stores the DVD duration
    
    def checkout(self):   # Overrides checkout method
        print("\nHandle with care: Do not scratch the disc.")   # Prints warning message
        return super().checkout()   # Calls parent checkout method
    
    def __str__(self):   # String representation of DVD
        if self.is_available:   # Checks availability
            status = "Available"   # Sets status as Available
        else:   # If not available
            status = "Checked out"   # Sets status as Checked out

        return self.title + " by " + self.author + " " + self.duration + " minutes [" + status + "]"   # Returns DVD info
    
class LibraryCollection:   # Class for storing multiple items
    def __init__(self):   # Constructor method
        self.items = []   # Creates an empty list for items
    
    def add_item(self,item):   # Method to add an item
        self.items.append(item)   # Appends the item to the list
    
    def list_available(self):   # Method to list available items
        available_items = []   # Creates an empty list for available titles
        for item in self.items:   # Loops through all items
            if item.is_available:   # Checks if the item is available
                available_items.append(item.title)   # Adds the title to the list
        return available_items   # Returns the list of available titles