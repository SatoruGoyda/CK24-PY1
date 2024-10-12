# TODO Найдите количество книг, которое можно разместить на дискете

bytes_per_book = 100 * 50 * 25 * 4
bytes_on_disk = 1.44 * 1024 * 1024
amount_of_books = int(bytes_on_disk / bytes_per_book)
print("Количество книг, помещающихся на дискету:", amount_of_books)
