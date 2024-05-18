# Linear Search
def linear_search(books, target_book):
    for i, book in enumerate(books):
        if book == target_book:
            return i
    return -1

# Binary Search
def binary_search(books, target_book):
    left, right = 0, len(books) - 1
    while left <= right:
        mid = (left + right) // 2
        if books[mid] == target_book:
            return mid
        elif books[mid] < target_book:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Recursive Binary Search
def recursive_binary_search(books, target_book, left, right):
    if left <= right:
        mid = (left + right) // 2
        if books[mid] == target_book:
            return mid
        elif books[mid] < target_book:
            return recursive_binary_search(books, target_book, mid + 1, right)
        else:
            return recursive_binary_search(books, target_book, left, mid - 1)
    return -1

# Example usage
books = ["Alice in Wonderland", "Harry Potter", "Lord of the Rings", "Pride and Prejudice", "To Kill a Mockingbird"]
target_book = "Harry Potter"

# Linear Search
linear_result = linear_search(books, target_book)
print("Linear Search Result:", linear_result)

# Binary Search (assuming books are sorted alphabetically)
books.sort()  # Sort the books alphabetically
binary_result = binary_search(books, target_book)
print("Binary Search Result:", binary_result)

# Recursive Binary Search (assuming books are sorted alphabetically)
recursive_result = recursive_binary_search(books, target_book, 0, len(books) - 1)
print("Recursive Binary Search Result:", recursive_result)





import csv

# Linear Search
def linear_search_csv(file_path, target_value):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if target_value in row:
                return i
    return -1

# Binary Search (not applicable for unsorted data)
# Recursive Binary Search (not applicable for unsorted data)

# Example usage
file_path = 'data.csv'
target_value = 'Harry Potter'

# Linear Search
linear_result = linear_search_csv(file_path, target_value)
if linear_result != -1:
    print("Linear Search Result: Found at index", linear_result)
else:
    print("Linear Search Result: Not found")

# Binary Search and Recursive Binary Search are not applicable for unsorted data in CSV files.
