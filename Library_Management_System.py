books = [
    {"id" : 1, "title" : "Ikadoli", "author" : "Hanan Lashin", "category" : "Fantasy", "available" : True},
    {"id" : 2, "title" : "Coffee with Uranium", "author" : "Ahmed Khaled Tawfik", "category" : "Science Fiction", "available" : True},
    {"id" : 3, "title" : "Zikola Land", "author" : "Amr Abdel Hamid", "category" : "Fantasy", "available" : True},
    {"id" : 4, "title" : "Utopia", "author" : "Ahmed Khaled Tawfik", "category" : "Dystopian", "available" : True},
    {"id" : 5, "title" : "The Antichrist", "author" : "Ahmed Khaled Mustafa", "category" : "Historical Fiction", "available" : True},
    {"id" : 6, "title" : "The Blue Elephant", "author" : "Ahmed Mourad", "category" : "Psychological Thriller", "available" : True},
    {"id" : 7, "title" : "Diamond Dust", "author" : "Ahmed Mourad", "category" : "Crime", "available" : True},
    {"id" : 8, "title" : "Kalila wa Dimna", "author" : "Ibn al-Muqaffa", "category" : "Fable", "available" : True},
    {"id" : 9, "title" : "The Days", "author" : "Taha Hussein", "category" : "Autobiography", "available" : True},
    {"id" : 10, "title" : "The Thief and the Dogs", "author" : "Naguib Mahfouz", "category" : "Psychological Fiction", "available" : True}
]
members = [
    {"id" : 1, "name" : "Mahmoud", "borrowed_books" : []},
    {"id" : 2, "name" : "Renad", "borrowed_books" : []},
    {"id" : 3, "name" : "Menna", "borrowed_books" : []}
]
#=================== Find ===================

def find_book(book_id) :
    for book in books :
        if book["id"] == book_id :
            return book
    return None

def find_member(member_id) :
    for member in members :
        if member["id"] == member_id :
            return member
    return None
        
#================= Add Book =================

def add_book() :
    print("\n" + "=" * 45 + "\n\t\tAdd Book\n" + "=" * 45 + "\n")
    
    book_id = input("Book ID : ")

    if not book_id.isdigit() or int(book_id) <= 0 :
        print("Invalid ID, ID must be a positive number.")
        return

    book_id = int(book_id)

    if find_book(book_id) :
        print("ID already exists.")
        return

    title = input("Title : ").strip()
    author = input("Author : ").strip()
    category = input("Category : ").strip()

    if not title or not author or not category :
        print("All fields are required.")
        return

    books.append({
        "id" : book_id,
        "title" : title,
        "author" : author,
        "category" : category,
        "available" : True
    })
    print("Book added successfully.")

#================= Register Member =================

def register_member() :
    print("\n" + "=" * 45 + "\n\t\tRegister Member\n" + "=" * 45 + "\n")

    member_id = input("Member ID : ")

    if not member_id.isdigit() or int(member_id) <= 0 :
        print("Invalid ID, ID must be a positive number.")
        return

    member_id = int(member_id)

    if find_member(member_id) :
        print("Member ID already exists.")
        return

    name = input("Name : ").strip()
    if not name :
        print("Name cannot be empty.")
        return

    members.append({
        "id" : member_id,
        "name" : name,
        "borrowed_books" : []
    })
    print("Member registered successfully.")
        
#================= Search Books =================

def search_books() :
    print("\n" + "=" * 45 + "\n\t\tSearch Books\n" + "=" * 45 + "\n")

    search = input("Enter title or author or category : ").lower().strip()

    if not search :
        print("Search cannot be empty.")
        return

    found = False

    for book in books :

        if search in book["title"].lower() or search in book["author"].lower() or search in book["category"].lower() :

            print("\nID :", book["id"])
            print("Title : ", book["title"])
            print("Author :", book["author"])
            print("Category :", book["category"])
            print("Available :", book["available"])
            found = True

    if found == False :
        print("Book not found.")

#================= Borrow Book =================

def borrow_book() :
    print("\n" + "=" * 45 + "\n\t\tBorrow Book\n" + "=" * 45 + "\n")

    member_id = input("Member ID : ")

    if not member_id.isdigit() or int(member_id) <= 0 :
        print("Invalid Member ID, ID must be a positive number.")
        return
    
    
    book_id = input("Book ID : ")

    if not book_id.isdigit() or int(book_id) <= 0 :
        print("Invalid Book ID, ID must be a positive number.")
        return

    member_id = int(member_id)
    book_id = int(book_id)
    
    member = find_member(member_id)
    if not member :
        print("Member not found.")
        return

    book = find_book(book_id)
    if not book :
        print("Book not found.")
        return

    if not book["available"] :
        print("Book is not available.")
        return
    
    if len(member["borrowed_books"]) >= 3 :
        print("You can't borrow more than 3 books.")
        return
    
    book["available"] = False
    member["borrowed_books"].append(book["id"])
    print(f"Book '{book['title']}' borrowed successfully.")

#================= Return Book =================

def return_book() :
    print("\n" + "=" * 45 + "\n\t\tReturn Book\n" + "=" * 45 + "\n")

    member_id = input("Member ID : ")

    if not member_id.isdigit() or int(member_id) <= 0 :
        print("Invalid Member ID, ID must be a positive number.")
        return

    
    book_id = input("Book ID : ")

    if not book_id.isdigit() or int(book_id) <= 0 :
        print("Invalid Book ID, ID must be a positive number.")
        return

    member_id = int(member_id)
    book_id = int(book_id)
    
    member = find_member(member_id)
    if not member :
        print("Member not found.")
        return

    book = find_book(book_id)
    if not book :
        print("Book not found.")
        return

    if book_id not in member["borrowed_books"] :
        print("This member didn't borrow this book.")
        return

    book["available"] = True
    member["borrowed_books"].remove(book["id"])
    print(f"Book '{book['title']}' returned successfully.")

#================= Calculate Fine =================

def calculate_fine() :
    print("\n" + "=" * 45 + "\n\t\tCalculate Fine\n" + "=" * 45 + "\n")

    overdue_days = input("Enter overdue days : ")

    if not overdue_days.isdigit() :

        print("Invalid overdue days.")
        return

    overdue_days = int(overdue_days)

    fine_per_day = 2

    fine = overdue_days * fine_per_day

    print("Fine = ", fine)

#================= Member Report =================

def member_report() :
    member_id = input("Member ID : ")

    if not member_id.isdigit() or int(member_id) <= 0 :
        print("Invalid ID, ID must be a positive number.")
        return

    member_id = int(member_id)

    member = find_member(member_id)
    if not member :
        print("Member not found.")
        return

    print("\n" + "=" * 45 + "\n\t\tMember Report\n" + "=" * 45 + "\n")

    print("ID : ", member["id"])
    print("Name : ", member["name"])

    if len(member["borrowed_books"]) == 0 :
        print("Borrowed Books : 0")
        return
    
    print("Borrowed Books :")

    for book_id in member["borrowed_books"] :

        book = find_book(book_id)
        if book :
            print("-", book["title"])
            

#================= Show Available Books =================

def show_available_books() :
    print("\n" + "=" * 45 + "\n\t\tAvailable Books\n" + "=" * 45 + "\n")

    i = 1
    found = False
    for book in books :

        if book["available"] :

            print(i, "-", book["title"])
            found = True
            i += 1
    
    if not found :
        print("There are no available books.")

#================= Show Borrowed Books =================

def show_borrowed_books() :
    print("\n" + "=" * 45 + "\n\t\tBorrowed Books\n" + "=" * 45 + "\n")

    i = 1
    found = False
    for book in books :

        if not book["available"] :

            print(i, "-", book["title"])
            found = True
            i+= 1

    if not found :
        print("There are no borrowed books.")

#===================== Library Menu =====================

def library_menu() :
    while True :
        print("\n" + "=" * 45 + "\n\tLibrary Management System\n" + "=" * 45)
        print("1. Add Book\n2. Register Member\n3. Search Books\n4. Borrow Book\n5. Return Book\n6. Calculate Fine\n7. Member Report\n8. Show Available Books\n9. Show Borrowed Books\n0. Exit\n")
        choose = input("Enter your choice : ").strip()

        if choose == "1" :
            add_book()

        elif choose == "2" :
            register_member()

        elif choose == "3" :
            search_books()

        elif choose == "4" :
            borrow_book()

        elif choose == "5" :
            return_book()

        elif choose == "6" :
            calculate_fine()

        elif choose == "7" :
            member_report()

        elif choose == "8" :
            show_available_books()

        elif choose == "9" :
            show_borrowed_books()

        elif choose == "0" :
            print("\nThank you for using Library Management System.\n")
            break

        else :
            print("\nInvalid choice, Please choose a number from 0 to 9.")

library_menu()

#======================== Done =======================