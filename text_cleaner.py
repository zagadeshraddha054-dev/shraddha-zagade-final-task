class text_cleaner:
    """
    A simple class to clean and format text.

    It removes spaces, removes special characters,
    and converts text to lowercase to make it clean.
    """

    def remove_extra_space(self,s):
        # Variable to store text without spaces
        new_s = ""

        # Loop through each character in the string
        for i in s:
            # Add character only if it is not a space
            if i != " ":
                new_s += i

        # Print the result
        print("After removing spaces:", new_s)

    def remove_special_characters(self ,s):
        # Global variable to reuse cleaned text
        global new_s1
        new_s1 = ""

        # Loop through each character
        for i in s:
            # Keep only letters and numbers
            if i.isalnum():
                new_s1 += i

        # Print the result
        print("After removing special characters:", new_s1)

    def normalize_case(self):
        # Convert text to lowercase
        print("After converting to lowercase:", new_s1.lower())


# Create an object of the class
cleaner = text_cleaner()

# Predefined input text (chosen to show clear output)
text = "Hello  World!! Welcome@123"

# Call the cleaning methods
cleaner.remove_extra_space(text)
cleaner.remove_special_characters(text)
cleaner.normalize_case()
