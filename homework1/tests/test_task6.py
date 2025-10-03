from src.task6 import count_words_in_file

#tests the file
def test_task6_read_me_file():
    #giving the file name
    filename = "task6_read_me.txt"
    #the expected count is 127 from the print checks
    expected_count = 127
    #calls function and stores return in result
    result = count_words_in_file(filename)
    #checking the word count
    print("Word count is:", result)
    #testing that the result is what we expected which is 27
    assert result == expected_count


