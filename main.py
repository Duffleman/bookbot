def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	create_rapport(text)

def get_book_text(path):
	with open(path) as f:
		return f.read()

def count_words(text):
	return len(text.split())
	
def count_characters(text):
    alphabet_dictionary = {}
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    lowered_text = text.lower()
    for character in alphabet:
        alphabet_dictionary[character] = lowered_text.count(character)
    for key, value in alphabet_dictionary.items():
        print(f"the character {key} was found {value} times")

   
def create_rapport(text):
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{count_words(text)} words found in the document")
	print("\n")
	count_characters(text)
	print("\n")
	print("--- End report ---")
    

main()