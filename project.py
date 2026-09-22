books = [
    {"id": "200", "title": "Harry Potter", "author": "J.K. Rowling", "category": "Fantasy", "quantity": 10},
    {"id": "201", "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "category": "Fantasy", "quantity": 20},
    {"id": "203", "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "quantity": 30},
    {"id": "204", "title": "Percy Jackson", "author": "Rick Riordan", "category": "Fantasy", "quantity": 5},
    {"id": "205", "title": "The Chronicles of Narnia", "author": "C.S. Lewis", "category": "Fantasy", "quantity": 15},
    {"id": "206", "title": "The Little Prince", "author": "Antoine de Saint-Exupery", "category": "Fiction", "quantity": 35},
    {"id": "207", "title": "Dracula", "author":"Bram Stoker" , "category": "Horror", "quantity": 40},
    {"id": "208", "title": "Sherlock Holmes", "author": "Arthur Conan Doyle", "category": "Mystery", "quantity": 25},
    {"id": "209", "title": "A Game of Thrones", "author": "George R.R. Martin", "category": "Fantasy", "quantity": 50},
    {"id": "210", "title": "To Kill a Mockingbird", "author":"Harper Lee" , "category": "Drama", "quantity": 55}
]
members = [
  {"id":"1","name":"sara","borrowed_books":["200"]},
  {"id":"2","name":"omar","borrowed_books":["203","204"]},
  {"id":"3","name":"Ahmed","borrowed_books":[]}
  ]
def library_menu():
    while True:
        print("\n" + "=" * 40)
        print(" Main Library Menu ")
        print("=" * 40)
        print("1. Add New Book")
        print("2. Register New Member")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Calculate Fine")
        print("7. Member Report")
        print("8. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            register_member()
        elif choice == "3":
            search_books()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            calculate_fine()
        elif choice == "7":
            member_report()
        elif choice == "8":
            print("Exiting system. Goodbye!")
            break
        else:
            print(" Invalid input! Please enter a number from 1 to 8.")
def add_book():
   title=input("Enter the title of book :")
   author=input("Enter the author of the book:")
   category=input("Enter the category of the book:")
   quatity=int(input("Enter the quantity of Newbook:"))
   if books:
       book__id=int(books[-1]['id'])+1
   else:
      book__id=1
   new_book = {
        "id": book__id,
        "title": title,
        "author": author,
        "category": category,
        "quatity": quatity
    }
   books.append(new_book)
print(books)
def register_member():
    name=input("Enter the member name:")
    if members:
      member_id = int(members[-1]["id"]) + 1
    else:
     member_id = 1
    new_member = {
        "name":name,
        "id" : member_id,
        "borrowed_books":[]
    }
    members.append(new_member)
    print(f"\nMember '{name}' registered successfully! Assigned ID: {member_id}")
def search_books():
    title_book = input("What is the title of the book? ")
    for book in books:
        if book["title"].lower() == title_book.lower():
            print(f"ID: {book['id']}, Author: {book['author']}, Category: {book['category']},quantity:{book["quantity"]}")
            return  
            
    print("This book isn't exist.")
def borrow_book():
    title_book = input("what is the title of the book? ")
    current_book = None
    
    for book in books:
        if book["title"].lower() == title_book.lower():
            print(f"quantity: {book['quantity']}")
            current_book = book
            break
    member_name = input("what is the name of the member? ")
    found_member = None

    for member in members:
        if member["name"].lower() == member_name.lower():
            found_member = member
            print(f"id: {member['id']}, borrowed_books: {member['borrowed_books']}")
            break
    if not found_member:
        print("This member is not registered!")
        return
    if len(found_member["borrowed_books"]) >= 3:
        print("Sorry you can't borrow the book (limit reached).")
    else:
        if current_book and current_book["quantity"] > 0:
            current_book["quantity"] -= 1
            found_member["borrowed_books"].append(current_book["id"])
            print(f"{found_member['name']} borrowed this book successfully!")
        else:
            print("Sorry, this book is not available or doesn't exist.")
def return_book():
    book_title = input("Enter the name of return book: ")
    member_name = input("Enter the name of the member: ")
    found_book = None
    for book in books:
        if book["title"].lower() == book_title.lower():
            found_book = book
            break
            
    if not found_book:
        print("This book does not belong to our library.")
        return
    for member in members:
        if member["name"].lower() == member_name.lower():
            if found_book["id"] in member["borrowed_books"]:
                member["borrowed_books"].remove(found_book["id"])
                found_book["quantity"] += 1
                print(f"Book '{found_book['title']}' returned successfully by {member['name']}!")
            else:
                print("This member didn't borrow this book.")
            return

    print("Member not found.")
def calculate_fine():
    borrow_day = int(input("Enter borrow day: "))
    borrow_month = int(input("Enter borrow month: "))
    borrow_year = int(input("Enter borrow year: "))
    current_day = int(input("Enter current day: "))
    current_month = int(input("Enter current month: "))
    current_year = int(input("Enter current year: "))
    total_borrow_days = (borrow_year * 360) + (borrow_month * 30) + borrow_day
    total_current_days = (current_year * 360) + (current_month * 30) + current_day
    total_days = total_current_days - total_borrow_days
    
    fine_per_day = 5
    if total_days > 7:
        late_days = total_days - 7
        fine = late_days * fine_per_day
        print(f"\nLate by {late_days} days. Total fine: {fine}")
    else:
        print("\nNo fine. Returned on time")
def member_report():
     member_name = input("Enter the name of the member: ")
     found_member = None
    
     for member in members:
        if member["name"].lower() == member_name.lower():
            found_member = member
            break
            
     if found_member:
        print(f"ID: {found_member['id']}, Borrowed books: {found_member['borrowed_books']}")
     else:
        print("This member is not registered!")
library_menu()
  
    
