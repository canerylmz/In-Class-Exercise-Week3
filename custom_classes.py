class MediaItem:
    def __init__(self,title,author,is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available
    
    def checkout(self):
        if self.is_available:
            self.is_available = False
            print("Successfull checkout\n")
        else:
            print("Already out\n")

    def return_item(self):
        self.is_available = True
        print("Item returned\n")

    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Checked out"
        
        return self.title + " by " + self.author + " [" + status + "]"

class Book(MediaItem):
    def __init__(self,title,author,page_count,is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available
        self.page_count = page_count
    
    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Checked out"
        
        return self.title + " by " + self.author + " " + self.page_count + " pages [" + status + "]"

class DVD(MediaItem):
    def __init__(self,title,author,duration,is_available=True):
        super().__init__(title,author,is_available)
        self.duration = duration
    
    def checkout(self):
        print("\nHandle with care: Do not scratch the disc.")
        return super().checkout()
    
    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Checked out"

        return self.title + " by " + self.author + " " + self.duration + " minutes [" + status + "]"
    
class LibraryCollection:
    def __init__(self):
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)
    
    def list_available(self):
        available_items = []
        for item in self.items:
            if item.is_available:
                available_items.append(item.title)
        return available_items