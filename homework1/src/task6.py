#reads task6_read_me.txt and counts the number of words in it
def count_words_in_file(filename):
    #open file as reading
    with open(filename, "r") as file:
        #read into string
        text = file.read()
        #split the text into words (by whitespace)
        words = text.split()

        #we get the number of words using length fucntion
        return len(words)

