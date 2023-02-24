books = []
books.append("learn c")
books.append("learn c++")
books.append("learn java")

print(books)

books.pop()
print("Now the top book is : ", books [-1])

books.pop()
print("Now the top book is : ", books [-1])

books.pop()
if not books:
    print("Not books left")