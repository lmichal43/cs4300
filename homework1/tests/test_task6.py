from src.task6 import count_words_in_file

def test_task6_read_me_file():
    filename = "task6_read_me.txt"
    expected_count = 127
    result = count_words_in_file(filename)
    print("Word count is:", result)
    assert result == expected_count


