# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as file:
        data = file.read()
    return data


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    new_word = text.replace(",", " ")
    new_word = new_word.replace("?", " ")
    new_word = new_word.replace(".", " ")
    word_list = new_word.split()
    
    word_dict = {word: word_list.count(word) for word in word_list}

    return word_dict
        
print(count_words())