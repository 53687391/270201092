#Books (cont.)

books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", " ENDER'S GAME"]
book_dict = {}
a_tuple = ()
for book in books:
  x = len(book)
  y = len(set(book))
  z = (x+y)/2
  book_dict[book] = (x,y,z)

print(book_dict)
