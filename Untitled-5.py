def add book():
    name=input enter the name f book:
    books. append (name)
    print (name is added )
 def show book():
    if len( books)==0:
        print("no of books available") 
    else:
        print ("available books ")
        for b in books:
            print (b)      
 def borrow book():
    name=input("enter the name of the book you want to borrow:")
    if name in books:
      issued_books.append(name) 
         books.remove(name)
         print (name,' is issued')

     else:
        print(name,' is not available in the library')
 def return book():
      name=input("enter the name of the book you want to return:")
      if name in issued books:
        name in issued_books:
         issued books. remove(name)
         print (name,'is returned') 
     else:
        print (name ,'is not issued ')
 def library():
    while true: