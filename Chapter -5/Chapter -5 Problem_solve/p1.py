#problem-1
# Write a program to create a dictionary of Bangla words with values as their English translation. Provide user with an option to look it up! 

# Bangla to English Dictionary
bangla_to_english = {
    "আপেল": "Apple",
    "বই": "Book",
    "মানুষ": "Human",
    "বাড়ি": "House",
    "গাড়ি": "Car",
    "নদী": "River",
    "সূর্য": "Sun",
    "চাঁদ": "Moon",
    "গাছ": "Tree",
    "জল": "Water"
}

def translate():
    while True:
        word = input("Enter a Bangla word (or type 'exit' to quit): ")
        if word == "exit":
            print("Exiting dictionary lookup. Goodbye!")
            break
        translation = bangla_to_english.get(word, "Sorry, this word is not in the dictionary.")
        print("English translation:", translation)

# Run the translation function
if __name__ == "__main__":
    translate()
