library = {
    101: {"TITLE": "Python Basics", "AUTHOR": "Amit", "PRICE": 300, "PUB_YEAR": 2020, "AVAILABLE": "Yes"},
    102: {"TITLE": "C Programming", "AUTHOR": "Neha", "PRICE": 250, "PUB_YEAR": 2019, "AVAILABLE": "No"},
    103: {"TITLE": "Java Guide", "AUTHOR": "Raj", "PRICE": 400, "PUB_YEAR": 2021, "AVAILABLE": "Yes"},
    104: {"TITLE": "DBMS", "AUTHOR": "Priya", "PRICE": 350, "PUB_YEAR": 2018, "AVAILABLE": "Yes"},
    105: {"TITLE": "Web Dev", "AUTHOR": "Karan", "PRICE": 450, "PUB_YEAR": 2022, "AVAILABLE": "No"}
}

# Display books with AVAILABLE = Yes
print("Available Books:\n")
for book_id, details in library.items():
    if details["AVAILABLE"] == "Yes":
        print("Book ID:", book_id)
        print("Title:", details["TITLE"])
        print("Author:", details["AUTHOR"])
        print("Price:", details["PRICE"])
        print("Year:", details["PUB_YEAR"])
        
