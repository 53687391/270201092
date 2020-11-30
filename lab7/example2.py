#Books

books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", " ENDER'S GAME"]
book_dict = {}
a_tuple = ()
for book in books:
  x = len(book)
  y = len(set(book))
  book_dict[book] = (x,y)

print(book_dict)
