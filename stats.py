
def get_book_text(book_path):
    # book_url = r"book\\frankenstein"
    with open(book_path) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents

def book_text_counter(book_text):
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")
      
def book_char_info(book_text):
    lowered_text = book_text.lower()
    char_dict = {}
    for curent_char in lowered_text:
        if curent_char in char_dict:
            char_dict[curent_char] +=1
        else:
            char_dict[curent_char]=1

    return dict( 
        sorted( char_dict.items(), 
               key=lambda item: item[1],
                reverse=True )
    )
def char_info_formatted(char_dict):
    for char, count in char_dict.items():
        if char.isalpha(): 
            print(f"{char}: {count}" )