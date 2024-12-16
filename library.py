class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.bBooks = []
        self.rBooks = []

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def addBook(self, id, name, quantity):

        for book in self.books:
            if book.id == id:
                print(f"Book with id {id} already exists !")
                return

        book = Book(id, name, quantity)
        self.books.append(book)
        print(f'Book "{book.name}" added successfully !')
        return book

    def addUser(self, id, name, password):

        for user in self.users:
            if user.id == id:
                print(f"User with id {id} already exists !")
                return

        user = User(id, name, password)
        self.users.append(user)
        print(f'User "{user.name}" added successfully !')
        return user

    def borrowBook(self, user, token):

        for book in self.books:
            if book.id == token:
                if book in user.bBooks:
                    print("Already borrowed !")
                    return
                elif book.quantity < 1:
                    print("No copy available !")
                    return
                else:
                    user.bBooks.append(book)
                    book.quantity -= 1
                    print("Borrowed Successfully !")

    def returnBook(self, user, token):

        for book in self.books:
            if book.id == token:

                if book in user.bBooks:
                    book.quantity += 1
                    user.rBooks.append(book)
                    user.bBooks.remove(book)
                    print("Returned Successfully !")
                else:
                    print("Not found in Borrowed List !")


pL = Library("Phitron Library")

admin =  pL.addUser(1, "admin", "1234")
habib = pL.addUser(2, "habib", "123456")

atomicHabbit = pL.addBook(1, "Atomic Habbit", 10)

currentUser = admin
changeOfUser = True


while True:

    if currentUser == None:
        print("\nNo logged in user\n")
        option = input("\nLogin\Register(L/R):")

        if option == "L":
            id = int(input("Enter Id: "))
            password = input("Enter your password: ")
        
            match = False
            for user in pL.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    changeOfUser = True
                    match = True
                    break
            if match == False:
                print("\nNo user found")
        
        elif option == "R":
            id = int(input("Enter Id: "))
            password = input("Enter your Password: ")
            name = input("Enter your Name: ")

            user = pL.addUser(id, name, password)

            currentUser = user
            changeOfUser = True
    else:
        if changeOfUser:
            print(f"Welcome back {currentUser.name} !\n")
            changeOfUser = False

        if currentUser.name == "admin":

            print("\nOptions:")
            print("\n1. Add Book")
            print("\n2. Show Users")
            print("\n3. Show Books")
            print("\n4. Logout")

            ch = int(input("\nEnter option: "))

            if ch == 1:
                id = int(input("Enter book id: "))
                quan = int(input("Enter Number of copies: "))
                name = (input("Enter book Name: "))
                pL.addBook(id, name, quan)
            
            elif ch == 2:
                pass

            elif ch == 3:
                pass
            
            elif ch == 4:
                currentUser = None

        else:
            print("\nOptions:")
            print("\n1. Borrow Book")
            print("\n2. Return Book")
            print("\n3. Show Books")
            print("\n4. Show Borrowed Books")
            print("\n5. Show History")
            print("\n6. Logout")

            ch = int(input("\nEnter option: "))

            if ch == 1:
                id = int(input("Enter Book Id: "))
                pL.borrowBook(currentUser, id)
            



                    
        

