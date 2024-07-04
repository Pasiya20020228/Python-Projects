#Available Resources

#Books
book1 = {
    "id" : "001",
    "title" : "Maya Dupatha",
    "format" : "hardcover",
    "subject" : "Story",
    "rental_price" : 20,
    "num_copies" : 4,
    "available_copies" : 4
}

book2 = {
    "id" : "001",
    "title" : "Maya Dupatha",
    "format" : "hardcover",
    "subject" : "Story",
    "rental_price" : 20,
    "num_copies" : 4,
    "available_copies" : 4
}

book3 = {
    "id" : "001",
    "title" : "Maya Dupatha",
    "format" : "hardcover",
    "subject" : "Story",
    "rental_price" : 20,
    "num_copies" : 4,
    "avaliable_copies" : 4
}

#Functions
def menu():
    print("Menu...")
    print("1.Add a new resource")
    print("2.Remove a resource")
    print("3.View available resources")
    print("4.View unavailable resources")
    print("5.View all resources")
    print("6.Lend a resource")
    print("7.Update resource")

def types_menu():
    print("What do you need to add:")
    print("1.Books")
    print("2.Magazines")
    print("3.Cds")
    print("4.Dvds")

#class
class Library:
    def books(self,id,title,format,subject,rental_price,num_copies,avalible_copies):
        self.id = id
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price = int(rental_price)
        self.num_copies = int(num_copies)
        self.avalible_copies = int(avalible_copies)

    def magazines(self,):
        pass







#Main Process Here
print("Welcome to Library System..")
print("System Online..")
print("Do you need to go Menu?")
if (input("Type 'y' to yes or 'n' to No:- ") == 'y'):
    menu()
    if (input("Type Option Number to Run :- ") == '1'):
        types_menu()
        if (input("Type do you need Option Number :- ") == '1'):
            book1 = Library()
            book1.id = input("Enter Book ID: ")
            book1.title = input("Enter Book Title: ")
            book1.format = input("Enter Book Format: ")
            book1.subject = input("Enter Book Subject: ")
            book1.rental_price = input("Enter Book Rental Price: ")
            book1.num_copies = input("Enter Number of Books: ")
            book1.avalible_copies = book1.num_copies
            print("Added Suscessfully!!")




else:
    print("Going System Offline, Bye.. See you Again..")