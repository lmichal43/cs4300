from src.task5 import favorite_books, first_three_books, student_database

def test_first_three_books():
    assert len(first_three_books) == 3

    assert first_three_books == first_three_books[:3]

def test_student_database():
    assert len(student_database) == 4
    assert student_database["Taylor Key"] == "S456"

    assert "Avery Buss" in student_database
