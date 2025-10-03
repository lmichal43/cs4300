from src.task5 import favorite_books, first_three_books, student_database

#testing the fact that we have three books 
def test_first_three_books():
    #testing to make sure that the length of first_three_books from the code is actually 3
    assert len(first_three_books) == 3
    #testing that those are in fact the first three books and not some others
    assert first_three_books == first_three_books[:3]

#testing the student database portion
def test_student_database():
    #I gave 4 people so checks that there are in fact 4 entries
    assert len(student_database) == 4
    #we are checking that Taylor Key is in the database and that the ID in fact is correct
    assert student_database["Taylor Key"] == "S456"
    #this just confirms that avery buss is in the database
    assert "Avery Buss" in student_database
