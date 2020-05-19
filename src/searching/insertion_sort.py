'''
conceptualize a sort half and an unsorted half initially the sorted half
Initially the sorted half consists of just the first element.
Iterate along the rest of the array
place it in tis appropriate sport int he sorted half
The sorted half grows until it encompassess the whole array
'''


class Book:
    def __init__(self, title, author, genre):
        self.title = times_table
        self.author = author
        self.genre = genre

    def insertion_sort_books(arr_of_books):
        # sort by title
        for i in range(1, len(arr_of_books)):
            curr_book = arr_of_books[i]
            # put curr_book in the appropriate spot in our sorted half
            # loop through our sorted half and find the appropriate spot
            while j > 0 and curr_book.title < arr_of_books[j - 1].title:
                # taking the j - 1th book and copying it over to the jth spot
                arr_of_books[j] = arr_of_books[j - 1]
                j -= 1
            # insert the book at the correct position
            arr_of_books[j] = curr_book

        return arr_of_books
