class TextTools:
   """
    A small helper class for working with text.

    It breaks text into words, counts them, and tracks how
    often each word appears. Simple and easy to understand.
    """
def tokenize(self, text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    # Split the text into words using spaces
    return text.split()

def word_count(self, text):
    # Convert the text into a list of words
    words = self.tokenize(text)

    # Count how many words are in the list
    return len(words)

def frequency_map(self, text):
    # Convert the text into a list of words
    words = self.tokenize(text)

    # Create an empty dictionary to store word counts
    freq = {}

    # Go through each word in the list
    #for word in words:
    # If the word is already in the dictionary, add 1
    # If not, start its count at 1
    freq[words] = freq.get(words, 0) + 1

    # Return the dictionary with word counts
    return freq


# Create an object of the TextTools class
tools = TextTools()

# Example text to analyze
text = "hello world hello"

# Show the results
print("Tokenize:", tools.tokenize(text))
print("Word Count:", tools.word_count(text))
print("Frequency Map:", tools.frequency_map(text))
