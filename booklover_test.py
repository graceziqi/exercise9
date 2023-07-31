import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        t1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t1.add_book("War of the Worlds", 4)

        ## test
        testValue = "War of the Worlds" in t1.book_list['book_name'].values
        
        ## if there's an error/fail
        message = "Test value is not true."
        ## assertTrue, check if it's true
        self.assertTrue(testValue, message)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        t1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t1.add_book("War of the Worlds", 4)
        t1.add_book("War of the Worlds", 4)
        
        ## test
        testValue = t1.book_list[t1.book_list['book_name']=="War of the Worlds"]['book_name'].value_counts()[0]
        expectValue = 1
                                 
        ## check if it fails
        message = "Test value is not 1."
        ## assertEqual, check if it's true
        self.assertEqual(testValue, expectValue, message)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        t1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t1.add_book("War of the Worlds", 4)
        
        ## test
        testValue = t1.has_read("War of the Worlds")
        ## check if it fails
        message = "Test value is not true."
        ## assertTrue, check if it's false
        self.assertTrue(testValue, message)
                                 
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        t1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t1.add_book("War of the Worlds", 4)
        
        ## test
        testValue = t1.has_read("Harry Potter")
        ## check if it fails
        message = "Test value is not false."
        ## assertFalse, check if it's false
        self.assertFalse(testValue, message)
                                 
                                 
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        t1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t1.add_book("War of the Worlds", 4)
        t1.add_book("Harry Potter", 3)
        t1.add_book("The Witch", 2)
                                 
        ## test
        testValue = t1.num_books
        expectValue = 3
        ## check if fails
        message = "The number of book does not indicate the real number of books that has read."
        ## assertEqual, check if it's true
        self.assertEqual(testValue, expectValue, message)                       
                                 

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        t1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        t1.add_book("War of the Worlds", 4)
        t1.add_book("Harry Potter", 4)
        t1.add_book("The Witch", 2)                         
        
        ## test
        testValue = all(t1.fav_books().book_rating > 3)
        
        ##check if it fails
        message = "The returned books do not have rating > 3."
                                 
        ## assertTrue, check if it's true
        self.assertTrue(testValue, message)
        
if __name__ == '__main__':

    unittest.main(verbosity=3)