from stats import * 
import sys 

def main():
    if len(sys.argv) < 2:
        print( "Usage: python3 main.py <path_to_book>")
        print( sys.argv)
        sys.exit(1)
    book_url = sys.argv[1]
    # book_url = r"books/frankenstein.txt"

    book_text =  get_book_text(book_url)
    print(f"============ BOOKBOT ============")
    print(rf"Analyzing book found at {book_url}...")
    
    print("----------- Word Count ----------")
    book_text_counter(book_text )
    print("--------- Character Count -------") 
    text = book_char_info(book_text)
    char_info_formatted(text )
    print("============= END ===============")

if __name__ == '__main__':
    main()