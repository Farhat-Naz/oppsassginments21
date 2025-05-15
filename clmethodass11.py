class Book:
       
    def __init__(self, total_books):
        self.total_books = total_books
     
      
        
    def increament_book_count(self, count ):
            count += 1
            print("New book is add", count)
            
b1 = Book("total_books")        
b1.increament_book_count(7)    
            